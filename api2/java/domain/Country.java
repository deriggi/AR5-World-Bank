/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package domain;

import java.util.HashSet;
import java.util.Set;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author jderiggi
 */
public class Country {
    
    private static final Logger log = Logger.getLogger(Country.class.getName());
    
    private String triCode;
    private Set<MonthlyCountryStat> countryStats = new HashSet<MonthlyCountryStat>();
    private void setTriCode(String code){
        
        if(code!= null && code.length() == 3){
            this.triCode = code;
        }
        else{
            log.log(Level.INFO, "country codes must be of length three");
        }
        
    }
    
    
    
}
