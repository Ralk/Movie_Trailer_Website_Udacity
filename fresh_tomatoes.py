import webbrowser
import os
import re


# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Movie Trailers!</title>

    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <style type="text/css" media="screen">
        body {
            padding-top: 80px;
        }
        #trailer .modal-dialog {
            margin-top: 200px;
            width: 640px;
            height: 480px;
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        #trailer-video {
            width: 100%;
            height: 100%;
        }
        .movie-tile {
            margin-bottom: 20px;
        }
        .movie-tile:hover {
            background-color: #EEE;
            cursor: pointer;
        }
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: white;
        }
        .video-card {
          overflow: hidden;
          width: 350px;
          height: 600px;
          margin-bottom: 50px;
          border-radius: 10px;
          background-color: #fff;
          box-shadow: 0 4px 21px -12px rgba(0, 0, 0, .66);
          transform: rotate(0deg);
          transition: all 200ms ease;
          font-size: 18px;
          cursor: pointer;
        }
        .movie_title {
         font-weight: bold;
        }
        .video-card:hover {
          box-shadow: 0 34px 32px -33px rgba(0, 0, 0, .18);
          transform: translate(0px, -3px);
        }
        .video-bar {
          width: 4px;
          height: 100%;
          float: left;
        }
        .video-bar.color-blue {
          background-color: #39606d;
        }
        .video-post-text {
          margin-top: 19px;
          margin-right: 20px;
          margin-left: 20px;
          font-size: 17px;
          text-transform: uppercase;
        }
        .video-duration {
            font-size: 10px;
            background-color: #2a7375;
            border-radius: 3px;
            height: 16px;
            vertical-align: middle;
            border: 2px dashed cadetblue;
            width: 37%;
            text-align: center;
            font-style: italic;
            color: white;
        }
        .video-description {
          font-size: 13px;
          text-transform: none;
        }
        .section-title {
          color: #2F4C56;
          font-size: 26px;
          font-weight: 400;
          text-align: center;
          letter-spacing: 1px;
          text-transform: uppercase;
          margin-bottom: 20px;
        }
        .title-underline {
          display: block;
          width: 50%;
          height: 2px;
          margin-right: auto;
          margin-left: auto;
          background-color: #23b9b6;
          margin-top: -20px;
        }
        .video-section {
          padding-bottom: 80px;
          background-color: #f7f7f7;
        }
        .video-flex {
          display: flex;
          margin-top: 20px;
          justify-content: space-around;
          flex-wrap: wrap;
          align-items: flex-end;
        }
        @media (max-width: 991px) {
          .video-card {
            flex: 0 auto;
          }
        }
    </style>
    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.movie-tile', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });
        // Animate in the movies when the page loads
        $(document).ready(function () {
          $('.movie-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
        });
    </script>
</head>
'''


# The main page layout and title bar
main_page_content = '''
  <body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>

    <!-- Main Page Content -->
    <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand" href="#">Movie Trailers</a>
          </div>
        </div>
      </div>
    </div>
    <div>
        <h1 class="section-title">The Lord of the Ring Movie Trailers</h1>
        <div class="title-underline"></div>
    </div>
    <div class="container">
    <div class="video-section">
        <div class="w-container promotion-container">
          <div class="video-flex">
            {movie_tiles}
          </div>
        </div>
    </div>
    </div>

  </body>
</html>
'''


# A single movie entry html template
movie_tile_content2 = '''
<div data-ix="video-card" class="w-clearfix w-preserve-3d video-card movie-tile" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
<img width="100%" height="70%" src="{poster_image_url}" >
  <div class="video-bar color-blue"></div>
  <div class="video-post-text">
    <div class="movie_title">{movie_title}</div>
    <h5 class="video-duration">Duration: {movie_duration}</h5>
    <div class="video-description color-blue">{movie_storyline}</div>
  </div>
</div>
'''

def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)

        # Append the tile for the movie with its content filled in
        content += movie_tile_content2.format(
            movie_title=movie.title,
            movie_storyline=movie.storyline,
            movie_duration=movie.duration,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id
        )
    return content


def open_movies_page(movies):
    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')

    # Replace the movie tiles placeholder generated content
    rendered_content = main_page_content.format(
        movie_tiles=create_movie_tiles_content(movies))

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
