import streamlit as st
import pandas as pd
# DB MGMT
import sqlite3

conn = sqlite3.connect("C:\\Users\\steve\\PycharmProjects\\sql_playground\\data\\world.sqlite")
c = conn.cursor()

conn = sqlite3.connect("C:\\Users\\steve\\PycharmProjects\\sql_playground\\data\\chinook.db")
c = conn.cursor()


# FUNCTION MAKE EXECUTION
def sql_executor(raw_code):
    c.execute(raw_code)
    data = c.fetchall()
    return data


city = ['ID,', 'Name,', 'CountryCode,', 'District,', 'Population']

country = ['Code,', 'Name,', 'Continent,', 'Region,', 'SurfaceArea,', 'IndepYear,', 'Population,', 'LifeExpectancy,',
           'GNP,', 'GNPOld,', 'LocalName,', 'GovernmentForm,', 'HeadOfState,', 'Capital,', 'Code2']

countrylanguage = ['CountryCode,', 'Language,', 'IsOfficial,', 'Percentage']

employees = ['employee_id', 'first_name', 'last_name',
             'email', 'phone', 'address', 'city', 'state',
             'country', 'postal_code', 'active', 'hire_date', 'termination_date']

customers = ['customer_id', 'first_name', 'last_name', 'email',
             'phone', 'address', 'city', 'state', 'country',
             'postal_code', 'active', 'credit_limit']

invoices = ['invoice_id', 'customer_id', 'invoice_date',
            'billing_address', 'billing_city', 'billing_state',
            'billing_country', 'billing_postal_code', 'total']

invoice_items = ['invoice_item_id', 'invoice_id', 'track_id',
                 'unit_price', 'quantity', 'discount']

tracks = ['track_id', 'name', 'album_id', 'media_type_id', 'genre_id',
          'composer', 'milliseconds', 'bytes', 'unit_price']

genres = ['genre_id', 'name']

media_types = ['media_type_id', 'name']

playlists = ['playlist_id', 'name', 'user_id']

playlist_tracks = ['playlist_id', 'track_id', 'playlist_track_id']


def main():
    st.title("SQLPlayground")

    menu = ["Home", "About"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("HomePage")

        # Columns/Layout
        col1, col2 = st.columns(2)

        with col1:
            with st.form(key='query_form'):
                raw_code = st.text_area("SQL Code Here")
                submit_code = st.form_submit_button("Execute")

            # TABLE of INFORMATION
            with st.expander("Country Information"):
                table_info = {'city': city, 'country': country, 'country_language': countrylanguage}
                st.json(table_info)

            with st.expander("Employee Information"):
                table_info = {'employees': employees, 'customers': customers, 'invoices': invoices,
                              'invoice_items': invoice_items, 'tracks': tracks, 'genres': genres,
                              'media_types': media_types, 'playlists': playlists, 'playlist_tracks': playlist_tracks}
                st.json(table_info)

        # RESULTS LAYOUTS
        with col2:
            if submit_code:
                st.info("Query Submitted")
                st.code(raw_code)

                # RESULTS
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
