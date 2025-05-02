import streamlit as st
import streamlit.components.v1 as components


powerbi_url = "https://app.powerbi.com/view?r=eyJrIjoiMmUzZTAwMDUtNGNlOS00OTQyLWFlZjctYTQ4NWJkZTQ5Y2QzIiwidCI6ImM2ZTU0OWIzLTVmNDUtNDAzMi1hYWU5LWQ0MjQ0ZGM1YjJjNCJ9" 
components.iframe(powerbi_url, width=800, height=500)