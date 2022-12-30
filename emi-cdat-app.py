import pickle
from pathlib import Path

import streamlit as st


import streamlit_authenticator as stauth

page_icon = "logo4.jpg"

st.set_page_config(
    page_title="Main Page",
    page_icon=page_icon,
    layout="wide"  # wide, centered
    )

# --- USER AUTHENTICATION ---
names = ["Yonas Mersha", "Asaminew Teshome", "Teferi Demissie", "Melesse Lemma", "Bezuneh Sego"]
usernames = ["yonas", "asaminew", "teferi", "melesse", "bezuneh" ]

# load hashed passwords
file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("rb") as file:
    hashed_passwords = pickle.load(file)

authenticator = stauth.Authenticate(names, usernames, hashed_passwords,
    "sales_dashboard", "abcdef", cookie_expiry_days=1)

name, authentication_status, username = authenticator.login("Login", "main")

if authentication_status == False:
    st.error("Username/password is incorrect")

if authentication_status == None:
    st.warning("Please enter your username and password")

if authentication_status:

    def intro():
        import streamlit as st
        from PIL import Image


        st.sidebar.success("Select a page")


        display = Image.open('logo41.jpg')

        authenticator.logout("Logout", "sidebar")
        st.sidebar.title(f"Welcome!, {name}")


        col1, col2= st.columns((3,7))
        col1.image(display, width = 200)
        col2.title("Ethiopian Meteorological Institute Climate Data Analysis Tool (EMI-CDAT)")
        st.markdown(
            """
            ---
            """
            )
        st.markdown(
                """
                The **Ethiopian Meteorological Institute Climate Data Analysis Tool (EMI-CDAT)** web application is designed to automate the data work flow at the Meteorological Data and Climatology Directorate and to generate charts, graphs, maps, and tabular outputs, as well as intermediate results required for the production of climate bulletins. 
                
                **EMI-CDAT** is build & deploy using the [Streamlit](https://docs.streamlit.io/) application development tool. The [Altair](https://altair-viz.github.io/index.html), [Bokeh](https://bokeh.org/), [Holoviews](https://holoviews.org/), [Plotly  Graphing Libraries](https://plotly.com/graphing-libraries/), [SciPy](https://scipy.org/), [NCAR PyNGL](https://www.pyngl.ucar.edu/index.shtml), & [PyNIO](https://www.pyngl.ucar.edu/index.shtml) visualizations packages are used to improve the statistical visualization and mapping capabilities of the App.
                """
                )
        st.markdown(
                    """
                    ---
                    EMI-CDAT App features includes:
                    - Reading input data in tabular formats such as Microsoft Excel spreadsheet (.xlsx) & comma separate value (.csv) & covert it to a Data-frame.
                    - The input data includes daily rainfall, maximum & minimum temperature.
                    - Summary report on the missing data
                    - Transform the data-frame to netCDF file format.
                    - Generate basic summary & indices in a tabular formats.
                    - Produce intermediate results & time series plots.
                    - Generates maps required for monthly, seasonal (i.e., Bega, Belg, Kiremt), & annual climate bulletins.
                    """
                    )
        st.markdown('### Our Partners')
        display1 = Image.open('AICCRA.png')
        display2 = Image.open('CGIAT.png')
        display3 = Image.open('CCAFS.png')
        
        col1, col2, col3 = st.columns(3)
        
        col1, col2, col3 = st.columns(3)
        col1.image(display1, width = 350)
        # col2.image(display2, width = 200)
        # col3.image(display3, width = 200)
        
        st.markdown('Copyright @2022 EMI-CDAT')
        st.markdown(
                        """
                        ---
                        """
                        )







        


        
    def data_reading_module():
        import streamlit as st 
        import pandas as pd
        import numpy as np
        import openpyxl
        import matplotlib.pyplot as plt
        import seaborn as sns
        from bokeh.plotting import figure, show
        from bokeh.io import output_notebook
        from bokeh.tile_providers import STAMEN_TONER
        from bokeh.models import ColumnDataSource
        from bokeh.palettes import Spectral11
        from bokeh.transform import factor_cmap
        from bokeh.tile_providers import get_provider, WIKIMEDIA, CARTODBPOSITRON, STAMEN_TERRAIN, STAMEN_TONER, ESRI_IMAGERY, OSM
        import holoviews as hv
        import scipy
        import plotly.figure_factory as ff
        import plotly.express as px


        authenticator.logout("Logout", "sidebar")
        st.sidebar.title(f"Welcome!, {name}")





    




        st.markdown(f'# {list(page_names_to_funcs.keys())[1]}')

        st.markdown(
            """
            ---
            """
            )


        # st.header("Setting Working Directory")

        # root = tk.Tk()
        # root.withdraw()
        
        # # Make folder picker dialog appear on top of other windows
        # root.wm_attributes('-topmost', 1)
        
        # # Folder picker button
        # st.title('Folder Picker')
        # st.write('Please select a folder:')
        # clicked = st.button('Folder Picker', key="11")
        # if clicked:
        #     dirname = st.text_input('Selected folder:', filedialog.askdirectory(master=root))

        # st.markdown(
        #     """
        #     ---
        #     """
        #     )

        st.header("Setting the Analysis Month and Year")

        col1, col2 = st.columns(2)

        with col1:
            month = st.selectbox('Choose a month',
            ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December" ), key="12")
            st.write('You selected:', month)

        with col2:
            year = st.selectbox('Choose a year', (2020, 2021, 2022, 2023, 2024, 2025), key="13")
            st.write('You selected:', year)

        st.markdown(
                        """
                        ---
                        """
                        )
        

        st.header("Rainfall")

        st.write('Daily Rainfall of', month, year)


        global  rainfall_daily
        rf_daily_mon = st.file_uploader("Please upload data in CSV or Excel file formats", type={"csv", "xlsx", "xls"}, key="14")
        if rf_daily_mon is not None:
            print(rf_daily_mon)
            print("Not correct file")
            try:
                daily_rf_x_month = pd.read_csv(rf_daily_mon)
            except Exception as e:
                print(e)
                daily_rf_x_month = pd.read_excel(rf_daily_mon)
                
                
            if  st.button("Load the data", key="15"):
                daily_rf_x_month
                st.success("Data Displayed!")
                
                
            if 'rainfall_daily' not in st.session_state:
                st.session_state['rainfall_daily'] = daily_rf_x_month

        year1=year -1

        st.write("Daily Rainfall of",  month, year1)

        global  daily_rf_pre_month
        uploaded_file = st.file_uploader("Please upload data in CSV or Excel file formats", type={"csv", "xlsx",  "xls"},  key="16")
        if uploaded_file is not None:
            print(uploaded_file)
            print("Not correct file")
            try:
                daily_rf_pre_month = pd.read_csv(uploaded_file)
            except Exception as e:
                print(e)
                daily_rf_pre_month = pd.read_excel(uploaded_file)
                
            if  st.button("Load the data", key="17"):
                daily_rf_pre_month
                st.success("Data Displayed!")



        st.write('Climatology of', month, 'Rainfall (30yrs)')

        global  clim_rf
        uploaded_file = st.file_uploader("Please upload data in CSV or Excel file formats", type={"csv", "xlsx",  "xls"}, key="18")
        if uploaded_file is not None:
            print(uploaded_file)
            print("Not correct file")
            try:
                clim_rf = pd.read_csv(uploaded_file)
            except Exception as e:
                print(e)
                clim_rf = pd.read_excel(uploaded_file)
                
            if  st.button('Load the data', key="19"):
                clim_rf
                st.success("Data Displayed!")




        st.markdown(
            """
            ---
            """
            )

        st.header("Maximum Temperature")

        st.write('Daily Maximum Temperature of', month, year)


        global  daily_tx_month
        uploaded_file = st.file_uploader("Please upload data in CSV or Excel file formats", type={"csv", "xlsx", "xls"}, key="20")
        if uploaded_file is not None:
            print(uploaded_file)
            print("Not correct file")
            try:
                daily_tx_month = pd.read_csv(uploaded_file)
            except Exception as e:
                print(e)
                daily_tx_month = pd.read_excel(uploaded_file)
                
            if  st.button("Load the data", key="21"):
                daily_tx_month
                st.success("Data Displayed!")
                
                if 'maximum_temperature_daily' not in st.session_state:
                    st.session_state['maximum_temperature_daily'] = daily_tx_month



        st.write("Daily Maximum Temperature of",  month, year1)

        global  daily_tx_pre_month
        uploaded_file = st.file_uploader("Please upload data in CSV or Excel file formats", type={"csv", "xlsx",  "xls"},  key="22")
        if uploaded_file is not None:
            print(uploaded_file)
            print("Not correct file")
            try:
                daily_tx_pre_month = pd.read_csv(uploaded_file)
            except Exception as e:
                print(e)
                daily_tx_pre_month = pd.read_excel(uploaded_file)
                
            if  st.button("Load the data", key="23"):
                daily_tx_pre_month
                st.success("Data Displayed!")


        st.write('Climatology of', month, 'Maximum Temperature (30yrs)')

        global  clim_tx
        uploaded_file = st.file_uploader("Please upload data in CSV or Excel file formats", type={"csv", "xlsx",  "xls"}, key="24")
        if uploaded_file is not None:
            print(uploaded_file)
            print("Not correct file")
            try:
                clim_tx = pd.read_csv(uploaded_file)
            except Exception as e:
                print(e)
                clim_tx = pd.read_excel(uploaded_file)
                
            if  st.button('Load the data', key="25"):
                clim_tx
                st.success("Data Displayed!")



        st.markdown(
            """
            ---
            """
            )


        st.header("Minimum Temperature")

        st.write('Daily Minimum Temperature of', month, year)


        global  daily_tm_month
        uploaded_file = st.file_uploader("Please upload data in CSV or Excel file formats", type={"csv", "xlsx", "xls"}, key="26")
        if uploaded_file is not None:
            print(uploaded_file)
            print("Not correct file")
            try:
                daily_tm_month = pd.read_csv(uploaded_file)
            except Exception as e:
                print(e)
                daily_tm_month = pd.read_excel(uploaded_file)
                
            if  st.button("Load the data", key="27"):
                daily_tm_month
                st.success("Data Displayed!")
                
                if 'minimum_temperature_daily' not in st.session_state:
                    st.session_state['minimum_temperature_daily'] = daily_tm_month


        
        st.write("Daily Minimum Temperature of",  month, year1)

        global  daily_tm_pre_month
        uploaded_file = st.file_uploader("Please upload data in CSV or Excel file formats", type={"csv", "xlsx",  "xls"},  key="28")
        if uploaded_file is not None:
            print(uploaded_file)
            print("Not correct file")
            try:
                daily_tm_pre_month = pd.read_csv(uploaded_file)
            except Exception as e:
                print(e)
                daily_tm_pre_month = pd.read_excel(uploaded_file)
                
            if  st.button("Load the data", key="29"):
                daily_tm_pre_month
                st.success("Data Displayed!")

        st.write('Climatology of', month, 'Minimum Temperature (30yrs)')

        global  clim_tm
        uploaded_file = st.file_uploader("Please upload data in CSV or Excel file formats", type={"csv", "xlsx",  "xls"}, key="30")
        if uploaded_file is not None:
            print(uploaded_file)
            print("Not correct file")
            try:
                clim_tm = pd.read_csv(uploaded_file)
            except Exception as e:
                print(e)
                clim_tm = pd.read_excel(uploaded_file)
                
            if  st.button('Load the data', key="31"):
                clim_tm
                st.success("Data Displayed!")


        st.markdown(
            """
            ---
            """
            )

        st.header("Summary of Missing Data")
        #chart_data1 = pd.DataFrame(
        #np.random.randn(10, 3),
        #columns=['a', 'b', 'c'])

        # chart_data2 = pd.DataFrame(
        # np.random.randn(10, 3),
        # columns=['a', 'b', 'c'])


        # chart_data3 = pd.DataFrame(
        # np.random.randn(10, 3),
        # columns=['a', 'b', 'c'])

        # st.write(chart_data1)
        # 






        


        # st.write(chart_data2)
        # st.write(chart_data3)

        # daily_rf_x_month

        st.markdown(
            """
            ---
            """
            )


        st.subheader("Total Missing Data Count")

        col1, col2, col3 = st.columns(3)
        
        with col1:
                st.write('Rainfall')
                if st.checkbox('Count missing data', key="32"):
                    if 'rainfall_daily' not in st.session_state:
                        st.text('Please Load Rainfall Data 😔')
                    else:
                        rainfall_daily = st.session_state['rainfall_daily']
                        missing_data1 = rainfall_daily.iloc[:, 9:40].isnull().sum().sum()
                        st.write('Rainfall missing data count in', month, 'is', missing_data1)
                        missing_data1 = rainfall_daily.iloc[:, 9:40].isnull().sum().sum()
                        rf_count = rainfall_daily.iloc[:, 9:40].size
                        per_miss_rf = (missing_data1/rf_count)*100
                        st.write('Percentage of missing values is:', round(per_miss_rf, 2), '%')
                        
                        per_miss_rf_ideal = 3
                        if per_miss_rf > per_miss_rf_ideal:
                            st.warning('Too many missing data points in the dataset, it is recommended to stop further analysis!')
                        else:
                            st.success('The dataset has no or fewer missing data points, it is recommended to continue the analysis!')

        with col2:
            st.write('Maximum Temperature')
            if st.checkbox('Count missing data', key="33"):
                if 'maximum_temperature_daily' not in st.session_state:
                    st.text('Please Load Maximum Temperature Data 😔')
                else:
                    maximum_temperature_daily = st.session_state['maximum_temperature_daily']
                    missing_data2 = maximum_temperature_daily.iloc[:, 9:40].isnull().sum().sum()
                    st.write('Maximum temperature missing data count in', month, 'is', missing_data2)
                    tx_count = maximum_temperature_daily.iloc[:, 9:40].size
                    per_miss_tx = (missing_data2/tx_count)*100
                    st.write('Percentage of missing values is:', round(per_miss_tx, 2), '%')
                    
                    per_miss_tx_ideal = 3
                    if per_miss_tx > per_miss_tx_ideal:
                        st.warning('Too many missing data points in the dataset, it is recommended to stop further analysis!')
                    else:
                        st.success('The dataset has no or fewer missing data points, it is recommended to continue the analysis!')

        with col3:
            st.write('Minimum Temperature')
            if st.checkbox('Count missing data', key="34"):
                if 'minimum_temperature_daily' not in st.session_state:
                    st.text('Please Load Minimum Temperature Data 😔')
                else:
                    minimum_temperature_daily = st.session_state['minimum_temperature_daily']
                    missing_data3 = minimum_temperature_daily.iloc[:, 9:40].isnull().sum().sum()
                    st.write('Minimum temperature missing data count in', month, 'is', missing_data3)
                    tm_count = minimum_temperature_daily.iloc[:, 9:40].size
                    per_miss_tm = (missing_data3/tm_count)*100
                    st.write('Percentage of missing values is:', round(per_miss_tm, 2), '%')

                    per_miss_tm_ideal = 3
                    if per_miss_tm > per_miss_tm_ideal:
                        st.warning('Too many missing data points in the dataset, it is recommended to stop further analysis!')
                    else:
                        st.success('The dataset has no or fewer missing data points, it is recommended to continue the analysis!')

        st.markdown(
            """
            ---
            """
            )

        st.subheader('Total Number of Missing Data  at each Day: Tabular Report')


        col1, col2, col3 = st.columns(3)
        with col1:
            st.write('Rainfall')
            if st.checkbox('Total number of missing data', key="35"):
                if 'rainfall_daily' not in st.session_state:
                    st.text('Please Load Rainfall Data 😔')
                else:
                    rainfall_daily = st.session_state['rainfall_daily']
                    missing_data_col1_rf = rainfall_daily.iloc[:, 9:40].isnull().sum()
                    missing_data_col1_rf = pd.DataFrame(missing_data_col1_rf)
                    names_rf1 = missing_data_col1_rf.columns.tolist()
                    names_rf1[names_rf1.index(0)] = 'Missing_Data_Count'
                    missing_data_col1_rf.columns = names_rf1
                    missing_data_col1_rf['Date'] = range(1, len(missing_data_col1_rf) + 1)
                    missing_data_date_rf = missing_data_col1_rf[["Date", "Missing_Data_Count"]]
                    missing_data_date_rf
                    
                    if 'missing_data_date_rf' not in st.session_state:
                        st.session_state['missing_data_date_rf'] = missing_data_date_rf
                                        
                
                    st.download_button('Download data as CSV', 
                    missing_data_date_rf.to_csv(),  
                    file_name='missing_data_by_date.csv', 
                    mime='text/csv', key="36")
                    
                    
            
        
        
        with col2:
            st.write('Maximum Temperature')
            if st.checkbox('Total number of missing data', key="37"):
                if 'maximum_temperature_daily' not in st.session_state:
                    st.text('Please Load Maximum Temperature Data 😔')
                else:
                    maximum_temperature_daily = st.session_state['maximum_temperature_daily']
                    missing_data_col1_tx = maximum_temperature_daily.iloc[:, 9:40].isnull().sum()
                    missing_data_col1_tx = pd.DataFrame(missing_data_col1_tx)
                    names_rf2 = missing_data_col1_tx.columns.tolist()
                    names_rf2[names_rf2.index(0)] = 'Missing_Data_Count'
                    missing_data_col1_tx.columns = names_rf2
                    missing_data_col1_tx['Date'] = range(1, len(missing_data_col1_tx) + 1)
                    missing_data_date_tx = missing_data_col1_tx[["Date", "Missing_Data_Count"]]


                    missing_data_date_tx
                    
                    if 'missing_data_date_tx' not in st.session_state:
                        st.session_state['missing_data_date_tx'] = missing_data_date_tx
                                        
                
                    st.download_button('Download data as CSV', 
                    missing_data_date_tx.to_csv(),  
                    file_name='missing_data_by_date.csv', 
                    mime='text/csv', key="38")

        with col3:
            st.write('Minimum Temperature')
            if st.checkbox('Total number of missing data', key="39"):
                if 'minimum_temperature_daily' not in st.session_state:
                    st.text('Please Load Maximum Temperature Data 😔')
                else:
                    minimum_temperature_daily = st.session_state['minimum_temperature_daily']
                    missing_data_col1_tm = minimum_temperature_daily.iloc[:, 9:40].isnull().sum()
                    missing_data_col1_tm = pd.DataFrame(missing_data_col1_tm)
                    names_rf3 = missing_data_col1_tm.columns.tolist()
                    names_rf3[names_rf3.index(0)] = 'Missing_Data_Count'
                    missing_data_col1_tm.columns = names_rf3
                    missing_data_col1_tm['Date'] = range(1, len(missing_data_col1_tm) + 1)
                    missing_data_date_tm = missing_data_col1_tm[["Date", "Missing_Data_Count"]]

                    missing_data_date_tm
                    
                    if 'missing_data_date_tm' not in st.session_state:
                        st.session_state['missing_data_date_tm'] = missing_data_date_tm
                        
                        
                    st.download_button('Download data as CSV', 
                    missing_data_date_tm.to_csv(),  
                    file_name='missing_data_by_date.csv', 
                    mime='text/csv', key="40")
                    

        st.markdown(
            """
            ---
            """
            )


        st.subheader('Total Number of Missing Data  at each Day: Graphical Report')
        
        miss_data_gr1 = st.selectbox('Choose a variable',
        ("None", "Rainfall", "Maximum Temperature ", "Minimum Temperature"))
        st.write('You selected:', miss_data_gr1)
        
        if 'Rainfall' in miss_data_gr1: 
            if 'missing_data_date_rf' not in st.session_state:
                st.text('Please Load Rainfall Data 😔')
            else:
                missing_data_date_rf = st.session_state['missing_data_date_rf']
                x1 = missing_data_date_rf['Date']
                y1 = missing_data_date_rf['Missing_Data_Count']
                p1 = figure(height=350, toolbar_location='right')
                p1.vbar(x=x1, top=y1, width=0.8)
                p1.xgrid.grid_line_color = None
                p1.y_range.start = 0
                p1.x_range.start = 0
                p1.title.text = "Missing Data Counts"
                p1.title.text_font_size = "20px"
                p1.title.align = "center"
                p1.xaxis.axis_label = 'Days'
                p1.yaxis.axis_label = 'Missing data'
                p1.plot_height=400
                p1.plot_width=800
                st.bokeh_chart(p1) 


        if 'Maximum Temperature' in miss_data_gr1: 
            if 'missing_data_date_tx' not in st.session_state:
                st.text('Please Load Maximum Temperature Data 😔')
            else:
                x2 = missing_data_date_tx['Date']
                y2 = missing_data_date_tx['Missing_Data_Count']
                p2 = figure(height=350, toolbar_location='right')
                p2.vbar(x=x2, top=y2, width=0.8)
                p2.xgrid.grid_line_color = None
                p2.y_range.start = 0
                p2.x_range.start = 0
                p2.title.text = "Missing Data Counts"
                p2.title.text_font_size = "20px"
                p2.title.align = "center"
                p2.xaxis.axis_label = 'Days'
                p2.yaxis.axis_label = 'Missing data'
                p2.plot_height=400
                p2.plot_width=800
                st.bokeh_chart(p2) 


        if 'Minimum Temperature' in miss_data_gr1:
            if 'missing_data_date_tm' not in st.session_state:
                st.text('Please Load Minimum Temperature Data 😔')
            else:
                x3 = missing_data_date_tm['Date']
                y3 = missing_data_date_tm['Missing_Data_Count']
                p3 = figure(height=350, toolbar_location='right')
                p3.vbar(x=x3, top=y3, width=0.8)
                p3.xgrid.grid_line_color = None
                p3.y_range.start = 0
                p3.x_range.start = 0
                p3.title.text = "Missing Data Counts"
                p3.title.text_font_size = "20px"
                p3.title.align = "center"
                p3.xaxis.axis_label = 'Days'
                p3.yaxis.axis_label = 'Missing data'
                p3.plot_height=400
                p3.plot_width=800
                st.bokeh_chart(p3) 


        st.markdown(
            """
            ---
            """
            )


        st.subheader('Total Number of Missing Data by Station: Tabular Report')

        col1, col2, col3 = st.columns(3)

        with col1:
            st.write('Rainfall')
            if st.checkbox('Total number of missing data', key="41"):
                if 'rainfall_daily' not in st.session_state:
                    st.text('Please Load Rainfall Data 😔')
                else:
                    rainfall_daily = st.session_state['rainfall_daily']
                    missingdata_rf = rainfall_daily.iloc[:, 9:40].isnull().sum(axis=1)
                    missingdata_rf_df = pd.DataFrame(missingdata_rf)
                    names_rf = missingdata_rf_df.columns.tolist()
                    names_rf[names_rf.index(0)] = 'Missing_Data_Count'
                    missingdata_rf_df.columns = names_rf
                    sub_rf = rainfall_daily.iloc[:, 0:9]
                    sub_rf_df = pd.DataFrame(sub_rf)
                    rf_join = sub_rf_df.join(missingdata_rf_df)
                    rf_miss_st = rf_join[["Sname", "Missing_Data_Count"]]
                    
                    rf_miss_st
                    
                    if 'rf_miss_st' not in st.session_state:
                        st.session_state['rf_miss_st'] = rf_miss_st

                    st.download_button('Download data as CSV', 
                                       rf_miss_st.to_csv(),  
                                       file_name='missing_data_by_station.csv', 
                                       mime='text/csv', key="42")


        with col2:
            st.write('Maximum Temperature')
            if st.checkbox('Total number of missing data', key="43"):
                
                if 'maximum_temperature_daily' not in st.session_state:
                    st.text('Please Load Maximum Temperature Data 😔')
                else:
                    maximum_temperature_daily = st.session_state['maximum_temperature_daily']
                    missingdata_tmax = maximum_temperature_daily.iloc[:, 9:40].isnull().sum(axis=1)
                    missingdata_tmax_df = pd.DataFrame(missingdata_tmax)
                    names_tmax = missingdata_tmax_df.columns.tolist()
                    names_tmax[names_tmax.index(0)] = 'Missing_Data_Count'
                    missingdata_tmax_df.columns = names_tmax
                    sub_tmax = maximum_temperature_daily.iloc[:, 0:9]
                    sub_tmax_df = pd.DataFrame(sub_tmax)
                    tmax_join = sub_tmax_df.join(missingdata_tmax_df)
                    tmax_miss_st = tmax_join[["Sname", "Missing_Data_Count"]]
                    
                    tmax_miss_st
                    
                    if 'tmax_miss_st' not in st.session_state:
                        st.session_state['tmax_miss_st'] = tmax_miss_st
                        
                    st.download_button('Download data as CSV', 
                                       tmax_miss_st.to_csv(),  
                                       file_name='missing_data_by_station.csv', 
                                       mime='text/csv', key="44")


        with col3:
            st.write('Minimum Temperature')
            if st.checkbox('Total number of missing data', key="45"):
                if 'minimum_temperature_daily' not in st.session_state:
                    st.text('Please Load Maximum Temperature Data 😔')
                else:
                    minimum_temperature_daily = st.session_state['minimum_temperature_daily']
                    missingdata_tmin = minimum_temperature_daily.iloc[:, 9:40].isnull().sum(axis=1)
                    missingdata_tmin_df = pd.DataFrame(missingdata_tmin)
                    names_tmin = missingdata_tmin_df.columns.tolist()
                    names_tmin[names_tmin.index(0)] = 'Missing_Data_Count'
                    missingdata_tmin_df.columns = names_tmin
                    sub_tmin = minimum_temperature_daily.iloc[:, 0:9]
                    sub_tmin_df = pd.DataFrame(sub_tmin)
                    tmin_join = sub_tmin_df.join(missingdata_tmin_df)
                    tmin_miss_st = tmin_join[["Sname", "Missing_Data_Count"]]
                    
                    tmin_miss_st
                    
                    if 'tmin_miss_st' not in st.session_state:
                        st.session_state['tmin_miss_st'] = tmin_miss_st
                        
                    st.download_button('Download data as CSV', 
                                       tmin_miss_st.to_csv(),  
                                       file_name='missing_data_by_station.csv', 
                                       mime='text/csv', key="46")

        st.markdown(
            """
            ---
            """
            )


        st.subheader('Stations without Missing Data: Tabular Report')
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.write('Rainfall stations with less than three days of missing data')
            

            if st.checkbox('Rainfall', key="47"):
                if 'rf_miss_st' not in st.session_state:
                    st.text('Please Load  Rainfall Data 😔')
                else:
                    st.text('')
                    
                    rf_miss_st = st.session_state['rf_miss_st']
                    miss_rf3 = rf_miss_st[rf_miss_st['Missing_Data_Count'] < 3] 
                    st.write(miss_rf3)
                    
                    st.download_button('Download data as CSV', 
                                       miss_rf3.to_csv(),  
                                       file_name='stationless3_daymissing data.csv', 
                                       mime='text/csv', key="48")
                

                
        with col2:
            st.write('Maximum Temperature stations with less than five days of missing data')
            if st.checkbox('Maximum Temperature', key="49"):
                if 'tmax_miss_st' not in st.session_state:
                    st.text('Please Load Maximum Temperature Data 😔')
                else:
                    st.text('')
                    tmax_miss_st = st.session_state['tmax_miss_st']
                    miss_tx5 = tmax_miss_st[tmax_miss_st['Missing_Data_Count'] < 5] 
                    st.write(miss_tx5)
                    
                    st.download_button('Download data as CSV', 
                                       miss_tx5.to_csv(),  
                                       file_name='stationless5_daymissing data.csv', 
                                       mime='text/csv', key="50")


        with col3:
            st.write('Minimum Temperature stations with less than five days of missing data')
            if st.checkbox('Minimum Temperature', key="51"):
                if 'tmin_miss_st' not in st.session_state:
                    st.text('Please Load Minimum Temperature Data 😔')
                else:
                    st.text('')
                    tmin_miss_st = st.session_state['tmin_miss_st']
                    miss_tm5 = tmin_miss_st[tmin_miss_st['Missing_Data_Count'] < 5] 
                    st.write(miss_tm5)
                    
                    st.download_button('Download data as CSV', 
                                       miss_tm5.to_csv(),  
                                       file_name='stationless5_daymissing data.csv', 
                                       mime='text/csv', key="52")


        st.markdown(
            """
            ---
            """
            )

        st.subheader('Locations of Stations with No Missing Data')

            
        station_loc = st.selectbox('Choose a variable',
        ("None", "Rainfall", "Maximum Temperature ", "Minimum Temperature"), key="53")
        st.write('You selected:', station_loc)
    

        if 'Rainfall' in station_loc: 
            if 'rainfall_daily' not in st.session_state:
                st.text('Please Load Rainfall Data 😔')
            else:
                rainfall_daily = st.session_state['rainfall_daily']
                missingdata_rf = rainfall_daily.iloc[:, 9:40].isnull().sum(axis=1)
                missingdata_rf_df = pd.DataFrame(missingdata_rf)
                names_rf = missingdata_rf_df.columns.tolist()
                names_rf[names_rf.index(0)] = 'Missing_Data_Count'
                missingdata_rf_df.columns = names_rf
                sub_rf = rainfall_daily.iloc[:, 0:9]
                sub_rf_df = pd.DataFrame(sub_rf)
                rf_join = sub_rf_df.join(missingdata_rf_df)
                rf_miss_st = rf_join[["Sname", "Lat", "Lon", "Missing_Data_Count"]]
                
                miss_rf3 = rf_miss_st[rf_miss_st['Missing_Data_Count'] < 3] 
                fig2_rf = px.scatter_mapbox(miss_rf3, lat="Lat", lon="Lon", hover_name="Sname", hover_data=["Sname", "Missing_Data_Count"],
                                            color_discrete_sequence=["green"], zoom=5, height=500)
                color="Sname"
                fig2_rf.update_layout(mapbox_style="open-street-map")   # open-street-map
                fig2_rf.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
                st.plotly_chart(fig2_rf, use_container_width=True)


        if 'Maximum Temperature' in station_loc: 
            if 'maximum_temperature_daily' not in st.session_state:
                st.text('Please Load Maximum Temperature Data 😔')
            else:
                maximum_temperature_daily = st.session_state['maximum_temperature_daily']
                missingdata_tx = maximum_temperature_daily.iloc[:, 9:40].isnull().sum(axis=1)
                missingdata_tx_df = pd.DataFrame(missingdata_tx)
                names_tx = missingdata_tx_df.columns.tolist()
                names_tx[names_tx.index(0)] = 'Missing_Data_Count'
                missingdata_tx_df.columns = names_tx
                sub_tx = maximum_temperature_daily.iloc[:, 0:9]
                sub_tx_df = pd.DataFrame(sub_tx)
                tx_join = sub_tx_df.join(missingdata_tx_df)
                tx_miss_st = tx_join[["Sname", "Lat", "Lon", "Missing_Data_Count"]]
                
                miss_tx5 = tx_miss_st[tx_miss_st['Missing_Data_Count'] < 5] 
                
                fig2_tx = px.scatter_mapbox(miss_tx5, lat="Lat", lon="Lon", hover_name="Sname", hover_data=["Sname", "Missing_Data_Count"],
                                            color_discrete_sequence=["green"], zoom=5, height=500)
                color="Sname"
                fig2_tx.update_layout(mapbox_style="open-street-map")   # open-street-map
                fig2_tx.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
                st.plotly_chart(fig2_tx, use_container_width=True)
                

        if 'Minimum Temperature' in station_loc:
            if 'minimum_temperature_daily' not in st.session_state:
                st.text('Please Load Minimum Temperature Data 😔')
            else:
                minimum_temperature_daily = st.session_state['minimum_temperature_daily']
                missingdata_tm = minimum_temperature_daily.iloc[:, 9:40].isnull().sum(axis=1)
                missingdata_tm_df = pd.DataFrame(missingdata_tm)
                names_tm = missingdata_tm_df.columns.tolist()
                names_tm[names_tm.index(0)] = 'Missing_Data_Count'
                missingdata_tm_df.columns = names_tm
                sub_tm = minimum_temperature_daily.iloc[:, 0:9]
                sub_tm_df = pd.DataFrame(sub_tm)
                tm_join = sub_tm_df.join(missingdata_tm_df)
                tm_miss_st = tm_join[["Sname", "Lat", "Lon", "Missing_Data_Count"]]
                miss_tm5 = tm_miss_st[tm_miss_st['Missing_Data_Count'] < 5] 
                
                fig2_tm = px.scatter_mapbox(miss_tm5, lat="Lat", lon="Lon", hover_name="Sname", hover_data=["Sname", "Missing_Data_Count"],
                                            color_discrete_sequence=["green"], zoom=5, height=500)
                color="Sname"
                fig2_tm.update_layout(mapbox_style="open-street-map")   # open-street-map", "carto-positron", "carto-darkmatter", "stamen-terrain", "stamen-toner" or "stamen-watercolor" 
                fig2_tm.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
                
                st.plotly_chart(fig2_tm, use_container_width=True)
                


    def basic_summary():
        import streamlit as st
        st.markdown(f"# {list(page_names_to_funcs.keys())[2]}")
        
        import streamlit as st
        import pandas as pd
        import numpy as np
        import openpyxl
        import matplotlib.pyplot as plt
        import seaborn as sns
        from bokeh.plotting import figure, show
        from bokeh.io import output_notebook
        from bokeh.tile_providers import STAMEN_TONER
        from bokeh.models import ColumnDataSource
        from bokeh.palettes import Spectral11
        from bokeh.transform import factor_cmap
        from bokeh.tile_providers import get_provider, WIKIMEDIA, CARTODBPOSITRON, STAMEN_TERRAIN, STAMEN_TONER, ESRI_IMAGERY, OSM
        import holoviews as hv
        import scipy
        import plotly.figure_factory as ff
        import plotly.express as px


        authenticator.logout("Logout", "sidebar")
        st.sidebar.title(f"Welcome!, {name}")


        


        st.header("Daily  Data to Monthly Data")
        st.markdown("""
                    ---
                    """)

        st.subheader('Tabular and Graphical Reports')
        
        station_loc = st.selectbox('Choose a variable', ("None", "Rainfall", "Maximum Temperature ", "Minimum Temperature"), key =2)
        st.write('You selected:', station_loc, 'data')
        
        
        if 'rainfall_daily' not in st.session_state:
            st.subheader('Please load Rainfall data')
        else:
            st.text('')
        
        if 'Rainfall' in station_loc: 
            Rainfall_daily = st.session_state['rainfall_daily']
            Rainfall_daily['Missing Data']= Rainfall_daily.iloc[:,:].isnull().sum(axis=1)
            Rainfall_daily3 = Rainfall_daily.loc[Rainfall_daily['Missing Data'] < 3]
            Rainfall_daily3['Monthly Total Rainfall'] = Rainfall_daily3.iloc[:, 9:40].sum(axis=1)
            Rainfall_daily3['No'] = range(1, len(Rainfall_daily3) + 1)
            Rainfall_mon = Rainfall_daily3[["No","Sname", "Lat", "Lon", "Missing Data", "Monthly Total Rainfall"]]
            #Rainfall_mon1 = Rainfall_daily3[["No", "Sname", "Total Rainfall"]]
            #Rainfall_mon1     
            Rainfall_mon = round(Rainfall_mon, 3)
            Rainfall_mon
            
            if 'rf_mon' not in st.session_state:
                st.session_state['rf_mon'] = Rainfall_mon
                
                
            st.download_button('Download data as CSV', 
            Rainfall_mon.to_csv(),  
            file_name='daily_rfmon.csv', 
            mime='text/csv')
            
            st.write('Plot for Monthly Total Rainfall')
            mon_rf = px.scatter_mapbox(Rainfall_mon, lat="Lat", lon="Lon", hover_name="Sname", hover_data=["Sname", "Monthly Total Rainfall"],
            color_discrete_sequence=["green"], zoom=5, height=500)
            color="Sname"
            mon_rf.update_layout(mapbox_style="open-street-map")   # open-street-map
            mon_rf.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
            st.plotly_chart(mon_rf, use_container_width=True)
            
            if 'rf_mon' not in st.session_state:
                st.session_state['rf_mon'] = rf_mon
            
            
        if 'maximum_temperature_daily' not in st.session_state:
            st.subheader('Please load maximum temperature data')
        else:
            st.text('')   

        if 'Maximum Temperature' in station_loc: 
            maxtemp_daily = st.session_state['maximum_temperature_daily']
            maxtemp_daily['Missing Data']= maxtemp_daily.iloc[:,:].isnull().sum(axis=1)
            maxtemp_daily5 = maxtemp_daily.loc[maxtemp_daily['Missing Data'] < 5]
            maxtemp_daily5['Monthly Maximum Temperature'] = maxtemp_daily5.iloc[:, 9:40].mean(axis=1)
            maxtemp_daily5['No'] = range(1, len(maxtemp_daily5) + 1)
            maxtemp_mon = maxtemp_daily5[["No","Sname", "Lat", "Lon", "Missing Data", "Monthly Maximum Temperature"]]
            maxtemp_mon = round(maxtemp_mon, 3)
            maxtemp_mon
            if 'tmax_mon' not in st.session_state:
                st.session_state['tmax_mon'] = maxtemp_mon
            
            st.download_button('Download data as CSV', 
                               maxtemp_mon.to_csv(),  
                               file_name='daily_tmaxmon.csv', 
                               mime='text/csv')
            
            st.write('Plot for Monthly Maximum Temperature')
            mon_tmax = px.scatter_mapbox(maxtemp_mon, lat="Lat", lon="Lon", hover_name="Sname", hover_data=["Sname", "Monthly Maximum Temperature"],
            color_discrete_sequence=["green"], zoom=5, height=500)
            color="Sname"
            mon_tmax.update_layout(mapbox_style="open-street-map")   # open-street-map
            mon_tmax.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
            st.plotly_chart(mon_tmax, use_container_width=True)
            
            
        if 'minimum_temperature_daily' not in st.session_state:
            st.subheader('Please load minimum temperature data')
        else:
            st.text('') 
        
        if 'Minimum Temperature' in station_loc: 
            mintemp_daily = st.session_state['minimum_temperature_daily']
            mintemp_daily['Missing Data']= mintemp_daily.iloc[:,:].isnull().sum(axis=1)
            mintemp_daily5 = mintemp_daily.loc[mintemp_daily['Missing Data'] < 5]
            mintemp_daily5['Monthly Minimum Temperature'] = mintemp_daily5.iloc[:, 9:40].mean(axis=1)
            mintemp_daily5['No'] = range(1, len(mintemp_daily5) + 1)
            mintemp_mon =mintemp_daily5[["No","Sname", "Lat", "Lon", "Missing Data", "Monthly Minimum Temperature"]]
            mintemp_mon = round(mintemp_mon, 3)
            mintemp_mon

            st.download_button('Download data as CSV', 
            mintemp_mon.to_csv(),  
            file_name='daily_tminmon.csv', 
            mime='text/csv')
        
            if 'tmin_mon' not in st.session_state:
                st.session_state['tmin_mon'] = mintemp_mon


            st.write('Plot for Monthly Minimum Temperature')
            mon_tmin = px.scatter_mapbox(mintemp_mon, lat="Lat", lon="Lon", hover_name="Sname", hover_data=["Sname", "Monthly Minimum Temperature"],
            color_discrete_sequence=["green"], zoom=5, height=500)
            color="Sname"
            mon_tmin.update_layout(mapbox_style="open-street-map")   # open-street-map
            mon_tmin.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
            st.plotly_chart(mon_tmin, use_container_width=True)
            
            
        st.header('Monthly Mean Temperature')
        clicked = st.button("Calculate Monthly Mean Temperature")
        if clicked:
            tmax_mon = st.session_state['tmax_mon']
            tmin_mon = st.session_state['tmin_mon']
            import functools
            dfs = [tmax_mon[["No","Sname", "Lat", "Lon", "Missing Data", "Monthly Maximum Temperature"]], tmin_mon[["No","Sname", "Lat", "Lon", "Missing Data", "Monthly Minimum Temperature"]]]
            df_final = functools.reduce(lambda left, right: pd.merge(left,right,on='Sname'), dfs)
            df_final['Monthly Mean Temperature'] = df_final.loc[:, ["Monthly Maximum Temperature","Monthly Minimum Temperature"]].mean(axis=1)
            df_final['No'] = range(1, len(df_final) + 1)
            meantemp_mon =df_final[["No","Sname", "Lat_x", "Lon_x",  "Monthly Mean Temperature"]]
            meantemp_mon.rename(columns = {'Lat_x':'Lat', 'Lon_x':'Lon'}, inplace = True)
            meantemp_mon = round(meantemp_mon, 3)
            meantemp_mon
            if 'meantemp_mon' not in st.session_state:
                st.session_state['meantemp_mon'] = meantemp_mon
            
            st.download_button('Download data as CSV', 
                               meantemp_mon.to_csv(),  
                               file_name='daily_mon.csv', 
                               mime='text/csv')
                
            st.write('Plot for Monthly Mean Temperature')
            mon_tmean = px.scatter_mapbox(meantemp_mon, lat="Lat", lon="Lon", hover_name="Sname", hover_data=["Sname", "Monthly Mean Temperature"],
                                          color_discrete_sequence=["green"], zoom=5, height=500)
            color="Sname"
            mon_tmean.update_layout(mapbox_style="open-street-map")   # open-street-map
            mon_tmean.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
            st.plotly_chart(mon_tmean, use_container_width=True)
        
        
        st.markdown("""
        ---
        """)
        
        st.subheader('Monthly Summary Statistics')
        
        station_loc2 = st.selectbox('Choose a variable', ("None", "Rainfall", "Maximum Temperature", "Minimum Temperature", "Mean Temperature"), key ="mon_sum")
        st.write('You selected:', station_loc2, 'data')
        
        
        #  Monthly  Rainfall summary statistics

        
        
        if 'rf_mon' not in st.session_state:
            st.subheader('Please Load Rainfall Data')
        else:
            st.text('')
            
        if 'Rainfall' in station_loc2: 
            rf_mondf = st.session_state['rf_mon']
            rf_info_mon = rf_mondf['Monthly Total Rainfall'].describe(include='all') 
            rf_info_mon
            
            st.download_button('Download data as CSV', 
                               rf_info_mon.to_csv(),  
                               file_name='mon_sum_stat_RF.csv', 
                               mime='text/csv')
            
      
            

            
        #  Monthly Maximum Temperature summary statistics
        
        
        if 'tmax_mon' not in st.session_state:
            st.subheader('Please Load Monthly Maximum Temperature Data')
        else:
            st.text('')
            
        if 'Maximum Temperature' in station_loc2: 
            tmax_mondf = st.session_state['tmax_mon']
            tmax_info_mon = tmax_mondf['Monthly Maximum Temperature'].describe(include='all') 
            tmax_info_mon
            
            st.download_button('Download data as CSV', 
                               tmax_info_mon.to_csv(),  
                               file_name='mon_sum_stat_tmax.csv', 
                               mime='text/csv')
            
        
        #  Monthly  Minimum Temperature  summary statistics
            
               
        if 'tmin_mon' not in st.session_state:
            st.subheader('Please Load Monthly Minimum Temperature Data')
        else:
            st.text('')
            
        if 'Minimum Temperature' in station_loc2: 
            tmin_mondf = st.session_state['tmin_mon']
            tmin_info_mon = tmin_mondf['Monthly Minimum Temperature'].describe(include='all') 
            tmin_info_mon
            
            st.download_button('Download data as CSV', 
                               tmin_info_mon.to_csv(),  
                               file_name='mon_sum_stat_tmin.csv', 
                               mime='text/csv')
            
        #  Monthly  Mean Temperature  summary statistics
        
                   
        if 'meantemp_mon' not in st.session_state:
            st.subheader('Please Load Monthly Mean Temperature data')
        else:
            st.text('')
            
        if 'Mean Temperature' in station_loc2: 
            tmean_mondf = st.session_state['meantemp_mon']
            tmean_info_mon = tmean_mondf['Monthly Mean Temperature'].describe(include='all') 
            tmean_info_mon
            
            st.download_button('Download data as CSV', 
                               tmean_info_mon.to_csv(),  
                               file_name='mon_sum_stat_tmean.csv', 
                               mime='text/csv')
            

            
            
        
        
        
        
        
        st.header('Monthly  Data to Seasonal Data')
        st.markdown("""
                    ---
                    """)

        st.subheader('Rainfall')

        st.markdown('Bega (October to January)')
        st.markdown('Belg (February to May) ')
        st.markdown('Kiremt (June to September)')

        st.subheader('Maximum Temperature')

        st.markdown('Bega (October to January)')
        st.markdown('Belg (February to May) ')
        st.markdown('Kiremt (June to September)')

        st.subheader('Minimum Temperature')

        st.markdown('Bega (October to January)')
        st.markdown('Belg (February to May) ')
        st.markdown('Kiremt (June to September)')


        st.markdown( """
                    ---
                    """)

        st.header('Monthly  Data to Annual Data')
        st.markdown("""
                    ---
                    """)

        st.subheader('Rainfall')

        st.subheader('Maximum Temperature')

        st.subheader('Minimum Temperature')



        st.markdown( """
                    ---
                    """)


        st.header('Seasonal  Data to Annual Data')
        st.markdown("""
                    ---
                    """)

        st.subheader('Rainfall')


        st.subheader('Maximum Temperature')

        st.subheader('Minimum Temperature')



        st.markdown( """
                    ---
                    """)

            
            
    def intermediate_result():
        import streamlit as st
        import pandas as pd
        import numpy as np
        import plotly.figure_factory as ff
        import plotly.express as px
        st.markdown(f"# {list(page_names_to_funcs.keys())[3]}")
        
        authenticator.logout("Logout", "sidebar")
        st.sidebar.title(f"Welcome!, {name}")
        
        st.header('Variables that Exceed Certain Thresholds')
        
        # Rainfall
        # global df_rainfall_reports
        if 'rainfall_daily' not in st.session_state:
            st.text('Please Load Rainfall Data 😔')
        else:
            st.subheader('Rainfall')

            rf = st.slider('Select rainfall values:', 10, 300, 10, key="rainfall")
            st.write("You selected", rf, 'mm')
            st.write(f'Station(s) with equal or greater than {rf}mm of rainfall.')

            rainfall_daily = st.session_state['rainfall_daily']

            df_rainfall_stations = rainfall_daily.loc[:,['Sname']]  
            df_rainfall_dates = rainfall_daily.loc[:,'Val01':'Val31'].astype(float)
            df_rainfall_dates_filtered = df_rainfall_dates[(df_rainfall_dates[df_rainfall_dates.columns[:]]>=rf)]
            
            dict_rainfall_reports = {'Station Name' : [], 'Rain Fall (mm)' : [], 'Date' : [], }

            for index, row in df_rainfall_dates_filtered.iterrows():
                notna_rainfall_dates = [(date, rainfall) for date, rainfall in row.items() if rainfall.is_integer()]
                for date, rainfall in notna_rainfall_dates:  
                    dict_rainfall_reports['Station Name'].append(df_rainfall_stations['Sname'].loc[index])
                    dict_rainfall_reports['Rain Fall (mm)'].append(rainfall)
                    dict_rainfall_reports['Date'].append(date)
            
            df_rainfall_reports = pd.DataFrame(dict_rainfall_reports)
            df_rainfall_reports
            
           
            st.download_button('Download data as CSV', 
            df_rainfall_reports.to_csv(),  
            file_name='df_rainfall_reports.csv', 
            mime='text/csv')
            
            if 'df_rainfall_reports' not in st.session_state:
                st.session_state['df_rainfall_reports'] = df_rainfall_reports
            
        
        # Maximum Temperature
        if 'maximum_temperature_daily' not in st.session_state:
            st.text('Please Load Maximum Temperature Data 😔')
        else:
            st.subheader('Maximum Temperature')

            tmax = st.slider('Select temperature values:', 20, 60, 20, key="max_temp")
            st.write("You selected", tmax, '°C')
            st.write(f'Station(s) with equal or greater than {tmax}°C.')

            maximum_temperature_daily = st.session_state['maximum_temperature_daily']

            df_tmax_stations = maximum_temperature_daily.loc[:,['Sname']] 
            # df_tmax_dates    = maximum_temperature_daily.loc[:,'Val01':'Val31']
            df_tmax_dates    = maximum_temperature_daily.loc[:,'Val01':'Val31'].astype(float)            
            
            df_tmax_date_filtered = df_tmax_dates[(df_tmax_dates[df_tmax_dates.columns[:]] >=tmax)]
            dict_tmax_reports = {'Station Name' : [], 'Max Temp' : [], 'Date' : [], }
            for index, row in df_tmax_date_filtered.iterrows():
                notna_date_temp = [(date, temp) for date, temp in row.items() if temp.is_integer()]
                for date, temp in notna_date_temp:  
                    dict_tmax_reports['Station Name'].append(df_tmax_stations['Sname'].loc[index])
                    dict_tmax_reports['Max Temp'].append(temp)
                    dict_tmax_reports['Date'].append(date)
                    
                    
            df_tmax_reports = pd.DataFrame(dict_tmax_reports)
            df_tmax_reports
            
            st.download_button('Download data as CSV', 
                               df_tmax_reports.to_csv(), 
                               file_name='df_tmax_re',
                               mime='text/csv')
        
        # Minimum Temperature
        if 'minimum_temperature_daily' not in st.session_state:
            st.text('Please Load Minimum Temperature Data😔')
        else:
            st.subheader('Minimum Temperature')

            tmin = st.slider('Select temperature values:', 20, 60, 20, key="min_temp")
            st.write("You selected", tmin, '°C')
            st.write(f'Station(s) with equal or less than {tmin}°C.')

            minimum_temperature_daily = st.session_state['minimum_temperature_daily']

            df_tmin_stations = minimum_temperature_daily.loc[:,['Sname']]  
            df_tmin_dates = minimum_temperature_daily.loc[:,'Val01':'Val31'].astype(float)
            df_tmin_date_filtered = df_tmin_dates[(df_tmin_dates[df_tmin_dates.columns[:]] <=tmin)]
            
            dict_tmin_reports = {'Station Name' : [], 'Min Temp' : [], 'Date' : [], }

            for index, row in df_tmin_date_filtered.iterrows():
                notna_date_temp = [(date, temp) for date, temp in row.items() if temp.is_integer()]
                for date, temp in notna_date_temp:  
                    dict_tmin_reports['Station Name'].append(df_tmin_stations['Sname'].loc[index])
                    dict_tmin_reports['Min Temp'].append(temp)
                    dict_tmin_reports['Date'].append(date)
            
            df_tmin_reports = pd.DataFrame(dict_tmin_reports)
            df_tmin_reports
            
            st.download_button('Download data as CSV', 
            df_tmin_reports.to_csv(),  
            file_name='df_tmin_reports.csv', 
            mime='text/csv')
            
            
            if 'rainfall_daily' not in st.session_state:
                st.text('Please Load Rainfall Data😔')
            else:
                st.header('Number of Rainy Days')
            clicked = st.button("Calculate Number of Rainy Days")
            if clicked:
                rainfall_daily = st.session_state['rainfall_daily'] 
                df_rfst_name = rainfall_daily.loc[:,['Sname']]  
                df_rfst_lon = rainfall_daily.loc[:,['Lon']]  
                df_rfst_lat = rainfall_daily.loc[:,['Lat']]             
                df_rfst_dates = rainfall_daily.loc[:,'Val01':'Val31'].astype(float)
                No_rain_days = df_rfst_dates[df_rfst_dates >= 0.5].count(axis=1)
                No_rain_days = pd.DataFrame(No_rain_days)  
                
                dict_no_rainy_days_reports = {'Station Name' : [], 'Lon' : [], 'Lat' : [],'Rainy Day Count' : [], }  
                
                for index, row in No_rain_days.iterrows():
                     norain_date_rf = [(date, temp) for date, temp in row.items()]
                     for date, temp in norain_date_rf:  
                         dict_no_rainy_days_reports['Station Name'].append(df_rfst_name['Sname'].loc[index])
                         dict_no_rainy_days_reports['Lon'].append(df_rfst_lon['Lon'].loc[index])
                         dict_no_rainy_days_reports['Lat'].append(df_rfst_lat['Lat'].loc[index])
                         dict_no_rainy_days_reports['Rainy Day Count'].append(temp)
                    
                df_norf_reports = pd.DataFrame(dict_no_rainy_days_reports)
                df_norf_reports
            
            
                st.download_button('Download data as CSV', 
                df_norf_reports.to_csv(),  
                file_name='no_rainy_days.csv', 
                mime='text/csv')
                
                
                st.write('Plot for Number of Rainy Days')
                no_rain_mon = px.scatter_mapbox(df_norf_reports, lat="Lat", lon="Lon", hover_name="Station Name", hover_data=["Station Name", "Rainy Day Count"],
                                               color_discrete_sequence=["green"], zoom=5, height=500)
                color="Sname"
                no_rain_mon.update_layout(mapbox_style="open-street-map")   # open-street-map
                no_rain_mon.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
                st.plotly_chart(no_rain_mon, use_container_width=True)

   
            


            
            
            
            

            
            
            
        
        
        













    def time_series_plots():
        import streamlit as st
        st.markdown(f"# {list(page_names_to_funcs.keys())[4]}")





    def netCDF_convector():
        import streamlit as st
        st.markdown(f"# {list(page_names_to_funcs.keys())[5]}")
        
        import streamlit as st
        import numpy as np
        import pandas as pd
        import openpyxl
        import matplotlib.pyplot as plt
        import scipy
        from scipy.interpolate import interp2d, griddata
        import numpy.ma as ma
        from numpy.random import uniform, seed
        import pykrige.kriging_tools as kt
        from pykrige.ok import OrdinaryKriging
        from pykrige.uk import UniversalKriging
        import xarray as xr
        import hvplot.xarray
        import rioxarray
        from datetime import datetime
        
        import cartopy
        import cartopy.crs as ccrs
        import cartopy.feature as cfeature
        from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
        import cartopy.io.shapereader as shpreader
        import cartopy.mpl.geoaxes
        import cartopy.io.img_tiles as cimgt
        from mpl_toolkits.axes_grid1.inset_locator import inset_axes
        from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter 
        import salem
        import time
        import geoviews as gv
        import geoviews.feature as gf
        import holoviews as hv
        from bokeh.plotting import figure, show
        import plotly.figure_factory as ff
        import plotly.express as px


        
           
        
        st.subheader('Geospatial Mapping')
        
        
        col1, col2, col3 = st.columns([4, 4, 4 ])
        
        with col1:
            kgdata = st.selectbox('Select Monthly/Seasonal/Annual Data',
            ("Monthly Data", "Seasonal Data", "Annual Data"), key="kgdata")
            st.write('You selected:', kgdata)
            
            if kgdata == "Monthly Data":
                uploaded_file = st.file_uploader("Please upload data in CSV or Excel file formats", type={"csv", "xlsx",  "xls"},  key="16")
                if uploaded_file is not None:
                    print(uploaded_file)
                    print("Not correct file")
                    try:
                        month_kg = pd.read_csv(uploaded_file)
                    except Exception as e:
                        print(e)
                        month_kg = pd.read_excel(uploaded_file)
                
                    if  st.button("Load the data", key="month_kg"):
                        month_kg
                    st.success("Data Displayed!")
                    
            if "month_kg" not in st.session_state:
                st.session_state.month_kg = "month_kg"
        
        
        
        with col2:
            Inter_method = st.selectbox("Select Interpolation Method",
                                                ("Ordinary Kriging", "Universal Kriging"),  key="Inter_method")
            st.write('You selected:', Inter_method)
            

            
            
        with col3:
            variogram = st.selectbox("Select Variogram Models",
                                     ("linear", "power", "spherical", "gaussian", "exponential", "hole-effect"),  key="variogram")
            st.write('You selected:', variogram)
            
        
        st.subheader('Step 1: Perform the spatial interpolation') 

         
        if Inter_method == "Ordinary Kriging":
            
            clicked = st.button("Perform Interpolation")
            if clicked:                  
                grid_lon = np.arange(33, 48.1, 0.1, dtype='float64')
                grid_lat = np.arange(3, 15.1, 0.1, dtype='float64')
                lon_x = month_kg['Lon']
                lat_y = month_kg['Lat']
                rf_value_mon = month_kg['Monthly Total Rainfall']
                variogram = st.session_state['variogram']   
                Ordinary_Kriging = OrdinaryKriging(lon_x, 
                                        lat_y, 
                                        rf_value_mon, 
                                        variogram_model=variogram
                                        )
                OK_mon_rf, var_mon_rf = Ordinary_Kriging.execute('grid', grid_lon, grid_lat)
                    
            
                if 'OK_mon_rf' not in st.session_state:
                    st.session_state['OK_mon_rf'] = OK_mon_rf
            
        else:
            clicked = st.button("Perform Interpolation", key='interpol1')
            if clicked:
                grid_lon = np.arange(33, 48.1, 0.1, dtype='float64')
                grid_lat = np.arange(3, 15.1, 0.1, dtype='float64')
                lon_x = month_kg['Lon']
                lat_y = month_kg['Lat']
                rf_value_mon = month_kg['Monthly Total Rainfall']
                Universal_Kriging = UniversalKriging(lon_x, 
                                        lat_y, 
                                        rf_value_mon, 
                                        variogram_model=variogram,
                                        drift_terms=['regional_linear']
                                        )
                UK_mon_rf, var_mon_rf = Universal_Kriging.execute('grid', grid_lon, grid_lat)
                
                
                if 'UK_mon_rf' not in st.session_state:
                    st.session_state['UK_mon_rf'] = UK_mon_rf 
      
   
        st.subheader('Step 2: Display the spatial interpolation') 
        if 'OK_mon_rf' not in st.session_state:
            st.text('Please Load Rainfall Data 😔')
        else:
            clicked = st.button("View the interpolation output")   
            OK_mon_rf = st.session_state['OK_mon_rf']
            if clicked:   
                plt.figure(figsize=(4, 3))
                extent = [33, 48, 3, 15]
                grid_lon = np.arange(33, 48.1, 0.1, dtype='float64')
                grid_lat = np.arange(3, 15.1, 0.1, dtype='float64')
                lon2d1, lat2d1 = np.meshgrid(grid_lon, grid_lat)
                ax11 = plt.axes(projection=ccrs.PlateCarree())              
                c1= ax11.pcolormesh(lon2d1, lat2d1, OK_mon_rf, transform=ccrs.PlateCarree(),  cmap='viridis')
                ax11.coastlines()
                ax11.add_feature(cartopy.feature.OCEAN, zorder=100, edgecolor='k')
                ax11.add_feature(cartopy.feature.BORDERS, edgecolor='black')
                cb = plt.colorbar(c1,orientation="vertical",extendrect='True', shrink=0.60)
                cb.set_label("Rainfall [mm]", fontsize=6)
                plt.title("Interpolatation Result of Monthly Rainfall \n using Ordinary Kriging Interpolation", fontsize=5)
                st.pyplot(plt)            

            
        st.subheader('Step 3: Convert the interpolated surface into netCDF') 
            
        clicked = st.button("Convert to netCDF", key="nc1")
        if clicked:
            grid_lon = np.arange(33, 48.1, 0.1, dtype='float64')
            grid_lat = np.arange(3, 15.1, 0.1, dtype='float64')
            mon_rf_data = OK_mon_rf.data
            mon_rfDataset = xr.Dataset( data_vars= {'mon_rf_data':(('lat', 'lon'), mon_rf_data), },
                                        coords={'lat':grid_lat, 'lon':grid_lon})
            Dataset = mon_rfDataset.rename({'lat':'lat', 'lon':'lon'})
            Dataset['mon_rf_data'].attrs = {'units':'mm', 'long_name':'Monthly Rainfall'}
            Dataset.lat.attrs['units'] = 'degrees_north'
            Dataset.lat.attrs['long_name'] = 'latitude'
            Dataset.lat.attrs['axis'] = 'Y'
            Dataset.lon.attrs['units'] = 'degrees_east'
            Dataset.lon.attrs['long_name'] = 'longitude'
            Dataset.lon.attrs['axis'] = 'X'
            Dataset.attrs = {'creation_date':datetime.now(), 'author':'EMI', 'email':'address@email.com', 
                            'title':'Rainfall Data', 'source':'EMI', 'conventions':'CF-1.6', 'platform':'observation', 'institution':'EMI'}
            Mon_Rainfall_OK = Dataset.mon_rf_data
            Mon_Rainfall_OK.to_netcdf('Mon_Rainfall_OK.nc')  
            
            if 'Mon_Rainfall_OK' not in st.session_state:
                st.session_state['Mon_Rainfall_OK'] = Mon_Rainfall_OK    
            
            with open("Mon_Rainfall_OK.nc", "rb") as fp:
                btn = st.download_button(
                label="Download netCDF file",
                data=fp,
                file_name="Mon_Rainfall_OK.nc",
            ) 
                

                
                
        st.subheader('Step 4: Subset the interpolated surface into Ethiopian domain')  
        a = 200
        b = 33
        if b > a:
            print("b is greater than a")
        elif a == b:
            print("a and b are equal")
        else:
            if 'Mon_Rainfall_OK' not in st.session_state:
                st.text('Please Load Rainfall Data 😔')
            else:        
                clicked = st.button("Extract to the Ethiopian Domain")
                if clicked:
                    Mon_Rainfall_OK = st.session_state['Mon_Rainfall_OK']
                    Mon_Rainfall_OK_pro = Mon_Rainfall_OK.rio.write_crs("EPSG:4326", inplace=True)
                    shdf_wo = salem.read_shapefile(salem.get_demo_file('world_borders.shp'))
                    shdf_et = shdf_wo.loc[shdf_wo['CNTRY_NAME'] == 'Ethiopia'] 
                    Mon_Rainfall_OK_pro_et = Mon_Rainfall_OK_pro.salem.roi(shape=shdf_et)
                    
                    if 'Mon_Rainfall_OK_pro_et' not in st.session_state:
                        st.session_state['Mon_Rainfall_OK_pro_et'] = Mon_Rainfall_OK_pro_et   
                    
            st.subheader('Step 5: Display the result within Ethiopian domain') 
            if 'Mon_Rainfall_OK_pro_et' not in st.session_state:
                st.text('Please Load Rainfall Data 😔')
            else:    
                clicked = st.button("Display the result")
                if clicked:
                    Mon_Rainfall_OK_pro_et = st.session_state['Mon_Rainfall_OK_pro_et']
        # if clicked:
        #     Mon_Rainfall_OK_pro_et.hvplot.quadmesh(
        #     'lon', 'lat', crs=ccrs.PlateCarree(),
        #     projection=ccrs.PlateCarree(),
        #     clim = (0, 400),
        #     ylim=(3, 15), 
        #     xlim = (33, 48),
        #     features = {'borders': '10m'},
        #     cmap='viridis',
        #     clabel = 'rainfall (mm)',
        #     project=True, 
        #     geo=True,
        #     rasterize=True, 
        #     coastline=True, 
        #     grid=True, 
        #     frame_width=500, 
        #     dynamic=False,  
        #     tiles='OSM').opts(title='first image') 
        
        
            
                    plt.figure(figsize=(4, 3))
                    extent = [33, 48, 3, 15]
                    grid_lon = np.arange(33, 48.1, 0.1, dtype='float64')
                    grid_lat = np.arange(3, 15.1, 0.1, dtype='float64')
                    lon2d1, lat2d1 = np.meshgrid(grid_lon, grid_lat)
                    ax11 = plt.axes(projection=ccrs.PlateCarree())
                    c1= ax11.pcolormesh(lon2d1, lat2d1, Mon_Rainfall_OK_pro_et , transform=ccrs.PlateCarree(),  cmap='viridis_r')
                    ax11.coastlines()
                    ax11.add_feature(cartopy.feature.OCEAN, zorder=100, edgecolor='k')
                    ax11.add_feature(cartopy.feature.BORDERS, edgecolor='black')
                    cb = plt.colorbar(c1,orientation="vertical",extendrect='True', shrink=0.60)
                    cb.set_label("Rainfall [mm]", fontsize=6)
                    plt.title("Interpolatation Result of Monthly Rainfall \n using Ordinary Kriging Interpolation", fontsize=5)
                    st.pyplot(plt)
        
        
        Mon_Rainfall_OK_pro_et = st.session_state['Mon_Rainfall_OK_pro_et']
        st.subheader('Step 6: Convert the final result into netCDF file and Download') 
        if 'Mon_Rainfall_OK_pro_et' not in st.session_state:
            st.text('Please Load Rainfall Data 😔')
        else:        
            clicked = st.button("Convert to netCDF", key="nc2")
            if clicked:
                Mon_Rainfall_OK_pro_et.to_netcdf('Mon_Rainfall_OK_pro_et.nc')  
                with open("Mon_Rainfall_OK.nc", "rb") as fp:
                    btn = st.download_button(
                    label="Download netCDF file",
                    data=fp,
                    file_name="Mon_Rainfall_OK_ET.nc",
                    ) 
                
        
      
        
        
            
   

        
      

        















    def mapping_tool():
        import streamlit as st
        # import numpy as np
        # from numpy import ma
        # import sys,os
        # import Nio
        # import Ngl

        # st.markdown(f"# {list(page_names_to_funcs.keys())[7]}")

        # st.header("Monthly Maps")
        # st.write('Total Rainfall Map for X Month')

        # f = Nio.open_file("/home/yoni/Documents/met_bulletin_template/et_tamsat_pre_mon_2019.nc","r")

        # pre = f.variables["rfe"][:]
        # rain = pre[0,:,:]
        # lon = f.variables['lon'][:]
        # lat = f.variables["lat"][:]
        # mask_specs = ["Ethiopia"]
        
        # MinLat = 3.0   #-- min lat
        # MaxLat = 15.0  #-- max lat
        # MinLon = 33.0  #-- min lon
        # MaxLon = 48.0  #-- max lon

        # wks = Ngl.open_wks("png","pre_june_con_lab44")
        
        # res = Ngl.Resources()
        # res.nglFrame = False
        
        # res.mpOutlineOn =                             True #-- turn on map outlines
        # res.mpGeophysicalLineColor = "gray50"
        # res.nglPointTickmarksOutward =                 True #-- tickmarks outward
        # res.cnFillOn = True                           #-- turn on contour level fill
        # res.cnFillPalette = "precip_11lev"              #precip2_17lev, precip3_16lev, precip4_11lev, precip_11lev
        # res.cnLinesOn = True                          #-- don't draw contour lines
        # res.cnLineLabelsOn = True                     #-- turn off contour line labels
        # res.cnLevelSelectionMode = "ManualLevels"     #-- set levels
        # res.cnMinLevelValF = 0.0                      #-- contour min. value
        # res.cnMaxLevelValF =  500                     #-- contour max. value
        # res.cnLevelSpacingF = 50.0                     #-- contour interval
        # res.cnFillDrawOrder = "PreDraw"               #-- contours first 
        # res.cnFillMode     = "RasterFill"
        # res.cnInfoLabelOn = True                     #-- turn off contour info label  
        # res.cnLineLabelBackgroundColor = "white"
        # res.cnLineLabelPlacementMode = "constant"
        # res.lbBoxMinorExtentF = 0.2                   #-- height of labelbar boxes
        # res.lbOrientation = "horizontal"              #-- horizontal labelbar
        # res.lbLabelFontHeightF = 0.014


        # res.mpDataBaseVersion = "MediumRes"           #-- alias to Ncarg4_1
        # res.mpDataSetName = "Earth..4"
        # res.mpLimitMode = "LatLon"
        
        # res.mpMinLatF = MinLat
        # res.mpMaxLatF = MaxLat
        # res.mpMinLonF = MinLon
        # res.mpMaxLonF = MaxLon
        # res.mpGridAndLimbOn = False
        
        # res.mpFillOn = True                                      #-- turn on map fill
        # res.mpOutlineBoundarySets = "National"
        # res.mpFillBoundarySets = "NoBoundaries"
        # res.mpAreaMaskingOn = True
        # res.mpMaskAreaSpecifiers = mask_specs
        # res.mpFillAreaSpecifiers = ["land","water"]
        # res.mpSpecifiedFillColors = ["gray65","lightblue","black"]  #-- Land,Ocean,InlandWater
        # res.mpNationalLineThicknessF     = 2.5                       # ; 2-1/2 times as thick.
        # res.mpGeophysicalLineThicknessF = 6.5
        # res.pmTickMarkDisplayMode       = "always"         # ; nicer tick mark labels
        # res.mpFillDrawOrder = "Predraw"                    #-- contours first 
        # res.sfXArray = lon
        # res.sfYArray = lat
        
        # res.tiMainString = "Monthly total rainfall during June 2022"     #-- add title
        # res.tiMainFontHeightF = 0.024
        # res.tiMainFontColor   = "black"
        # res.tiMainFont        = 26
        # res.tiMainOffsetYF    =  0.0009

        # res.tiXAxisString = "Longitude"                               #-- x-axis title
        # res.tiXAxisFont = 22
        # res.tiXAxisFontHeightF = 0.016
        # res.tiXAxisOffsetYF    = 0.04
        # res.tiXAxisOffsetXF    = -0.009
        
        # res.tiYAxisString = "Latitude"                               #-- y-axis title
        # res.tiYAxisFont = 22
        
        # #res.tiYAxisFont         = "helvetica"
        # res.tiYAxisFontHeightF = 0.016
        # res.tiYAxisOffsetXF     = 0.01
        
        # # Grids
        # res.mpGridAndLimbOn       = True                           # Turn on the grid lines 
        # res.mpGridLatSpacingF     = 2
        # res.mpGridLonSpacingF     = 2
        # res.mpGridLineDashPattern = 4                              #(/0, 11, 4/) -- 0=solid,11=dashed,4=line dotted
        # res.mpGridSpacingF        = 2                              #grid line spacing 1 degree
        # res.mpGridLineThicknessF  = 2.0                            #make grid lines thicker
        # res.mpGridLineColor       = "Gray30"                       # grid line color

        # res.tmLabelAutoStride = True                               #-- use nice tick mark labels
        # res.pmLabelBarOrthogonalPosF = -0.1                      #-- move labelbar upward
        # res.lbLabelFontHeightF = 0.015                            #-- labelbar labe font size
        # res.lbBoxMinorExtentF = 0.18                              #-- decrease height of #-- labelbar box 
        # res.lbOrientation = "horizontal"                          #-- horizontal labelbar
        # res.lbLabelFontHeightF = 0.014
        # res.lbTitleOn          = True                                        # write title (default: "labelbar")
        # res.lbTitleFont        = "courier-bold"                              # set title font
        # res.lbTitleFontColor   = "black"                                     # set title font
        # res.lbTitleFontHeightF = 0.012                                       # decrease the font size (default: 0.025)
        # res.lbTitlePosition    = "Bottom"                                    # labelbar title postion (default: "Top")
        # res.lbTitleString      = "Rainfall [mm]"                 # define labelbar title string
        # res.lbTitleOffsetF     = -0.4                                        # move the labelbar title upwards


        # #-- viewport resources
        # res.nglMaximize = False                                     #-- don't maximize plot
        # res.vpXF = 0.12                                              #-- x-pos of viewport
        # res.vpYF = 0.89                                              #-- start y-position of viewport
        # res.vpWidthF = 0.82                                         #-- width of viewport
        # res.vpHeightF = 0.64                                        #-- height of viewport
        
        # #-- create the contour plot
        # plot = Ngl.contour_map(wks,rain,res)
        # #-- write variable long_name and units to the plot
        # txres = Ngl.Resources()
        # txres.txFontHeightF = 0.018
        # #-- draw the frame
        # Ngl.frame(wks)

        # # st.map(plot) 




        st.write('Percent of Normal Rainfall Map for X Month')
        st.write('Monthly Rainfall Departure Map relative to the previous year for X Month')
        st.write('Monthly Maximum Temperature Map for X Month')
        st.write('Monthly Minimum Temperature Map for X Month')
        st.write('Monthly average Temperature Map for X Month')
        st.write('Average Temperature Departure Map relative to the previous year for X Month')



        st.header("Seasonal Maps")
        st.subheader('Bega Maps (October to January)')
        st.subheader('Belg Maps (February to April)')
        st.subheader('Kiremt Maps (June to September)')


        st.header("Annual Maps")
        st.write('Annual Total Rainfall for X Year')
        st.write('Percent of Normal Rainfall for X Year')
        st.write('Annual Total Rainfall X Year - Year (Previous year)')
        st.write('Mean Maximum Temperature for X Year')
        st.write('Mean Minimum Temperature for X Year')
        st.write('Wind Rose Diagrams over Selected Stations')








        




















    page_names_to_funcs = {
        "🏠 Landing Page": intro,
        "🗃️ Data Importing & Missing Data": data_reading_module,
        "🖩 Data Converter & Basic Summary ": basic_summary,
        "📊 Indices Calculator": intermediate_result,
        "📈 Time Series Plots ": time_series_plots,
        "💾 Interpolation & netCDF Convector":  netCDF_convector,
        "🌍 Map Room ":   mapping_tool,
    }




    demo_name = st.sidebar.selectbox("Navigation Panel", page_names_to_funcs.keys())
    page_names_to_funcs[demo_name]()