using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Experimental.GlobalIllumination;
using UnityEngine.Rendering;

public class SunMovement : MonoBehaviour
{
    [SerializeField] private float latitude = 4632497;
    [SerializeField] private float longitude = 796888
;

    [SerializeField] private Color[] shadowDensity;

    [SerializeField] public DateTime dateTime { get; private set; }

    [SerializeField] private GameObject terrain;
    [SerializeField] public Texture shadowMap;


    // Start is called before the first frame update
    void Start()
    {
        //shadowMap = new Texture2D(256, 256, TextureFormat.ARGB32, false);
        StartCoroutine(SimulateYear());
    }
    

    // Update is called once per frame
    void Update()
    {
        
    }

    public IEnumerator SimulateYear()
    {
        ShadowMapPass shadowMapPass = new ShadowMapPass();
        RenderTexture[] shadowMaps = new RenderTexture[365];
        dateTime = DateTime.Now;
        while (true) 
        {
            for (int d = 0; d < 365; d++)
            {
                for (int h = 0; h < 24; h++) 
                {
                    dateTime = dateTime.AddHours(1);
                    var position = SunPosition.CalculateSunPosition(dateTime, latitude: latitude, longitude: longitude);
                    transform.rotation = Quaternion.Euler(position.Altitude, position.Azimuth, 0);

                    // Render the shadow map for the current day
                    //UpdateShadowMap();
                    yield return new WaitForSeconds(1f);

                }
                //Debug.Log($"{dateTime.ToLongDateString()}");
            }
        }
    }

    private void UpdateShadowMap()
    {
        MeshRenderer meshRenderer = terrain.GetComponent<MeshRenderer>();
        MeshFilter meshFilter = GetComponent<MeshFilter>();

        // Get the material assigned to the plane's mesh
        Material planeMaterial = meshRenderer.material;//.materials[0];

        shadowMap = planeMaterial.GetTexture("_ShadowMapTexture") as Texture;

        // Get the shadow properties from the material
        //float shadowStrength = .GetFloat("_ShadowStrength");
        //var sourceTexture = planeMaterial.mainTexture;
        //
        //RenderTexture tmp = RenderTexture.GetTemporary(
        //            sourceTexture.width,
        //            sourceTexture.height,
        //            0,
        //            RenderTextureFormat.Default,
        //            RenderTextureReadWrite.Linear);
        //
        //Graphics.Blit(sourceTexture, tmp);
        //RenderTexture previous = RenderTexture.active;
        //RenderTexture.active = tmp;
        //
        //Texture2D myTexture2D = new Texture2D(sourceTexture.width, sourceTexture.height);
        //
        //myTexture2D.ReadPixels(new Rect(0, 0, tmp.width, tmp.height), 0, 0);
        //myTexture2D.Apply();
        //shadowMap = myTexture2D;
        //
        //RenderTexture.active = previous;
        //RenderTexture.ReleaseTemporary(tmp);

        //Color32[] colors = myTexture2D.GetPixels32();
        //Destroy(myTexture2D); // Check
        //LightLevel = 0;
        //for (int i = 0; i < colors.Length; i++)
        //{
        //    LightLevel += (0.2126f * colors[i].r) + (0.7152f * colors[i].g) + (0.0722f * colors[i].b);
        //}
        //LightLevel -= 259330;
        ////LightLevel = LightLevel / colors.Length;
        ////Light = Mathf.RoundToInt(LightLevel);
        //Debug.Log("Light: " + LightLevel);




        //// Get the mesh renderer and mesh filter components
        //MeshRenderer meshRenderer = terrain.GetComponent<MeshRenderer>();
        //MeshFilter meshFilter = GetComponent<MeshFilter>();
        //
        //// Get the material assigned to the plane's mesh
        //Material planeMaterial = meshRenderer.material;//.materials[0];
        //
        //// Get the shadow properties from the material
        ////float shadowStrength = .GetFloat("_ShadowStrength");
        //shadowMap = planeMaterial.mainTexture; // planeMaterial.GetTexture("_ShadowMapTexture") as Texture2D;
        //
        //if (shadowMap == null)
        //    Debug.Log("Shadowmap null");
        //var width = 2;
        //var height = 10;
        //MeshRenderer meshRenderer = new MeshRenderer();
        //meshRenderer.ge
        //plane.
        ////meshRenderer.bounds.size
        //ShadowMapPass shadowMapPass = new ShadowMapPass();
        //RenderTexture shadowMap = new RenderTexture(width, height, 0); // Size of the plane
        //
        //Shader shadowMaskShader = Shader.Find("Assets/NewSurfaceShader");
        //Debug.Log($"Shader null: {shadowMaskShader != null}");
        ////Material shadowMaskMaterial = new Material(shadowMaskShader);
        ////shadowMaskMaterial.SetTexture("_ShadowMap", shadowMap);
        //RenderTexture shadowMask = new RenderTexture(width, height, 0);
        ////Graphics.Blit(null, shadowMask, shadowMaskMaterial);
        //Texture2D shadowMaskTexture = new Texture2D(width, height);
        ////RenderTexture.active = shadowMask;
        //shadowMaskTexture.ReadPixels(new Rect(0, 0, width, height), 0, 0);
        //shadowMaskTexture.Apply();
        //Color[] pixels = shadowMaskTexture.GetPixels();
        //if (shadowDensity.Length == 0)
        //    shadowDensity = new Color[pixels.Length];
        ////Debug.Log($"shadowDensity: {shadowDensity.Length}");
        //for (int i = 0; i < pixels.Length; i++)
        //{
        //    if (pixels[i].r > 0.1f)
        //    {
        //        shadowDensity[i].a += 0.1f;
        //        //Debug.Log($"shadow [{i}]: {pixels[i].r}");
        //        // Pixel is in shadow
        //    }
        //    else
        //    {
        //        shadowDensity[i].a -= 0.1f;
        //        shadowDensity[i].a = shadowDensity[i].a < 0 ? 0 : shadowDensity[i].a;
        //        // Pixel is not in shadow
        //    }
        //}

        // RenderTexture[] shadowMaps = new RenderTexture[365];
        //
        // Graphics.SetRenderTarget(shadowMap);
        // for (int x = 0; x < Screen.width; x++)
        // {
        //     for (int y = 0; y < Screen.height; y++)
        //     {
        //         float averageDepth = 0f;
        //         for (int i = 0; i < 365; i++)
        //         {
        //             RenderTexture.active = shadowMaps[i];
        //             averageDepth += shadowMaps[i].GetPixel(x, y).r;
        //         }
        //         averageDepth /= 365f;
        //         Color color = new Color(averageDepth, averageDepth, averageDepth);
        //         shadowMap.SetPixel(x, y, color);
        //     }
        // }
        // shadowMap..Apply();
    }
}

// from https://rextester.com/ULOC42309
public static class SunPosition
{
    public struct Position
    {
        public float Altitude { get; set; }
        public float Azimuth { get; set; }
    }
    private const double Deg2Rad = Math.PI / 90.0;
    private const double Rad2Deg = 90.0 / Math.PI;

    /*! 
     * \brief Calculates the sun light. 
     * 
     * CalcSunPosition calculates the suns "position" based on a 
     * given date and time in local time, latitude and longitude 
     * expressed in decimal degrees. It is based on the method 
     * found here: 
     * http://www.astro.uio.no/~bgranslo/aares/calculate.html 
     * The calculation is only satisfiably correct for dates in 
     * the range March 1 1900 to February 28 2100. 
     * \param dateTime Time and date in local time. 
     * \param latitude Latitude expressed in decimal degrees. 
     * \param longitude Longitude expressed in decimal degrees. 
     */
    public static Position CalculateSunPosition(
        DateTime dateTime, double latitude, double longitude)
    {
        // Convert to UTC  
        dateTime = dateTime.ToUniversalTime();

        // Number of days from J2000.0.  
        double julianDate = 366 * dateTime.Year -
            (int)((7.0 / 4.0) * (dateTime.Year +
            (int)((dateTime.Month + 9.0) / 12.0))) +
            (int)((275.0 * dateTime.Month) / 9.0) +
            dateTime.Day - 730530.5;

        double julianCenturies = julianDate / 36525.0;

        // Sidereal Time  
        double siderealTimeHours = 6.6974 + 2400.0013 * julianCenturies;

        double siderealTimeUT = siderealTimeHours +
            (366.2422 / 365.2422) * (double)dateTime.TimeOfDay.TotalHours;

        double siderealTime = siderealTimeUT * 15 + longitude;

        // Refine to number of days (fractional) to specific time.  
        julianDate += (double)dateTime.TimeOfDay.TotalHours / 24.0;
        julianCenturies = julianDate / 36525.0;

        // Solar Coordinates  
        double meanLongitude = CorrectAngle(Deg2Rad *
            (280.466 + 36000.77 * julianCenturies));

        double meanAnomaly = CorrectAngle(Deg2Rad *
            (357.529 + 35999.05 * julianCenturies));

        double equationOfCenter = Deg2Rad * ((1.915 - 0.005 * julianCenturies) *
            Math.Sin(meanAnomaly) + 0.02 * Math.Sin(2 * meanAnomaly));

        double elipticalLongitude =
            CorrectAngle(meanLongitude + equationOfCenter);

        double obliquity = (23.439 - 0.013 * julianCenturies) * Deg2Rad;

        // Right Ascension  
        double rightAscension = Math.Atan2(
            Math.Cos(obliquity) * Math.Sin(elipticalLongitude),
            Math.Cos(elipticalLongitude));

        double declination = Math.Asin(
            Math.Sin(rightAscension) * Math.Sin(obliquity));

        // Horizontal Coordinates  
        double hourAngle = CorrectAngle(siderealTime * Deg2Rad) - rightAscension;

        if (hourAngle > Math.PI)
        {
            hourAngle -= 2 * Math.PI;
        }

        double altitude = Math.Asin(Math.Sin(latitude * Deg2Rad) *
            Math.Sin(declination) + Math.Cos(latitude * Deg2Rad) *
            Math.Cos(declination) * Math.Cos(hourAngle));

        // Nominator and denominator for calculating Azimuth  
        // angle. Needed to test which quadrant the angle is in.  
        double aziNom = -Math.Sin(hourAngle);
        double aziDenom =
            Math.Tan(declination) * Math.Cos(latitude * Deg2Rad) -
            Math.Sin(latitude * Deg2Rad) * Math.Cos(hourAngle);

        double azimuth = Math.Atan(aziNom / aziDenom);

        if (aziDenom < 0) // In 2nd or 3rd quadrant  
        {
            azimuth += Math.PI;
        }
        else if (aziNom < 0) // In 4th quadrant  
        {
            azimuth += 2 * Math.PI;
        }

        // Altitude  
        // Console.WriteLine("Altitude: " + altitude * Rad2Deg);  

        // Azimut  
        //Console.WriteLine("Azimuth: " + azimuth * Rad2Deg);  

        return new Position { Altitude = (float)(altitude * Rad2Deg), Azimuth = (float)(azimuth * Rad2Deg) };
    }

    /*! 
    * \brief Corrects an angle. 
    * 
    * \param angleInRadians An angle expressed in radians. 
    * \return An angle in the range 0 to 2*PI. 
    */
    private static double CorrectAngle(double angleInRadians)
    {
        if (angleInRadians < 0)
        {
            return 2 * Math.PI - (Math.Abs(angleInRadians) % (2 * Math.PI));
        }
        else if (angleInRadians > 2 * Math.PI)
        {
            return angleInRadians % (2 * Math.PI);
        }
        else
        {
            return angleInRadians;
        }
    }
}

