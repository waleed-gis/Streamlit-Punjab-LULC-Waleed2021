import streamlit as st
import ee
import geemap.foliumap as geemap

#ee.Authenticate()
#ee.Initialize()


def app():
    st.title("Punjab-LST (1990-2020")

    st.markdown(
        """
    # Under PROGRESS....

    """
    )

#    m = leafmap.Map(locate_control=True)
#    m.add_basemap("ROADMAP")
#    m.to_streamlit(height=700)



    # defining auth token for Geemap form system
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
    # Create an interactive map
    Map = geemap.Map(plugin_Draw=True, Draw_export=False)
    # Add a basemap
    Map.add_basemap("TERRAIN")

    pu1990 = ee.Image('users/WaleedGIS/PU1990')
    vis_lulc = {
        'min': 1,
        'max': 6,
        'palette': ['D44526', '1F7531', 'CFA844', '17DA08', 'A75C74', '3445AB']
    }
    Map.set_center(72.1491, 30.6411, 6.8)

    legend_dict = {
        'Builtup': 'D44526',
        'Forest': '1F7531',
        'Barren': 'CFA844',
        'Agriculture':  '17DA08',
        'Rangeland': 'A75C74',
        'Water': '3445AB'

    }

    Map.addLayer(pu1990, vis_lulc, 'LULC1990', True)
    Map.add_legend(legend_title='LULC Type', legend_dict=legend_dict)
    Map.to_streamlit()