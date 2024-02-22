import streamlit as st

# VARIABLES
html_code = """
<blockquote class="tiktok-embed" cite="https://www.tiktok.com/@aiempodera/video/7283881695168728325" data-video-id="7283881695168728325" style="max-width: 605px;min-width: 325px;" > <section> <a target="_blank" title="@aiempodera" href="https://www.tiktok.com/@aiempodera?refer=embed">@aiempodera</a> Empoderate, inspirate. Proximamente. <a title="ai" target="_blank" href="https://www.tiktok.com/tag/ai?refer=embed">#ai</a> <a title="inspiration" target="_blank" href="https://www.tiktok.com/tag/inspiration?refer=embed">#inspiration</a> <a title="viral" target="_blank" href="https://www.tiktok.com/tag/viral?refer=embed">#viral</a> <a title="aprende" target="_blank" href="https://www.tiktok.com/tag/aprende?refer=embed">#aprende</a> <a target="_blank" title="♬ Epic Inspiration - DM Production" href="https://www.tiktok.com/music/Epic-Inspiration-7116400670005872641?refer=embed">♬ Epic Inspiration - DM Production</a> </section> </blockquote> <script async src="https://www.tiktok.com/embed.js"></script>
"""
url = "https://www.tiktok.com/@aiempodera"

# SOME STUFF
st.title("Mira algunos de nuestros videos de AIEmpodera 🎥")

st.write("Nuestro canal ")
st.components.v1.iframe(url, height=600)

st.title("Algunos videos 📹")
st.components.v1.html(html_code, height=600)
