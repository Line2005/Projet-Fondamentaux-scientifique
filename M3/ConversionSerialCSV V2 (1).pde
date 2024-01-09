//From Arduino to Processing to Txt or cvs etc. 
//inclusion des librairies 
import processing.serial.*;


//Déclaration des variable de fichier et de port USB
PrintWriter output; // Flux de Sortie vers le fichier CSV
Serial udSerial;//Port Serie pour la communication avec Arduino 

int previousMillis=0;
int interval=100 ; 
int counter= 0 ; 
int currentMillis=millis();//Ecrire les données de pouls et de temp dans le fichier CSV

//Initialisation du port USB et du fichier 
void setup() {
  udSerial = new Serial(this, "COM7", 115200);//Ouvrir le port série à 115200 bauds 
  String[] headers = {"Pulses","Time (ms)"};
  output = createWriter ("Battement.csv"); // Ecrire l'en-tête  du fichier CSV 
  output.println(join(headers,","));
  
}
  //Récupération des données envoyées par l'Arduino et son écriture sur la console + le fichiers
  void draw() {
    
    if (udSerial.available() > 0) {
      String SenVal = udSerial.readString();
      if (SenVal != null) {
        System.out.println(SenVal);
        output.println(SenVal+","+currentMillis );
        if (currentMillis-previousMillis >= interval) {
          System.out.println(currentMillis);
          output.println(currentMillis);
          previousMillis=currentMillis ; 
          counter++;
      }
      }
    }
  }
  //Pression d'une touche -> écriture sur le fichier csv + extinction du programme 
  void keyPressed(){//Fermer le fichier CSV et quitter le programme si on appuie sur une touche 
    output.flush();
    output.close();
    exit(); 
  }
