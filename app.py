import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as gg
import plotly.graph_objects as go
import os

# Set page configuration
st.set_page_config(
    page_title="Blinkit Grocery Real-Time Analytics",
    page_icon="🛒",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for modern styling
st.markdown("""
<style>
    /* Main container tweaks */
    .main .block-container {
        padding-top: 1.5rem;
        padding-bottom: 2rem;
        max-width: 95%;
    }
    
    /* Header style */
    .dashboard-title {
        font-family: 'Inter', sans-serif;
        font-size: 2.2rem;
        font-weight: 800;
        color: #0F172A;
        margin-bottom: 0.2rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    .dashboard-subtitle {
        font-size: 1.0rem;
        color: #64748B;
        margin-bottom: 1.5rem;
    }

    /* Metric card styling */
    .metric-card {
        background: linear-gradient(135deg, #ffffff 0%, #f8fafc 100%);
        border: 1px solid #E2E8F0;
        border-radius: 12px;
        padding: 1.2rem;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    .metric-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.08), 0 4px 6px -2px rgba(0, 0, 0, 0.04);
    }
    .metric-title {
        font-size: 0.85rem;
        font-weight: 600;
        color: #64748B;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        margin-bottom: 0.4rem;
    }
    .metric-value {
        font-size: 1.8rem;
        font-weight: 800;
        color: #0C831F; /* Blinkit Green accent */
        line-height: 1.2;
    }
    .metric-subtitle {
        font-size: 0.8rem;
        color: #94A3B8;
        margin-top: 0.4rem;
    }

    /* Badge styles */
    .badge-green {
        background-color: #DCFCE7;
        color: #15803D;
        padding: 2px 8px;
        border-radius: 9999px;
        font-size: 0.75rem;
        font-weight: 600;
    }
    
    .badge-yellow {
        background-color: #FEF9C3;
        color: #A16207;
        padding: 2px 8px;
        border-radius: 9999px;
        font-size: 0.75rem;
        font-weight: 600;
    }

    /* Tab styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 42px;
        white-space: pre;
        background-color: #F1F5F9;
        border-radius: 8px 8px 0 0;
        color: #475569;
        font-weight: 600;
        padding: 0px 16px;
    }
    .stTabs [aria-selected="true"] {
        background-color: #0C831F !important;
        color: white !important;
    }
</style>
""", unsafe_allow_html=True)

# Load and clean dataset
@st.cache_data
def load_data():
    file_path = "BlinkIT Grocery Data.csv"
    if not os.path.exists(file_path):
        st.error(f"Dataset file '{file_path}' not found!")
        return pd.DataFrame()
    
    df = pd.read_csv(file_path)
    
    # Data Cleaning: Standardize Item Fat Content
    df['Item Fat Content'] = df['Item Fat Content'].replace({
        'LF': 'Low Fat',
        'low fat': 'Low Fat',
        'reg': 'Regular'
    })
    
    # Clean Outlet Size strings if needed
    df['Outlet Size'] = df['Outlet Size'].str.strip()
    
    return df

df_raw = load_data()

if df_raw.empty:
    st.stop()

# Header
col_header1, col_header2 = st.columns([3, 1])
with col_header1:
    st.markdown("""
        <div class="dashboard-title">
            🛒 Blinkit Grocery Real-Time Power BI Analytics Dashboard
        </div>
        <div class="dashboard-subtitle">
            Comprehensive business performance metrics, sales breakdowns, outlet insights, and product trends.
        </div>
    """, unsafe_allow_html=True)

with col_header2:
    st.markdown(
        """
        <div style="text-align: right; padding-top: 10px;">
            <span class="badge-green">● Live Connection</span>
            <span class="badge-yellow">Dataset: 8,523 Records</span>
        </div>
        """,
        unsafe_allow_html=True
    )

# Sidebar Filters
st.sidebar.markdown("## 🎛️ Dashboard Filters")
st.sidebar.markdown("---")

# Quick reset button state
if 'reset_filters' not in st.session_state:
    st.session_state.reset_filters = False

def reset_filter_callback():
    st.session_state.reset_filters = True

# Outlet Location Filter
location_options = sorted(list(df_raw['Outlet Location Type'].unique()))
selected_locations = st.sidebar.multiselect(
    "Outlet Location Tier",
    options=location_options,
    default=location_options
)

# Outlet Size Filter
size_options = sorted(list(df_raw['Outlet Size'].unique()))
selected_sizes = st.sidebar.multiselect(
    "Outlet Size",
    options=size_options,
    default=size_options
)

# Outlet Type Filter
outlet_type_options = sorted(list(df_raw['Outlet Type'].unique()))
selected_outlet_types = st.sidebar.multiselect(
    "Outlet Type",
    options=outlet_type_options,
    default=outlet_type_options
)

# Item Type Filter
item_type_options = sorted(list(df_raw['Item Type'].unique()))
selected_item_types = st.sidebar.multiselect(
    "Item Category",
    options=item_type_options,
    default=item_type_options
)

# Item Fat Content Filter
fat_options = sorted(list(df_raw['Item Fat Content'].unique()))
selected_fat = st.sidebar.multiselect(
    "Item Fat Content",
    options=fat_options,
    default=fat_options
)

# Establishment Year Filter
min_year = int(df_raw['Outlet Establishment Year'].min())
max_year = int(df_raw['Outlet Establishment Year'].max())
selected_years = st.sidebar.slider(
    "Establishment Year Range",
    min_value=min_year,
    max_value=max_year,
    value=(min_year, max_year)
)

st.sidebar.markdown("---")
if st.sidebar.button("🔄 Reset All Filters", use_container_width=True):
    st.rerun()

# Apply Filters to DataFrame
filtered_df = df_raw[
    (df_raw['Outlet Location Type'].isin(selected_locations)) &
    (df_raw['Outlet Size'].isin(selected_sizes)) &
    (df_raw['Outlet Type'].isin(selected_outlet_types)) &
    (df_raw['Item Type'].isin(selected_item_types)) &
    (df_raw['Item Fat Content'].isin(selected_fat)) &
    (df_raw['Outlet Establishment Year'] >= selected_years[0]) &
    (df_raw['Outlet Establishment Year'] <= selected_years[1])
]

if filtered_df.empty:
    st.warning("⚠️ No data available matching the selected filter criteria. Please adjust your sidebar filters.")
    st.stop()

# Key Performance Indicators (KPI Cards)
total_sales = filtered_df['Total Sales'].sum()
avg_sales = filtered_df['Total Sales'].mean()
no_of_items = len(filtered_df)
avg_rating = filtered_df['Rating'].mean()
avg_visibility = filtered_df['Item Visibility'].mean() * 100  # Percentage

# Format Sales
if total_sales >= 1_000_000:
    total_sales_fmt = f"${total_sales / 1_000_000:.2f}M"
elif total_sales >= 1_000:
    total_sales_fmt = f"${total_sales / 1_000:.2f}K"
else:
    total_sales_fmt = f"${total_sales:.2f}"

kpi1, kpi2, kpi3, kpi4, kpi5 = st.columns(5)

with kpi1:
    st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">💰 Total Sales</div>
            <div class="metric-value">{total_sales_fmt}</div>
            <div class="metric-subtitle">Exact: ${total_sales:,.2f}</div>
        </div>
    """, unsafe_allow_html=True)

with kpi2:
    st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">📊 Avg Sales / Item</div>
            <div class="metric-value">${avg_sales:.1f}</div>
            <div class="metric-subtitle">Average order revenue</div>
        </div>
    """, unsafe_allow_html=True)

with kpi3:
    st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">📦 Total Items</div>
            <div class="metric-value">{no_of_items:,}</div>
            <div class="metric-subtitle">Filtered item count</div>
        </div>
    """, unsafe_allow_html=True)

with kpi4:
    st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">⭐ Avg Rating</div>
            <div class="metric-value">{avg_rating:.2f} <span style="font-size:1.2rem; color:#F59E0B;">★</span></div>
            <div class="metric-subtitle">Out of 5.0 scale</div>
        </div>
    """, unsafe_allow_html=True)

with kpi5:
    st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">👁️ Avg Visibility</div>
            <div class="metric-value">{avg_visibility:.2f}%</div>
            <div class="metric-subtitle">Product display ratio</div>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Main Navigation Tabs
tab_exec, tab_cat, tab_outlet, tab_data = st.tabs([
    "📊 Executive Summary",
    "📦 Category & Product Analytics",
    "🏪 Outlet Performance Analysis",
    "🔍 Raw Data Explorer"
])

# Color Palette Definitions
PRIMARY_COLOR = "#0C831F"
SECONDARY_COLOR = "#F7C600"
ACCENT_COLORS = ["#0C831F", "#F7C600", "#3B82F6", "#EC4899", "#8B5CF6", "#14B8A6", "#F97316"]

# --- TAB 1: EXECUTIVE SUMMARY ---
with tab_exec:
    col_pie1, col_pie2 = st.columns(2)
    
    with col_pie1:
        st.subheader("Total Sales by Fat Content")
        fat_sales = filtered_df.groupby('Item Fat Content')['Total Sales'].sum().reset_index()
        fig_fat = px.pie(
            fat_sales,
            values='Total Sales',
            names='Item Fat Content',
            hole=0.55,
            color='Item Fat Content',
            color_discrete_map={'Low Fat': '#0C831F', 'Regular': '#F7C600'}
        )
        fig_fat.update_traces(
            textinfo='percent+label+value',
            hovertemplate="<b>%{label}</b><br>Sales: $%{value:,.2f}<br>Percentage: %{percent}"
        )
        fig_fat.update_layout(margin=dict(t=30, b=10, l=10, r=10), showlegend=True, height=350)
        st.plotly_chart(fig_fat, use_container_width=True)

    with col_pie2:
        st.subheader("Percentage of Sales by Outlet Size")
        size_sales = filtered_df.groupby('Outlet Size')['Total Sales'].sum().reset_index()
        fig_size = px.pie(
            size_sales,
            values='Total Sales',
            names='Outlet Size',
            hole=0.55,
            color_discrete_sequence=['#3B82F6', '#10B981', '#F59E0B']
        )
        fig_size.update_traces(
            textinfo='percent+label',
            hovertemplate="<b>%{label} Size</b><br>Sales: $%{value:,.2f}<br>Share: %{percent}"
        )
        fig_size.update_layout(margin=dict(t=30, b=10, l=10, r=10), showlegend=True, height=350)
        st.plotly_chart(fig_size, use_container_width=True)

    st.markdown("---")

    # Sales Trend by Establishment Year
    st.subheader("Total Sales Trend by Outlet Establishment Year")
    year_sales = filtered_df.groupby('Outlet Establishment Year')['Total Sales'].sum().reset_index()
    fig_year = px.area(
        year_sales,
        x='Outlet Establishment Year',
        y='Total Sales',
        markers=True,
        line_shape='spline',
        color_discrete_sequence=['#0C831F']
    )
    fig_year.update_traces(
        fillcolor='rgba(12, 131, 31, 0.15)',
        hovertemplate="<b>Year %{x}</b><br>Total Sales: $%{y:,.2f}"
    )
    fig_year.update_layout(
        xaxis_title="Establishment Year",
        yaxis_title="Total Sales ($)",
        height=380,
        margin=dict(t=20, b=20, l=10, r=10)
    )
    st.plotly_chart(fig_year, use_container_width=True)

    # Fat Content by Outlet Location Tier (Stacked Bar) & Sales by Location Type
    col_loc1, col_loc2 = st.columns(2)
    
    with col_loc1:
        st.subheader("Fat Content Sales by Location Tier")
        tier_fat = filtered_df.groupby(['Outlet Location Type', 'Item Fat Content'])['Total Sales'].sum().reset_index()
        fig_tier_fat = px.bar(
            tier_fat,
            x='Outlet Location Type',
            y='Total Sales',
            color='Item Fat Content',
            barmode='stack',
            color_discrete_map={'Low Fat': '#0C831F', 'Regular': '#F7C600'}
        )
        fig_tier_fat.update_layout(
            xaxis_title="Outlet Location Tier",
            yaxis_title="Total Sales ($)",
            height=350,
            margin=dict(t=20, b=20, l=10, r=10)
        )
        st.plotly_chart(fig_tier_fat, use_container_width=True)

    with col_loc2:
        st.subheader("Sales by Outlet Location Tier")
        loc_sales = filtered_df.groupby('Outlet Location Type')['Total Sales'].sum().reset_index()
        fig_loc = px.bar(
            loc_sales,
            x='Outlet Location Type',
            y='Total Sales',
            color='Outlet Location Type',
            color_discrete_sequence=['#3B82F6', '#8B5CF6', '#EC4899'],
            text_auto='.2s'
        )
        fig_loc.update_layout(
            xaxis_title="Location Tier",
            yaxis_title="Total Sales ($)",
            height=350,
            showlegend=False,
            margin=dict(t=20, b=20, l=10, r=10)
        )
        st.plotly_chart(fig_loc, use_container_width=True)

# --- TAB 2: CATEGORY & PRODUCT ANALYTICS ---
with tab_cat:
    st.subheader("Total Sales by Item Type (Category Ranking)")
    item_sales = filtered_df.groupby('Item Type')['Total Sales'].sum().reset_index().sort_values('Total Sales', ascending=True)
    
    fig_item = px.bar(
        item_sales,
        x='Total Sales',
        y='Item Type',
        orientation='h',
        color='Total Sales',
        color_continuous_scale='Greens',
        text_auto='.2s'
    )
    fig_item.update_layout(
        yaxis_title="Item Type",
        xaxis_title="Total Sales ($)",
        height=500,
        coloraxis_showscale=False,
        margin=dict(t=20, b=20, l=10, r=10)
    )
    st.plotly_chart(fig_item, use_container_width=True)

    st.markdown("---")
    
    col_cat_detail1, col_cat_detail2 = st.columns([1, 1])
    
    with col_cat_detail1:
        st.subheader("Category Performance Table")
        cat_table = filtered_df.groupby('Item Type').agg(
            Total_Sales=('Total Sales', 'sum'),
            Avg_Sales=('Total Sales', 'mean'),
            Items_Count=('Item Identifier', 'count'),
            Avg_Rating=('Rating', 'mean'),
            Avg_Visibility=('Item Visibility', lambda x: x.mean() * 100)
        ).reset_index().sort_values('Total_Sales', ascending=False)
        
        cat_table_fmt = cat_table.copy()
        cat_table_fmt['Total_Sales'] = cat_table_fmt['Total_Sales'].map("${:,.2f}".format)
        cat_table_fmt['Avg_Sales'] = cat_table_fmt['Avg_Sales'].map("${:,.2f}".format)
        cat_table_fmt['Avg_Rating'] = cat_table_fmt['Avg_Rating'].map("{:.2f} ★".format)
        cat_table_fmt['Avg_Visibility'] = cat_table_fmt['Avg_Visibility'].map("{:.2f}%".format)
        
        st.dataframe(
            cat_table_fmt,
            column_config={
                "Item Type": "Category",
                "Total_Sales": "Total Revenue",
                "Avg_Sales": "Avg Ticket",
                "Items_Count": "Item Count",
                "Avg_Rating": "Rating",
                "Avg_Visibility": "Visibility"
            },
            hide_index=True,
            use_container_width=True,
            height=400
        )

    with col_cat_detail2:
        st.subheader("Item Visibility vs. Total Sales Analysis")
        fig_scatter = px.scatter(
            filtered_df.sample(min(1500, len(filtered_df)), random_state=42),
            x='Item Visibility',
            y='Total Sales',
            color='Item Fat Content',
            size='Rating',
            hover_data=['Item Type', 'Outlet Type'],
            color_discrete_map={'Low Fat': '#0C831F', 'Regular': '#F7C600'},
            opacity=0.7
        )
        fig_scatter.update_layout(
            xaxis_title="Item Visibility Ratio",
            yaxis_title="Total Sales ($)",
            height=400,
            margin=dict(t=20, b=20, l=10, r=10)
        )
        st.plotly_chart(fig_scatter, use_container_width=True)

# --- TAB 3: OUTLET PERFORMANCE ANALYSIS ---
with tab_outlet:
    st.subheader("All Comprehensive Metrics by Outlet Type")
    
    outlet_summary = filtered_df.groupby('Outlet Type').agg(
        Total_Sales=('Total Sales', 'sum'),
        Avg_Sales=('Total Sales', 'mean'),
        No_Of_Items=('Item Identifier', 'count'),
        Avg_Rating=('Rating', 'mean'),
        Avg_Visibility=('Item Visibility', lambda x: x.mean() * 100)
    ).reset_index().sort_values('Total_Sales', ascending=False)
    
    # Display styled summary table
    outlet_summary_fmt = outlet_summary.copy()
    outlet_summary_fmt['Total_Sales'] = outlet_summary_fmt['Total_Sales'].map("${:,.2f}".format)
    outlet_summary_fmt['Avg_Sales'] = outlet_summary_fmt['Avg_Sales'].map("${:,.2f}".format)
    outlet_summary_fmt['Avg_Rating'] = outlet_summary_fmt['Avg_Rating'].map("{:.2f} ★".format)
    outlet_summary_fmt['Avg_Visibility'] = outlet_summary_fmt['Avg_Visibility'].map("{:.2f}%".format)
    
    st.dataframe(
        outlet_summary_fmt,
        column_config={
            "Outlet Type": "Outlet Type",
            "Total_Sales": "Total Sales ($)",
            "Avg_Sales": "Average Sales ($)",
            "No_Of_Items": "Items Count",
            "Avg_Rating": "Avg Rating",
            "Avg_Visibility": "Avg Item Visibility (%)"
        },
        hide_index=True,
        use_container_width=True
    )
    
    st.markdown("---")
    
    col_out_fig1, col_out_fig2 = st.columns(2)
    
    with col_out_fig1:
        st.subheader("Total Sales Comparison across Outlet Types")
        fig_out_bar = px.bar(
            outlet_summary,
            x='Outlet Type',
            y='Total_Sales',
            color='Outlet Type',
            color_discrete_sequence=ACCENT_COLORS,
            text_auto='.2s'
        )
        fig_out_bar.update_layout(
            xaxis_title="Outlet Type",
            yaxis_title="Total Sales ($)",
            showlegend=False,
            height=380,
            margin=dict(t=20, b=20, l=10, r=10)
        )
        st.plotly_chart(fig_out_bar, use_container_width=True)

    with col_out_fig2:
        st.subheader("Average Ticket Size ($) by Outlet Type")
        fig_out_avg = px.bar(
            outlet_summary,
            x='Outlet Type',
            y='Avg_Sales',
            color='Outlet Type',
            color_discrete_sequence=['#8B5CF6', '#EC4899', '#3B82F6', '#10B981'],
            text_auto='.1f'
        )
        fig_out_avg.update_layout(
            xaxis_title="Outlet Type",
            yaxis_title="Average Sales ($)",
            showlegend=False,
            height=380,
            margin=dict(t=20, b=20, l=10, r=10)
        )
        st.plotly_chart(fig_out_avg, use_container_width=True)

# --- TAB 4: RAW DATA EXPLORER ---
with tab_data:
    st.subheader("🔍 Interactive Dataset Explorer & Export")
    
    search_term = st.text_input("Search records by Item Identifier or Item Type:", "")
    
    display_df = filtered_df
    if search_term:
        display_df = display_df[
            display_df['Item Identifier'].str.contains(search_term, case=False, na=False) |
            display_df['Item Type'].str.contains(search_term, case=False, na=False)
        ]
    
    st.markdown(f"Displaying **{len(display_df):,}** out of **{len(filtered_df):,}** filtered records.")
    
    st.dataframe(
        display_df,
        use_container_width=True,
        height=450
    )
    
    col_dl1, col_dl2 = st.columns([1, 4])
    with col_dl1:
        csv_data = display_df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 Download Cleaned CSV",
            data=csv_data,
            file_name="BlinkIT_Cleaned_Grocery_Data.csv",
            mime="text/csv",
            use_container_width=True
        )

# Footer
st.markdown("---")
st.markdown(
    """
    <div style="text-align: center; color: #94A3B8; font-size: 0.85rem; padding: 10px;">
        🛒 <b>Blinkit Real-Time Grocery Analytics Dashboard</b> | Developed for Executive Business Insights & KPI Tracking
    </div>
    """,
    unsafe_allow_html=True
)
