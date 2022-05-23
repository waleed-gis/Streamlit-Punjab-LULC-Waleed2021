import streamlit as st
import ee
import geemap.foliumap as geemap

def app():
    st.title("Punjab-LULC (1990-2020)")

    st.markdown(
        """
    
    ## App Under Progress... @Mirzawaleed197@gmail.com
    ### Please wait for the Map to load...
    """
    )



    def ee_initialize(token_name="EARTHENGINE_TOKEN"):
        """Authenticates Earth Engine and initialize an Earth Engine session"""
        if ee.data._credentials is None:
            try:
                ee_token = os.environ.get(token_name)
                if ee_token is not None:
                    credential_file_path = os.path.expanduser("~/.config/earthengine/")
                    if not os.path.exists(credential_file_path):
                        credential = '{"refresh_token":"%s"}' % ee_token
                        os.makedirs(credential_file_path, exist_ok=True)
                        with open(credential_file_path + "credentials", "w") as file:
                            file.write(credential)
                elif in_colab_shell():
                    if credentials_in_drive() and (not credentials_in_colab()):
                        copy_credentials_to_colab()
                    elif not credentials_in_colab:
                        ee.Authenticate()
                        if is_drive_mounted() and (not credentials_in_drive()):
                            copy_credentials_to_drive()
                    else:
                        if is_drive_mounted():
                            copy_credentials_to_drive()

                ee.Initialize()
            except Exception:
                ee.Authenticate()
                ee.Initialize()


    geemap.ee_initialize()



    vis_lulc = {
        'min': 1,
        'max': 6,
        'palette': ['D44526', '1F7531', 'CFA844', '17DA08', 'A75C74', '3445AB']
    }

    legend_dict = {
        'Builtup': 'D44526',
        'Forest': '1F7531',
        'Barren': 'CFA844',
        'Agriculture':  '17DA08',
        'Rangeland': 'A75C74',
        'Water': '3445AB'

    }
    # adding layers
    pu1990 = ee.Image('users/WaleedGIS/PU1990')
    pu2000 = ee.Image('users/WaleedGIS/PU2000')
    pu2010 = ee.Image('users/WaleedGIS/PU2010')
    pu2020 = ee.Image('users/WaleedGIS/PU2020')

    # Create an interactive map
    Map = geemap.Map()
    # Add a basemap
    Map.add_basemap("HYBRID")
    Map.set_center(72.1491, 30.6411, 6.8)

   
    Map.addLayer(pu1990, vis_lulc, '1990')
    Map.addLayer(pu2000, vis_lulc, '2000')
    Map.addLayer(pu2010, vis_lulc, '2010')
    Map.addLayer(pu2020, vis_lulc, '2020')
    Map.add_legend(legend_title='LULC Type', legend_dict=legend_dict)
    Map.addLayerControl()
    Map.to_streamlit()
    #streamlit run streamlit_app.py