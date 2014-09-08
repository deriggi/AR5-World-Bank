/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package domain;

import java.util.ArrayList;

/**
 *
 * @author jderiggi
 */
public class MonthlyCountryStat {
    
    // 
    private Float[] data = new Float[12];
//    private String model;
    private RCP rcp;
//    private ClimateVariable cv;
    private String countryCode;
    private int startYear;//, endYear;
    
    public MonthlyCountryStat(RCP rcp, ClimateVariable cv, String model, String countryCode, int startYear, int endYear){
//        this.model = model;
//        this.cv = cv;
        this.rcp = rcp;
        this.countryCode = countryCode;
        this.startYear = startYear;
//        this.endYear = endYear;
    }
    
    public void add (float val, int index){
        data[index] = val;
    }
    
    public int getDataSize(){
        return data.length;
    }
    
    public void addData(int month, float val){
//        this.data.add(month-1, val);
    }
    
//    public ClimateVariable getCv() {
//        return cv;
//    }
//
//    public void setCv(ClimateVariable cv) {
//        this.cv = cv;
//    }
    
//    public String getModel() {
//        return model;
//    }
//
//    public void setModel(String model) {
//        this.model = model;
//    }

    public RCP getRcp() {
        return rcp;
    }

    public void setRcp(RCP rcp) {
        this.rcp = rcp;
    }
    
    
}
