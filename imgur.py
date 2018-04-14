from imgurpython import ImgurClient

content_type = ['.mp4', '.gifv', '.webm']

def imgur_parse_link(link):
    if 'imgur' in link:
        for ct in content_types:
            if link.endswith(ct):
                return link
        id = link.split('/')[-1]
        try:
            return client.get_image(id).mp4
        except:
            return None

#image = imgur_parse_link('https://imgur.com/gallery/KhOSXiT')

#print(image)
