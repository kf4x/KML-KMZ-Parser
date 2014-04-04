#Parse
NOTE: this is only for KML KMZ with points only!

**First import**

    from JSON_model import *

**How to use**

    data = Data(location='http://data.cabq.gov/community/art/publicart/PublicArt.kmz', kmz=True)

---

##Misc

**File:** *art_desc_parser.py* is used to parse the html of the ABQ art found in the description.

eg.


              <tr>
                <td>Location</td>
                <td>City/County Government Building</td>
              </tr>
              <tr bgcolor="#D4E4F3">
                <td>Shape</td>
                <td>Point</td>
              </tr>
              <tr>
                <td>IMAGE_URL</td>
                <td>
                  <a href="http://www.flickr.com/photos/abqpublicart/6944724811/in/photostream/" target="_blank">http://www.flickr.com/photos/abqpublicart/6944724811/in/photostream/</a>
                </td>
              </tr>
              <tr bgcolor="#D4E4F3">
                <td>JPG_URL</td>
                <td>
                  <a href="http://farm8.staticflickr.com/7066/6944724811_92623fe4da_m.jpg" target="_blank">http://farm8.staticflickr.com/7066/6944724811_92623fe4da_m.jpg</a>
                </td>
              </tr>
            </table>
          </font>
        </body>
      </html>]]></description>


**Parsed into**

      "description": {
        "shape": "Point",
        "jpg_url": "http://farm8.staticflickr.com/7066/6944724811_92623fe4da_m.jpg",
        "image_url": "http://www.flickr.com/photos/abqpublicart/6944724811/in/photostream/",
        "title": "Fence II",
        "year": "2011",
        "art_code": "662.06",
        "artist": "Evan Dent",
        "type": "etchings",
        "address": "400 Marquette NW",
        "location": "City/County Government Building"
      }
