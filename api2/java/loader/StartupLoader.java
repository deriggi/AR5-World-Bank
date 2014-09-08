/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package loader;

import domain.ClimateVariable;
import domain.MonthlyCountryStat;
import java.util.ArrayList;
import java.util.HashMap;
import javax.servlet.ServletContext;
import javax.servlet.ServletContextEvent;
import javax.servlet.ServletContextListener;
import javax.servlet.annotation.WebListener;

/**
 * Web application lifecycle listener.
 *
 * @author jderiggi
 */
@WebListener()
public class StartupLoader implements ServletContextListener {

    @Override
    public void contextInitialized(ServletContextEvent sce) {
        ServletContext context = sce.getServletContext();
        
        String prbase =     "/WEB-INF/pr/";               
        String tasbase =     "/WEB-INF/tas/";               
        String tasmaxbase =     "/WEB-INF/tasmax/";               
        String tasminbase =     "/WEB-INF/tasmin/";               
        
        HashMap<String, MonthlyCountryStat> tasmaxMcs = CSVLoader.get().load(context.getRealPath("/WEB-INF/tasmax/country_tasmax_model_means.csv"), ClimateVariable.tasmax );
        CSVLoader.get().setTasmax(tasmaxMcs);
        HashMap<String, MonthlyCountryStat> tasmaxBcs = CSVLoader.get().load(context.getRealPath("/WEB-INF/tasmax/basin_tasmax_model_means.csv"), ClimateVariable.tasmax );
        CSVLoader.get().setBasintasmax(tasmaxBcs);
        HashMap<String, MonthlyCountryStat> tasmaxRcs = CSVLoader.get().load(context.getRealPath("/WEB-INF/tasmax/region_tasmax_model_means.csv"), ClimateVariable.tasmax);
        CSVLoader.get().setRegionpr(tasmaxRcs);
        
        HashMap<String, MonthlyCountryStat> prMcs = CSVLoader.get().load(context.getRealPath("/WEB-INF/pr/country_pr_model_means.csv"), ClimateVariable.pr);
        CSVLoader.get().setPr(prMcs);
        HashMap<String, MonthlyCountryStat> prBcs = CSVLoader.get().load(context.getRealPath("/WEB-INF/pr/basin_pr_model_means.csv"), ClimateVariable.pr);
        CSVLoader.get().setBasinpr(prBcs);
        HashMap<String, MonthlyCountryStat> prRcs = CSVLoader.get().load(context.getRealPath("/WEB-INF/pr/region_pr_model_means.csv"), ClimateVariable.pr);
        CSVLoader.get().setRegionpr(prRcs);
        
        
        HashMap<String, MonthlyCountryStat> tasminMcs = CSVLoader.get().load(context.getRealPath("/WEB-INF/tasmin/country_tasmin_model_means.csv"), ClimateVariable.tasmin);
        CSVLoader.get().setTasmin(tasminMcs);
        HashMap<String, MonthlyCountryStat> tasminBcs = CSVLoader.get().load(context.getRealPath("/WEB-INF/tasmin/basin_tasmin_model_means.csv"), ClimateVariable.tasmin);
        CSVLoader.get().setBasintasmin(tasminBcs);
        HashMap<String, MonthlyCountryStat> tasminRcs = CSVLoader.get().load(context.getRealPath("/WEB-INF/tasmin/region_tasmin_model_means.csv"), ClimateVariable.tasmin);
        CSVLoader.get().setRegionpr(tasminRcs);
        
        HashMap<String, MonthlyCountryStat> tasMcs = CSVLoader.get().load(context.getRealPath("/WEB-INF/tas/country_tas_model_means.csv"), ClimateVariable.tas);
        CSVLoader.get().setTas(tasMcs);
        HashMap<String, MonthlyCountryStat> tasBcs = CSVLoader.get().load(context.getRealPath("/WEB-INF/tas/basin_tas_model_means.csv"), ClimateVariable.tas);
        CSVLoader.get().setBasintas(tasBcs);
        HashMap<String, MonthlyCountryStat> tasRcs = CSVLoader.get().load(context.getRealPath("/WEB-INF/tas/region_tas_model_means.csv"), ClimateVariable.tas);
        CSVLoader.get().setRegiontas(tasRcs);
        
        
    }

    @Override
    public void contextDestroyed(ServletContextEvent sce) {
//        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }
}
