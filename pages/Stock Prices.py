import streamlit as st
from api_logic import get_screener_data

# Config app
st.set_page_config(page_title="Stock Screener", layout="wide")
st.title("Stock Screener")


# Selection options
sector_options = ("Consumer Cyclical", "Energy", "Technology", "Industrials", "Financial Services", "Basic Materials",
                  "Communication Services", "Consumer Defensive", "Healthcare", "Real Estate", "Utilities",
                  "Industrial Goods", "Financial", "Services", "Conglomerates")

exchange_options = ("nyse", "nasdaq", "amex", "euronext", "tsx", "etf", "mutual_fund")


# Define a Streamlit UI function
def stock_screener(my_api_key: str):
    """Provide the User interface to the financial modeling Prep API.
    This function provides the input widgets to interact with the get_screener_data()
    function from the api_logic module.
    Args:
    	my_api_key: The API key required for accessing the fmp API
    Returns:
    	A DataFrame of the stocks matching the user's inputs.
    """
    # Placing Input widgets in sidebar
    with st.sidebar.form(key="my_form", clear_on_submit=False):
        market_cap = st.number_input(label="MarketCapMoreThan", value=1000000, min_value=1000000)
        beta = st.number_input(label="BetaLessThan", value=1, max_value=2)
        volume = st.number_input(label="VolMoreThan", value=10000)
        sector = st.selectbox(label="Sector", options=sector_options)
        exchange = st.selectbox(label="Exchange", options=exchange_options)
        dividend = st.number_input(label="DividendMoreThan", value=0)
        # Submit button
        pressed = st.form_submit_button(label="Submit")

    # If Submit button is pressed, then retrieve stock screener results from API
    if not pressed:
        results = get_screener_data(api_key=my_api_key)
        st.dataframe(results, height=800)

    else:
        results = get_screener_data(
                    api_key=my_api_key,
                    marketcapmorethan=market_cap,
                    betalessthan=beta,
                    volmorethan=volume,
                    sector=sector,
                    exchange=exchange,
                    dividendmorethan=dividend
        )
        st.dataframe(results, height=800)

# Download screening results
    @st.cache
    def convert_df(df):
        # IMPORTANT: Cache the conversion to prevent computation on every rerun
        return df.to_csv().encode('utf-8')

    csv = convert_df(results)

    st.download_button(
        label="Download data as CSV",
        data=csv,
        file_name='screener_data.csv',
        mime='text/csv',
    )


# Call the function with API credentials
stock_screener(my_api_key=st.secrets.api_credentials.key)