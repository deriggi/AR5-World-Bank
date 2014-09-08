/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package resource;

import domain.ClimateVariable;
import javax.ws.rs.GET;
import javax.ws.rs.Path;
import javax.ws.rs.PathParam;
import javax.ws.rs.Produces;
import javax.ws.rs.core.MediaType;
import loader.CSVLoader;
import loader.GsonHelper;

/**
 *
 * @author jDeRiggi
 */

@Path("mcs")
public class MonthlyCountryResource {
    
    @GET
    @Path("/mavg/{cv}/country/{country}/{model}")
    @Produces(MediaType.APPLICATION_JSON)
    public String getMonthlyCountry(@PathParam("cv") String cv, @PathParam("model") String model, @PathParam("country") String country){
        
        return GsonHelper.get().toJson(CSVLoader.get().getMap(ClimateVariable.valueOf(cv)).get(new StringBuilder().append(country).append(model).toString()));
        
    }
    
    @GET
    @Path("/mavg/{cv}/country/{key}")
    @Produces(MediaType.APPLICATION_JSON)
    public String getMonthlyCountryFromKey(@PathParam("cv") String cv, @PathParam("key") String key){
        
        return GsonHelper.get().toJson(CSVLoader.get().getMap(ClimateVariable.valueOf(cv)).get(key));
        
    }
    
    
    @GET
    @Path("/mavg/{cv}/basin/{key}")
    @Produces(MediaType.APPLICATION_JSON)
    public String getMonthlyBasinFromKey(@PathParam("cv") String cv, @PathParam("key") String key){
        
        return GsonHelper.get().toJson(CSVLoader.get().getBasinMap(ClimateVariable.valueOf(cv)).get(key));
        
    }
    
    @GET
    @Path("/mavg/{cv}/region/{key}")
    @Produces(MediaType.APPLICATION_JSON)
    public String getMonthlyRegionFromKey(@PathParam("cv") String cv, @PathParam("key") String key){
        
        return GsonHelper.get().toJson(CSVLoader.get().getRegionMap(ClimateVariable.valueOf(cv)).get(key));
        
    }
     
    @GET
    @Path("/mavg/{cv}/basin/{country}/{model}")
    @Produces(MediaType.APPLICATION_JSON)
    public String getMonthlyBasin(@PathParam("cv") String cv, @PathParam("model") String model, @PathParam("country") String country){
        
        return GsonHelper.get().toJson(CSVLoader.get().getBasinMap(ClimateVariable.valueOf(cv)).get(new StringBuilder().append(country).append(model).toString()));
        
    }
}
