using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class ShadowMap : MonoBehaviour
{
    public int resolution = 512;
    public MeshRenderer planeRenderer;
    private Texture shadowMapTexture;
    [HideInInspector] private RawImage shadowMapImage;

    void Start()
    {
        // Create a new texture to hold the shadow map
        shadowMapTexture = new Texture2D(resolution, resolution, TextureFormat.RGBA32, false);

        // Set the shadow map texture to the RawImage component
        shadowMapImage = GetComponent<RawImage>();
        shadowMapImage.texture = shadowMapTexture;

        // Disable the plane renderer to prevent it from casting shadows on itself
        planeRenderer.enabled = false;
    }
    void LateUpdate()
    {
        // Calculate the illumination at each point on the plane
        CalculateIllumination();
    }

    void CalculateIllumination()
    {
        // Get the bounds of the plane mesh
        Bounds bounds = planeRenderer.bounds;

        // Loop through each pixel in the shadow map texture
        for (int y = 0; y < resolution; y++)
        {
            for (int x = 0; x < resolution; x++)
            {
                // Convert the pixel coordinates to a point on the plane mesh
                Vector3 point = new Vector3(
                    bounds.min.x + (bounds.max.x - bounds.min.x) * x / (resolution - 1),
                    0f,
                    bounds.min.z + (bounds.max.z - bounds.min.z) * y / (resolution - 1));

                // Get the color of the plane material at the current point
                shadowMapTexture = planeRenderer.material.GetTexture(0); //  "_ShadowMapTexture");
                Debug.Log(shadowMapTexture?.name);

                // Convert the color to HSV space
                //Color.RGBToHSV(shadowtexture, out float hue, out float saturation, out float brightness);

                // Use the brightness value as the illumination at the current point
                //float illumination = brightness;

                // Set the pixel color in the shadow map texture based on the illumination value
                //shadowMapTexture.SetPixel(x, y, new Color(illumination, illumination, illumination));
            }
        }
    }
}
