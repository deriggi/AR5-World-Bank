package jd.prepender;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 * Hello world!
 *
 */
public class Cru321Reader {

    public static final String LINE_SEPARATOR = System.getProperty("line.separator");

    public void prepend(int year, int month) {
        FileWriter fw = null;
        InputStreamReader isr = null;
        try {
            
            fw = new FileWriter("D:/cru_ts3.21.1901.2012.tmp_" +year + "_" + month + ".asc");
            fw.write("ncols  720");
            fw.write(LINE_SEPARATOR);
            fw.write("nrows  360");
            fw.write(LINE_SEPARATOR);

            fw.write("xllcorner  -180");
            fw.write(LINE_SEPARATOR);

            fw.write("yllcorner  -89.9999999999999");
            fw.write(LINE_SEPARATOR);

            fw.write("cellsize 0.5");
            fw.write(LINE_SEPARATOR);

            fw.write("NODATA_value  -999");
            fw.write(LINE_SEPARATOR);

            

            isr = new InputStreamReader(new FileInputStream(new File("D:/cru_ts3.21.1901.2012.tmp.dat")));
            BufferedReader br = new BufferedReader(isr);
            String line = null;
            int lineCounter = 0;
            ArrayList<String> lineContainer = new ArrayList<String>();
            int cruIndex = ((year - 1901) * 12) + month;
            System.out.println("from " + 361*cruIndex + " " + (361*cruIndex - 361) );
            
            int max = (360*cruIndex);
            int min = (360*cruIndex - 360);
            while ((line = br.readLine()) != null && lineCounter < max) {
                if (line.trim().length() == 0){
                    continue;
                }
                if (lineCounter >= min){
                    
                    lineContainer.add(line);
                } 
                
                lineCounter++;
//                System.out.println(line);
            }
            System.out.println("ROWSNUM " + lineContainer.size());
            
            int rowsWritten  = 0;
            for (int i = lineContainer.size() - 1; i >= 0; i--) {
                fw.write(lineContainer.get(i));
                if(i>0){
                    
                    
                }
                fw.write(LINE_SEPARATOR);
                rowsWritten++;
            }
            System.out.println("rows written " + rowsWritten);
        } catch (IOException ex) {
            Logger.getLogger(Cru321Reader.class.getName()).log(Level.SEVERE, null, ex);
            
        } finally{
            try {
                fw.close();
                isr.close();
                
            } catch (IOException ex) {
                Logger.getLogger(Cru321Reader.class.getName()).log(Level.SEVERE, null, ex);
            }
            
        }

    }
    
    public static void main(String[] args){
        new Cru321Reader().prepend(1901, 1);
    }
}