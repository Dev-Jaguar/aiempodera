import streamlit as st

# VARIABLES
url_video_1 = """
<blockquote class="tiktok-embed" cite="https://www.tiktok.com/@aiempodera/video/7283881695168728325" data-video-id="7283881695168728325" style="max-width: 605px;min-width: 325px;" > <section> <a target="_blank" title="@aiempodera" href="https://www.tiktok.com/@aiempodera?refer=embed">@aiempodera</a> Empoderate, inspirate. Proximamente. <a title="ai" target="_blank" href="https://www.tiktok.com/tag/ai?refer=embed">#ai</a> <a title="inspiration" target="_blank" href="https://www.tiktok.com/tag/inspiration?refer=embed">#inspiration</a> <a title="viral" target="_blank" href="https://www.tiktok.com/tag/viral?refer=embed">#viral</a> <a title="aprende" target="_blank" href="https://www.tiktok.com/tag/aprende?refer=embed">#aprende</a> <a target="_blank" title="♬ Epic Inspiration - DM Production" href="https://www.tiktok.com/music/Epic-Inspiration-7116400670005872641?refer=embed">♬ Epic Inspiration - DM Production</a> </section> </blockquote> <script async src="https://www.tiktok.com/embed.js"></script>
"""
url_video_2 = """
<blockquote class="tiktok-embed" cite="https://www.tiktok.com/@aiempodera/video/7284835784203455749" data-video-id="7284835784203455749" style="max-width: 605px;min-width: 325px;" > <section> <a target="_blank" title="@aiempodera" href="https://www.tiktok.com/@aiempodera?refer=embed">@aiempodera</a> <a title="crypto" target="_blank" href="https://www.tiktok.com/tag/crypto?refer=embed">#crypto</a> <a title="ia" target="_blank" href="https://www.tiktok.com/tag/ia?refer=embed">#ia</a> <a title="inspira" target="_blank" href="https://www.tiktok.com/tag/inspira?refer=embed">#inspira</a> <a title="elsalvador" target="_blank" href="https://www.tiktok.com/tag/elsalvador?refer=embed">#ElSalvador</a>🇸🇻 <a title="yanylovers" target="_blank" href="https://www.tiktok.com/tag/yanylovers?refer=embed">#yanylovers</a> #empodera <a title="nayibbukele" target="_blank" href="https://www.tiktok.com/tag/nayibbukele?refer=embed">#NayibBukele</a> @yanyespejo @nayibbukele <a target="_blank" title="♬ sonido original - AIEmpodera" href="https://www.tiktok.com/music/sonido-original-7284835793842424581?refer=embed">♬ sonido original - AIEmpodera</a> </section> </blockquote> <script async src="https://www.tiktok.com/embed.js"></script>"""

# SOME STUFF
st.title("Mira algunos de nuestros videos de AIEmpodera 🎥")

st.link_button("Hecho con :heart: desde :flag-co:", "https://www.tiktok.com/@aiempodera")

st.divider()

st.header("Algunos videos 📹")

col1, col2, col3 = st.columns(3)

video_1 = st.components.v1.html(url_video_1, height=600)

st.write("\n")

video_2 = st.components.v1.html(url_video_2, height=600)


