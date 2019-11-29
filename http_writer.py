def post_img(img_name, width=600, how='a'):
    '''
    assumes image is in /var/www/html/img
    how: a for append, w for write over
    '''
    img_path = '/img/' + img_name
    img_html = "<img src='{}' width='{}' /><br><br>\n".format(img_path, width)
    html_path = '/var/www/html/index.html'
    with open(html_path, how) as f: f.write(img_html)
