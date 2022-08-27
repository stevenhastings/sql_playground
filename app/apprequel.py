import streamlit as st
import pandas as pd

#DB MGMT
import sqlite3
conn = sqlite3.connect("data_bank\sqlplayground_app\sqlplayground_app\data\world.sqlite")
c = conn.cursor()

#FUNCTION MAKE EXECUTION
def sql_executor(raw_code):
    c.execute(raw_code)
    data = c.fetchall()
    return data 

city = ['ID,', 'Name,', 'CountryCode,', 'District,', 'Population']
country = ['Code,', 'Name,', 'Continent,', 'Region,', 'SurfaceArea,', 'IndepYear,', 'Population,', 'LifeExpectancy,', 'GNP,', 'GNPOld,', 'LocalName,', 'GovernmentForm,', 'HeadOfState,', 'Capital,', 'Code2']
countrylanguage = ['CountryCode,', 'Language,', 'IsOfficial,', 'Percentage']


def main():
    st.title("SQLPlayground")

    menu = ["Home", "About"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("HomePage")

        #Columns/Layout
        col1,col2 = st.columns(2)

        with col1:
            with st.form(key='query_form'):
                raw_code = st.text_area("SQL Code Here")
                submit_code = st.form_submit_button("Execute")

            #TABLE of INFORMATION

            with st.expander("Table Info"):
                table_info = {'city':city,'country':country,'country_language':countrylanguage}
                st.json(table_info)

        #RESULTS LAYOUTS
        with col2:
            if submit_code:
                st.info("Query Submitted")
                st.code(raw_code)

                #RESULTS
                query_results = sql_executor(raw_code)
                with st.expander("Results"):
                    st.write(query_results)

                with st.expander("Pretty Lil' Pandas View"):
                    query_df = pd.DataFrame(query_results)
                    st.dataframe(query_df)

    else:
        st.subheader("About")




if __name__ == "__main__":
    main()