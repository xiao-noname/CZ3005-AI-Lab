import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.text.ParseException;
import java.util.Iterator;
import java.util.Set;

import org.json.*;
import org.json.simple.*;
import org.json.simple.parser.JSONParser;

public class readFile {
    private int fileno;
    JSONParser parser = new JSONParser();
    JSONObject weightObject;
    JSONObject energyObject;
    public readFile(){
        
		try {
			Object NodeWeight = parser.parse(new FileReader("Lab1/Dist.json"));
            Object eCost = parser.parse(new FileReader("Lab1/Cost.json"));
            weightObject = (JSONObject) NodeWeight;
            energyObject = (JSONObject) eCost;
            Set keys = weightObject.keySet();
            Iterator a = keys.iterator();
            while(a.hasNext())
            {
                String b = (String) a.next();   //split the key and create edges
                System.out.println(energyObject.get(b));   //read in the energy file to get the cost
            }
            
            //JSONArray AdjacencyList = (JSONArray) jsonObject.get("1");
            //System.out.println(AdjacencyList);

        }
        catch (Exception e) {
			e.printStackTrace();
        }
        
    }
    public void createEdges()
    {

    }
    
}
