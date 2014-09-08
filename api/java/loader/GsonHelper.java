/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package loader;

import com.google.gson.Gson;



/**
 *
 * @author jderiggi
 */
public class GsonHelper {
    private static Gson g = new Gson();
    
    public static Gson get(){
        return g;
    }
    
}
