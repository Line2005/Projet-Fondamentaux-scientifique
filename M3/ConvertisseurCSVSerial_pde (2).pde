import processing.serial.*;
import processing.data.Table;


PrintWriter output  ;  // Flux de Sortie vers le fichier CSV
Serial udSerial;//Port Serie pour la communication avec Arduino 
Table tableau_donnees ; // le tableau qui va contenir les donnes
int ligne = 0 ; // le nombre de ligne qu'il y a dans le tableau

void setup(){
  size(400,400);
  udSerial = new Serial(this, "COM6", 9600);//Ouvrir le port série à 9600 bauds 
  tableau_donnees=new Table();// Creation d'une Table
  tableau_donnees.addColumn("Pouls");// Creation d'une Colonne 'Pouls"
  tableau_donnees.addColumn("Temps"); // Creation d'une Colonne 'Temps"
  output=createWriter("Battements.csv"); // Ecrire l'en-tête  du fichier CSV  

}

  void draw(){
    while (udSerial.available() > 0) {
       String SenVal = udSerial.readStringUntil('\n'); //Lit une ligne de données sur le port Serie 
       if (SenVal != null) {// Si la ligne n'est pas vide 
          String [] values=split(SenVal,';');//Separe les valeurs de la ligne par une semi-colon,*
          System.out.println(SenVal);
          output.println(SenVal);
          if (values.length == 1) {
            float pouls= float(values[0]);
            output.println(pouls+";"+millis());
            TableRow ligne2=tableau_donnees.addRow();// Cree un range dans le tableau
            ligne2.setInt("Pouls",int(SenVal));// Envoie les pouls du Serie 
            ligne2.setInt("Temps",millis());// Envoie les donnees 
            ligne++;  // Incremente le nombre de ligne 
        }
     }
  }
       if (ligne%20==0){//Attend que le nombre de ligne arrive à 50 pour sauvergarder 
     saveTable(tableau_donnees,"Battements.csv"); // Sauvergarde les données dans le fichier CSV
         ligne=0;//remett le nombre de ligne  à zero
   }
}


    
   void keyPressed(){//Fermer le fichier CSV et quitter le programme si on appuie sur une touche 
    output.flush();
    output.close();
    exit(); 
  }
