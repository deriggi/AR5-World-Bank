/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package application;

import java.util.HashSet;
import java.util.Set;
import javax.ws.rs.ApplicationPath;
import javax.ws.rs.core.Application;
import resource.MonthlyCountryResource;

/**
 *
 * @author jDeRiggi
 */
@ApplicationPath("v2")
public class ClimateAPIv2Application extends Application{
    
    @Override
    public Set<Class<?>> getClasses() {
        Set<Class<?>> s = new HashSet<Class<?>>();
        s.add(MonthlyCountryResource.class);
        return s;
    }  
    
    
    private void addRestResourceClasses(Set<Class<?>> resources) {
         resources.add(resource.MonthlyCountryResource.class);
     }
    
    
}
