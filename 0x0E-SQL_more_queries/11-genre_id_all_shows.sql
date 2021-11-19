-- list all shows within hbtn_0d_tvshows that have at least one genre linked
SELECT S.title, G.genre_id FROM tv_shows S LEFT JOIN tv_show_genres G on S.id = G.show_id ORDER BY S.title, G.genre_id
