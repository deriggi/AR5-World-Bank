/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package loader;

import domain.ClimateVariable;
import domain.MonthlyCountryStat;
import domain.RCP;
import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author jderiggi
 */
public class CSVLoader {

    private final Logger log = Logger.getLogger(CSVLoader.class.getName());
    private static CSVLoader loader = new CSVLoader();
    private final String rcpstring = "rcp";
    private final String rcpDelim = "r1i1p1";
    private HashMap<String, MonthlyCountryStat> tasmax, tasmin, tas, pr;
    private HashMap<String, MonthlyCountryStat> basintasmax, basintasmin, basintas, basinpr;
    private HashMap<String, MonthlyCountryStat> regiontasmax, regiontasmin, regiontas, regionpr;

    public HashMap<String, MonthlyCountryStat> getRegiontasmax() {
        return regiontasmax;
    }

    public void setRegiontasmax(HashMap<String, MonthlyCountryStat> regiontasmax) {
        this.regiontasmax = regiontasmax;
    }

    public HashMap<String, MonthlyCountryStat> getRegiontasmin() {
        return regiontasmin;
    }

    public void setRegiontasmin(HashMap<String, MonthlyCountryStat> regiontasmin) {
        this.regiontasmin = regiontasmin;
    }

    public HashMap<String, MonthlyCountryStat> getRegiontas() {
        return regiontas;
    }

    public void setRegiontas(HashMap<String, MonthlyCountryStat> regiontas) {
        this.regiontas = regiontas;
    }

    public HashMap<String, MonthlyCountryStat> getRegionpr() {
        return regionpr;
    }

    public void setRegionpr(HashMap<String, MonthlyCountryStat> regionpr) {
        this.regionpr = regionpr;
    }

    public HashMap<String, MonthlyCountryStat> getBasintasmax() {
        return basintasmax;
    }

    public void setBasintasmax(HashMap<String, MonthlyCountryStat> basintasmax) {
        this.basintasmax = basintasmax;
    }

    public HashMap<String, MonthlyCountryStat> getBasintasmin() {
        return basintasmin;
    }

    public void setBasintasmin(HashMap<String, MonthlyCountryStat> basintasmin) {
        this.basintasmin = basintasmin;
    }

    public HashMap<String, MonthlyCountryStat> getBasintas() {
        return basintas;
    }

    public void setBasintas(HashMap<String, MonthlyCountryStat> basintas) {
        this.basintas = basintas;
    }

    public HashMap<String, MonthlyCountryStat> getBasinpr() {
        return basinpr;
    }

    public void setBasinpr(HashMap<String, MonthlyCountryStat> basinpr) {
        this.basinpr = basinpr;
    }

    public HashMap<String, MonthlyCountryStat> getMap(ClimateVariable cv) {
        if (cv.equals(ClimateVariable.pr)) {
            return pr;
        }
        if (cv.equals(ClimateVariable.tas)) {
            return tas;
        }
        if (cv.equals(ClimateVariable.tasmin)) {
            return tasmin;
        }
        return tasmax;

    }
    public HashMap<String, MonthlyCountryStat> getBasinMap(ClimateVariable cv) {
        if (cv.equals(ClimateVariable.pr)) {
            return basinpr;
        }
        if (cv.equals(ClimateVariable.tas)) {
            return basintas;
        }
        if (cv.equals(ClimateVariable.tasmin)) {
            return basintasmin;
        }
        return basintasmax;

    }
    
     public HashMap<String, MonthlyCountryStat> getRegionMap(ClimateVariable cv) {
        if (cv.equals(ClimateVariable.pr)) {
            return regionpr;
        }
        if (cv.equals(ClimateVariable.tas)) {
            return regiontas;
        }
        if (cv.equals(ClimateVariable.tasmin)) {
            return regiontasmin;
        }
        return regiontasmax;

    }

    public HashMap<String, MonthlyCountryStat> getTasmax() {
        return tasmax;
    }

    public HashMap<String, MonthlyCountryStat> getTasmin() {
        return tasmin;
    }

    public HashMap<String, MonthlyCountryStat> getTas() {
        return tas;
    }

    public HashMap<String, MonthlyCountryStat> getPr() {
        return pr;
    }

    public static CSVLoader get() {
        return loader;
    }

    public void setPr(HashMap<String, MonthlyCountryStat> pr) {
        this.pr = pr;
    }

    public void setTas(HashMap<String, MonthlyCountryStat> tas) {
        this.tas = tas;
    }

    public void setTasmin(HashMap<String, MonthlyCountryStat> tasmin) {
        this.tasmin = tasmin;
    }

    public void setTasmax(HashMap<String, MonthlyCountryStat> tasmax) {
        this.tasmax = tasmax;
    }

    private String parseModel(String model) {
        if (model == null) {
            return null;
        }
        model = model.toLowerCase();
        int rcpIndex = model.indexOf(rcpstring);

        if (rcpIndex < 0) {
            return null;
        }

        return model.substring(0, rcpIndex - 1);
    }

    private String[] parseYears(String model) {
        if (model == null) {
            return null;
        }

        return model.substring(model.lastIndexOf("_") + 1, model.lastIndexOf(".")).split("\\-");
    }

    private RCP parseRcp(String model) {
        if (model == null) {
            return null;
        }
        model = model.toLowerCase();
        int rcpIndex = model.indexOf(rcpstring);
        int rcpDelimIndex = model.indexOf(rcpDelim);

        if (rcpIndex < 0 || rcpDelimIndex < 0) {
            return null;
        }

        String parsedRcp = model.substring(rcpIndex, rcpDelimIndex - 1);
        RCP rcp = RCP.valueOf(parsedRcp);

        return rcp;
    }

//    private void load(ServletContext context, String path) {
    public HashMap<String, MonthlyCountryStat> load(String path, ClimateVariable cv) {
        BufferedReader br = null;

        HashMap<String, MonthlyCountryStat> countryStatMap = new HashMap<String, MonthlyCountryStat>();

        try {
            //        InputStream resourceContent = context.getResourceAsStream("/WEB-INF/test/foo.txt")

//            InputStream resourceContent = context.getResourceAsStream(path);
            log.log(Level.INFO, "trying to load {0}", path);
            InputStreamReader isr = new InputStreamReader(new FileInputStream(path));
            br = new BufferedReader(isr);
            String line = null;


            MonthlyCountryStat mcs = null;
            int lastMonth = 0;
            int counter = 0;
            while ((line = br.readLine()) != null) {
                String[] parts = line.split("\\,");
                String model = parseModel(parts[0]);
                RCP rcp = parseRcp(parts[0]);
                String countryCode = parts[1];
                int month = Integer.parseInt(parts[2]);
                float val = Float.parseFloat(parts[3]);
                String[] parsedYears = parseYears(parts[0]);
                int startYear = Integer.parseInt(parsedYears[0]);
                int endYear = Integer.parseInt(parsedYears[1]);

                String key = new StringBuilder().append(countryCode).append(model).append(startYear).append(rcp).toString();
                if(!countryStatMap.containsKey(key)){
                    mcs = new MonthlyCountryStat(rcp, cv, model, countryCode, startYear, endYear);
                    countryStatMap.put(key, mcs);
                }
                mcs = countryStatMap.get(key);
                mcs.add(val, month-1);
                
//                if (mcs == null || mcs.getDataSize() == 12) {
//                    
//                    String key = new StringBuilder().append(countryCode).append(model).append(startYear).append(rcp).toString();
////                    System.out.println(key);
//                    if (countryStatMap.get(key) == null) {
//                        countryStatMap.put(key, new ArrayList<MonthlyCountryStat>());
//                    }
//                    countryStatMap.get(key).add(mcs);
//
//                    lastMonth = 0;
//
//                } 

                
//                mcs.add(val, month-1);
//                lastMonth = month;
//                counter++;
            }
            log.log(Level.INFO, "done loading {0} items into a map of size {1}", new Object[]{ countryStatMap.size()});


        } catch (IOException ex) {
            Logger.getLogger(CSVLoader.class.getName()).log(Level.SEVERE, null, ex);
        } finally {
            try {
                br.close();
            } catch (IOException ex) {
                Logger.getLogger(CSVLoader.class.getName()).log(Level.SEVERE, null, ex);
            }
        }
        return countryStatMap;

    }

    public static void main(String[] args) {
                    HashMap<String, MonthlyCountryStat> basintasmax = CSVLoader.get().load("C:\\Users\\jderiggi\\Documents\\NetBeansProjects\\ClimateAPIV2\\src\\main\\webapp\\WEB-INF\\tasmax\\basin_tasmax_model_means.csv", ClimateVariable.tasmax);
                    HashMap<String, MonthlyCountryStat> basintas = CSVLoader.get().load("C:\\Users\\jderiggi\\Documents\\NetBeansProjects\\ClimateAPIV2\\src\\main\\webapp\\WEB-INF\\tas\\basin_tas_model_means.csv", ClimateVariable.tas);
                    HashMap<String, MonthlyCountryStat> basinpr = CSVLoader.get().load("C:\\Users\\jderiggi\\Documents\\NetBeansProjects\\ClimateAPIV2\\src\\main\\webapp\\WEB-INF\\pr\\basin_pr_model_means.csv", ClimateVariable.pr);
                    HashMap<String, MonthlyCountryStat> basintasmin = CSVLoader.get().load("C:\\Users\\jderiggi\\Documents\\NetBeansProjects\\ClimateAPIV2\\src\\main\\webapp\\WEB-INF\\tasmin\\basin_tasmin_model_means.csv", ClimateVariable.tasmin);
                    
//                    HashMap<String, MonthlyCountryStat> countrytasmax = CSVLoader.get().load("C:\\Users\\jderiggi\\Documents\\NetBeansProjects\\ClimateAPIV2\\src\\main\\webapp\\WEB-INF\\tasmax\\basin_tasmax_model_means.csv", ClimateVariable.tasmax);
//                    HashMap<String, MonthlyCountryStat> countrytas = CSVLoader.get().load("C:\\Users\\jderiggi\\Documents\\NetBeansProjects\\ClimateAPIV2\\src\\main\\webapp\\WEB-INF\\tas\\basin_tas_model_means.csv", ClimateVariable.tas);
//                    HashMap<String, MonthlyCountryStat> countrypr = CSVLoader.get().load("C:\\Users\\jderiggi\\Documents\\NetBeansProjects\\ClimateAPIV2\\src\\main\\webapp\\WEB-INF\\pr\\basin_pr_model_means.csv", ClimateVariable.pr);
//                    HashMap<String, MonthlyCountryStat> countrytasmin = CSVLoader.get().load("C:\\Users\\jderiggi\\Documents\\NetBeansProjects\\ClimateAPIV2\\src\\main\\webapp\\WEB-INF\\tasmin\\basin_tasmin_model_means.csv", ClimateVariable.tasmin);
                    
//        ArrayList<HashMap<String, MonthlyCountryStat>> countryStatMaps = new ArrayList<HashMap<String, MonthlyCountryStat>>();
//
//        int num = 16;
//
//        for (int i = 0; i < num; i++) {
//            CSVLoader.get().load("C:\\Users\\jderiggi\\Documents\\Climate\\climatev2\\tasmax_model_means (1)\\model_means.csv");
//            System.out.println(countryStatMaps.size());
//        }
    }

    private CSVLoader() {
    }
}
