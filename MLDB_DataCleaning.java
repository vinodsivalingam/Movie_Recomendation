
package pipeseparatedfile;

import com.csvreader.CsvReader;
import com.csvreader.CsvWriter;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;

public class MLDB_DataCleaning {

    
    public static void main(String[] args) throws FileNotFoundException, IOException {
       try{
        String outputFile = "M:\\MLDBMergedDataset_GenreJAVAOutputFile_LargeDataset.csv";
        CsvReader mov_rating = new CsvReader("M:\\merge2.csv"); 
        mov_rating.readHeaders();
        CsvWriter csvOutput = new CsvWriter(new FileWriter(outputFile,true),',');
       // csvOutput.app
            csvOutput.write("movieId");
            csvOutput.write("userId");
            csvOutput.write("rating");
            csvOutput.write("genres");
            csvOutput.endRecord();
            
       while(mov_rating.readRecord()){
       
            String movieId =mov_rating.get("movieId");
            String userId = mov_rating.get("userId");
            String rating = mov_rating.get("rating");            
            String genres = mov_rating.get("genres");
            String[] splitLine = genres.split("\\|");
            genres=splitLine[0];
            
            
            csvOutput.write(movieId);
            csvOutput.write(userId);
            csvOutput.write(rating);
            csvOutput.write(genres);
            csvOutput.endRecord();
            System.out.println("InsertSucessful");
            
        }
       mov_rating.close();
       csvOutput.close();
       }catch(FileNotFoundException e){
           e.printStackTrace();
       }catch(IOException e){
           e.printStackTrace();
       }
        
       /* String[] splitLine = line.split(",");
        //for(int i=0;i<splitLine.length;i++){
            String[] genres = splitLine[1].split("\\|");
            splitLine[1] = genres[0];
            for(int j=0;j<splitLine.length;j++){
                //if(genres[i]=="Action" || genres[i]=="Comedy" || genres[i]=="Romance" )
                System.out.println(splitLine[j]);
            }*/
          
        
        //}
    }
    
}
