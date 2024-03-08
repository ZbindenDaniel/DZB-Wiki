using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class UI_ShadowMap : MonoBehaviour
{
    [SerializeField] private SunMovement sun;


    RawImage image;

    // Start is called before the first frame update
    void Start()
    {
        image = GetComponent<RawImage>();

    }

    // Update is called once per frame
    void Update()
    {
        if (sun?.shadowMap != null)
            image.texture = sun.shadowMap;
    }
}
