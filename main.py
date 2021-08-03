import pandas as pd
import numpy as np
from plotly.offline import plot
import plotly.graph_objs as go
import plotly.express as px
import streamlit as st

# data :
games = pd.read_csv('datasets_nba/games.csv')
games_details = pd.read_csv('datasets_nba/games_details.csv')
players = pd.read_csv('datasets_nba/players.csv')
ranking = pd.read_csv('datasets_nba/ranking.csv')
teams = pd.read_csv('datasets_nba/teams.csv')
debut_reg_saison = {
    '2003': '2003-10-28',
    '2004': '2004-11-2',
    '2005': '2005-11-1',
    '2006': '2006-10-31',
    '2007': '2007-10-30',
    '2008': '2008-10-28',
    '2009': '2009-10-27',
    '2010': '2010-10-26',
    '2011': '2011-12-25',
    '2012': '2012-10-30',
    '2013': '2013-10-29',
    '2014': '2014-10-28',
    '2015': '2015-10-27',
    '2016': '2016-10-25',
    '2017': '2017-10-17',
    '2018': '2018-10-16',
    '2019': '2019-10-22',
}

# functions
def id_to_player(id): # id en str
    table = players[['PLAYER_ID', 'PLAYER_NAME']].drop_duplicates()
    return table[table['PLAYER_ID']==int(id)]['PLAYER_NAME']
def id_to_team(id): # id en str
    table = ranking[['TEAM_ID', 'TEAM']].drop_duplicates()
    return table[table['TEAM_ID']==int(id)]['TEAM']
def classement_saison_top10(annee): # annee en string
    data = ranking[(ranking['SEASON_ID']==int('1'+annee)) | (ranking['SEASON_ID']==int('2'+annee)) ]
    classement = data[data['STANDINGSDATE']==data['STANDINGSDATE'].iloc[0]].sort_values(by=['W'], ascending=False)[['TEAM', 'W', 'L', 'G', 'W_PCT', 'CONFERENCE', 'HOME_RECORD', 'ROAD_RECORD']].iloc[:10]
    classement.index = np.arange(1, len(classement) + 1)
    return classement
def stats_saison_1(annee): # annee en string
    pd.to_datetime(games['GAME_DATE_EST'])
    data = games[(games['SEASON']==int(annee)) & (games['GAME_DATE_EST']>=debut_reg_saison[annee])] # contient les matchs de la saison + playoffs

    nb_points_tot = data['PTS_home'].sum()+data['PTS_away'].sum()
    nb_matchs = len(data)

    when_home = data.pivot_table(index=['HOME_TEAM_ID'], values=['PTS_home'], aggfunc=np.sum)
    when_road = data.pivot_table(index=['VISITOR_TEAM_ID'], values=['PTS_away'], aggfunc=np.sum)
    tot = pd.concat([when_home, when_road], axis=1).sum(axis=1)
    equipe_plus_pts = id_to_team(tot.index[tot.argmax()]) # avec tot.iloc[tot.argmax()] pts
    equipe_moins_pts = id_to_team(tot.index[tot.argmin()])  # avec tot.iloc[tot.argmin()] pts

    g_details = games_details[games_details['GAME_ID'].isin(data['GAME_ID'])] # tous les matchs de la saison

    tot_player_pts = g_details.pivot_table(index=['PLAYER_ID'], values=['PTS'], aggfunc=np.sum)
    player_most_pts = id_to_player(tot_player_pts.index[tot_player_pts['PTS'].argmax()]) # avec tot_player_pts.iloc[tot_player_pts['PTS'].argmax()]

    tot_player_reb = g_details.pivot_table(index=['PLAYER_ID'], values=['REB'], aggfunc=np.sum)
    player_most_reb = id_to_player(tot_player_reb.index[tot_player_reb['REB'].argmax()])  # avec tot_player_reb.iloc[tot_player_reb['REB'].argmax()]

    tot_player_ast = g_details.pivot_table(index=['PLAYER_ID'], values=['AST'], aggfunc=np.sum)
    player_most_ast = id_to_player(tot_player_ast.index[tot_player_ast['AST'].argmax()])  # avec tot_player_ast.iloc[tot_player_ast['AST'].argmax()]

    tot_player_stl = g_details.pivot_table(index=['PLAYER_ID'], values=['STL'], aggfunc=np.sum)
    player_most_stl = id_to_player(tot_player_stl.index[tot_player_stl['STL'].argmax()])  # avec tot_player_stl.iloc[tot_player_stl['STL'].argmax()]

    tot_player_blk = g_details.pivot_table(index=['PLAYER_ID'], values=['BLK'], aggfunc=np.sum)
    player_most_blk = id_to_player(tot_player_blk.index[tot_player_blk['BLK'].argmax()])  # avec tot_player_blk.iloc[tot_player_blk['BLK'].argmax()]

    resultats = {
        "Nombre de points total" : nb_points_tot,
        "Nombre de matchs de la saison": nb_matchs,
        "Équipe(s) ayant marqué le plus de points" : [list(equipe_plus_pts), tot.iloc[tot.argmax()]],
        "Équipe(s) ayant marqué le moins de points": [list(equipe_moins_pts), tot.iloc[tot.argmin()]],
        "Joueur(s) avec le plus de points": [list(player_most_pts),list(tot_player_pts.iloc[tot_player_pts['PTS'].argmax()])[0]],
        "Joueur(s) avec le plus de rebonds": [list(player_most_reb), list(tot_player_reb.iloc[tot_player_reb['REB'].argmax()])[0]],
        "Joueur(s) avec le plus de passes décisives": [list(player_most_ast), list(tot_player_ast.iloc[tot_player_ast['AST'].argmax()])[0]],
        "Joueur(s) avec le plus de steals": [list(player_most_stl), list(tot_player_stl.iloc[tot_player_stl['STL'].argmax()])[0]],
        "Joueur(s) avec le plus de blocks": [list(player_most_blk), list(tot_player_blk.iloc[tot_player_blk['BLK'].argmax()])[0]],
    }

    return resultats
def stats_saison_2(annee): # top10
    pd.to_datetime(games['GAME_DATE_EST'])
    data = games[(games['SEASON'] == int(annee)) & (games['GAME_DATE_EST'] >= debut_reg_saison[annee])]  # contient les matchs de la saison + playoffs
    g_details = games_details[games_details['GAME_ID'].isin(data['GAME_ID'])]
    [fig1, fig2, fig3, fig4, fig5] = [None, None, None, None, None]
    try :
        # points total
        top10_player_pts = g_details.pivot_table(index=['PLAYER_ID'], values=['PTS'], aggfunc=np.sum)
        top10_most_pts = top10_player_pts.nlargest(10, 'PTS', keep='first')
        top10_most_pts['PLAYER_ID']=top10_most_pts.index
        top10_most_pts['PLAYER_ID']=top10_most_pts['PLAYER_ID'].apply(lambda x : id_to_player(x).values[0])
        fig1=go.Figure()
        fig1.add_trace(go.Histogram(histfunc="sum", y=top10_most_pts['PTS'], x=top10_most_pts['PLAYER_ID'],opacity=0.75,text=top10_most_pts['PTS']))
        fig1.update_layout(
           title="<b>Les 10 joueurs avec le plus de points<b>",
           template='simple_white',
           xaxis_title_text='Joueurs',  # xaxis label
           yaxis_title_text='Points',  # yaxis label
           bargap=0.2,  # gap between bars of adjacent location coordinates
        )
    except :
        pass

    try :
        # reb total
        top10_player_reb = g_details.pivot_table(index=['PLAYER_ID'], values=['REB'], aggfunc=np.sum)
        top10_most_reb = top10_player_reb.nlargest(10, 'REB', keep='first')
        top10_most_reb['PLAYER_ID']=top10_most_reb.index
        top10_most_reb['PLAYER_ID']=top10_most_reb['PLAYER_ID'].apply(lambda x : id_to_player(x).values[0])
        fig2=go.Figure()
        fig2.add_trace(go.Histogram(histfunc="sum", y=top10_most_reb['REB'], x=top10_most_reb['PLAYER_ID'],opacity=0.75,text=top10_most_reb['REB']))
        fig2.update_layout(
            title="<b>Les 10 joueurs avec le plus de rebonds<b>",
            template='simple_white',
            xaxis_title_text='Joueurs',  # xaxis label
            yaxis_title_text='Rebonds',  # yaxis label
            bargap=0.2,  # gap between bars of adjacent location coordinates
        )
    except :
        pass

    try :
        # ast total
        top10_player_ast = g_details.pivot_table(index=['PLAYER_ID'], values=['AST'], aggfunc=np.sum)
        top10_most_ast = top10_player_ast.nlargest(10, 'AST', keep='first')
        top10_most_ast['PLAYER_ID']=top10_most_ast.index
        top10_most_ast['PLAYER_ID']=top10_most_ast['PLAYER_ID'].apply(lambda x : id_to_player(x).values[0])
        fig3=go.Figure()
        fig3.add_trace(go.Histogram(histfunc="sum", y=top10_most_ast['AST'], x=top10_most_ast['PLAYER_ID'],opacity=0.75, text=top10_most_ast['AST']))
        fig3.update_layout(
            title="<b>Les 10 joueurs avec le plus de passes décisives<b>",
            template='simple_white',
            xaxis_title_text='Joueurs',  # xaxis label
            yaxis_title_text='passes décisives',  # yaxis label
            bargap=0.2,  # gap between bars of adjacent location coordinates
        )
    except :
        pass

    try :
        # steals total
        top10_player_stl = g_details.pivot_table(index=['PLAYER_ID'], values=['STL'], aggfunc=np.sum)
        top10_most_stl = top10_player_stl.nlargest(10, 'STL', keep='first')
        top10_most_stl['PLAYER_ID']=top10_most_stl.index
        top10_most_stl['PLAYER_ID']=top10_most_stl['PLAYER_ID'].apply(lambda x : id_to_player(x).values[0])
        fig4=go.Figure()
        fig4.add_trace(go.Histogram(histfunc="sum", y=top10_most_stl['STL'], x=top10_most_stl['PLAYER_ID'],opacity=0.75, text=top10_most_stl['STL']))
        fig4.update_layout(
            title="<b>Les 10 joueurs avec le plus de steals<b>",
            template='simple_white',
            xaxis_title_text='Joueurs',  # xaxis label
            yaxis_title_text='steals',  # yaxis label
            bargap=0.2,  # gap between bars of adjacent location coordinates
        )
    except :
        pass

    try :
        # steals total
        top10_player_blk = g_details.pivot_table(index=['PLAYER_ID'], values=['BLK'], aggfunc=np.sum)
        top10_most_blk = top10_player_blk.nlargest(10, 'BLK', keep='first')
        top10_most_blk['PLAYER_ID']=top10_most_blk.index
        top10_most_blk['PLAYER_ID']=top10_most_blk['PLAYER_ID'].apply(lambda x : id_to_player(x).values[0])
        fig5=go.Figure()
        fig5.add_trace(go.Histogram(histfunc="sum", y=top10_most_blk['BLK'], x=top10_most_blk['PLAYER_ID'],opacity=0.75, text=top10_most_blk['BLK']))
        fig5.update_layout(
            title="<b>Les 10 joueurs avec le plus de blocks<b>",
            template='simple_white',
            xaxis_title_text='Joueurs',  # xaxis label
            yaxis_title_text='blocks',  # yaxis label
            bargap=0.2,  # gap between bars of adjacent location coordinates
        )
    except :
        pass

    return [fig1, fig2, fig3, fig4, fig5]

# CSS
st.set_page_config(layout="wide")
st.markdown("""
<style>
.first_titre {
    font-size:50px !important;
    font-weight: bold;
    box-sizing: border-box;
    text-align: left;
    width: 100%;
    text-decoration: underline;
}
.intro{
    text-align: justify;
    font-size:20px !important;
}
.grand_titre {
    font-size:30px !important;
    font-weight: bold;
    text-decoration: underline;
    text-decoration-color: #2782CD;
    text-decoration-thickness: 5px;
}
.section_titre{
    font-size:20px !important;
    font-weight: bold;
    text-decoration-color: #2782CD;
    text-decoration-thickness: 5px;
    text-align:center
}
</style>
""", unsafe_allow_html=True)

################################
######## Streamlit app #########
################################

# Pages principales
PAGES = ["Accueil 🏠", "Basketball 🏀"]
st.sidebar.title('Menu :bulb:')
st.sidebar.write("---")
choix_page = st.sidebar.selectbox(label="Sports", options=PAGES)

if choix_page == "Accueil 🏠" :

    st.markdown('<p class="first_titre">Sports analytics</p>', unsafe_allow_html=True)
    st.write("##")
    col1, a, col2 = st.beta_columns((0.5,1,0.5))
    with a :
        st.image('images/nba_intro_image.png')

elif choix_page == "Basketball 🏀":

    st.sidebar.write("---")
    PAGES_categories = ["Saisons", "Équipes", "Matchs", "Joueurs"]
    choix_page_cat = st.sidebar.selectbox(label="Dashboard", options=PAGES_categories)

    if choix_page_cat == "Saisons" :
        choix_annee = list(debut_reg_saison.keys())[::-1]
        select_annee = st.sidebar.selectbox(label="Année", options=choix_annee)

        st.markdown('<p class="grand_titre">Dashboard saison ' + select_annee +'</p>', unsafe_allow_html=True)
        st.write("##")

        ## Top 10 tableau
        col_top10_gauche, col_mid, col_top10_droite = st.beta_columns((0.2,1,0.2))
        with col_mid :
            st.markdown('<p class="section_titre">Top 10 Teams</p>', unsafe_allow_html=True)
            st.write(classement_saison_top10(select_annee))
            st.write("##")
        st.write("---")
        st.write("##")

        ## Données numérique
        titre_g, titre_m, titre_d = st.beta_columns((0.2, 1, 0.2))
        with titre_m :
            st.markdown('<p class="section_titre">Top stats</p>', unsafe_allow_html=True)
            st.write("##")
        col1_tab, j, col2_tab = st.beta_columns((1,0.2,1))
        with col1_tab :
            for key in ['Nombre de points total',
                        'Nombre de matchs de la saison',
                        'Équipe(s) ayant marqué le plus de points',
                        'Équipe(s) ayant marqué le moins de points',
                        'Joueur(s) avec le plus de points']:
                try :
                    st.text('●  '+str(key)+' : '+str(', '.join(stats_saison_1(select_annee)[key][0]))+' ('+str(int(stats_saison_1(select_annee)[key][1]))+')')
                except :
                    st.text('●  ' + str(key) + ' : ' + str(int(stats_saison_1(select_annee)[key])) +' ('+str(int(stats_saison_1(select_annee)[key]))+')')
        with col2_tab :
            for key in ['Joueur(s) avec le plus de rebonds',
                        'Joueur(s) avec le plus de passes décisives',
                        'Joueur(s) avec le plus de steals',
                        'Joueur(s) avec le plus de blocks']:
                try:
                    st.text('●  ' + str(key) + ' : ' + str(', '.join(stats_saison_1(select_annee)[key][0])) + ' (' + str(
                        int(stats_saison_1(select_annee)[key][1])) + ')')
                except:
                    st.text('●  ' + str(key) + ' : ' + str(int(stats_saison_1(select_annee)[key])) + ' (' + str(
                        int(stats_saison_1(select_annee)[key])) + ')')

        st.write("##")
        st.write("---")
        st.write("##")
        ## Graphiques
        graph_g, graph_m, graph_d = st.beta_columns((0.2, 1, 0.2))
        with graph_m :
            st.markdown('<p class="section_titre">Top 10 players stats</p>', unsafe_allow_html=True)
            st.write("##")
        col1, m, col2 = st.beta_columns((3,0.2,3))
        with col1 :
            if stats_saison_2(select_annee)[0] is not None :
                st.plotly_chart(stats_saison_2(select_annee)[0])
            if stats_saison_2(select_annee)[2] is not None:
                st.plotly_chart(stats_saison_2(select_annee)[2])
            if stats_saison_2(select_annee)[4] is not None:
                st.plotly_chart(stats_saison_2(select_annee)[4])
        with col2 :
            if stats_saison_2(select_annee)[1] is not None:
                st.plotly_chart(stats_saison_2(select_annee)[1])
            if stats_saison_2(select_annee)[3] is not None:
                st.plotly_chart(stats_saison_2(select_annee)[3])
        with m :
            st.write("##")


