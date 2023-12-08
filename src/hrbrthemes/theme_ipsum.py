from copy import copy, deepcopy

from plotnine import *
from plotnine.data import mtcars
from plotnine.options import get_option

class theme_ipsum(theme_bw):
    """
    hrbrthemes::theme_ipsum()
    """
    
    def __init__(
      self,
      base_family = "Arial Narrow",
      base_size = 11.5,
      axis_text_size = 9,
      plot_title_family = "Arial Narrow",
      plot_title_face = "bold",
      plot_title_size = 16,
      plot_title_margin = {"t": 0, "b": 10, "l": 0, "r": 0, "units": "pt"},
      subtitle_family = "Arial Narrow",
      subtitle_size = 12,
      subtitle_face = "plain",
      subtitle_margin = {"t": 0, "b": 15, "l": 0, "r": 0, "units": "pt"},
      strip_text_family = "Arial Narrow",
      strip_text_size = 10,
      strip_text_face = "plain",
      caption_family = "Arial Narrow",
      caption_size = 8,
      caption_face = "italic",
      caption_margin = {"t": 10, "b": 0, "l": 0, "r": 0, "units": "pt"},
      axis_title_family = "Arial Narrow",
      axis_title_size = 9,
      axis_title_face = "plain",
      axis_title_just = "rt",
      plot_margin = 0.05,
      axis_text_margin = {"t": 0, "b": 0, "l": 0, "r": 0, "units": "pt"},
      axis_title_margin = {"t": 0, "b": 0, "l": 0, "r": 0, "units": "pt"},
      grid_col = "#cccccc",
      panel_spacing = 0.05
    ):

      super().__init__(base_size)
     
      self += theme(
          text = element_text(family = base_family),
          title = element_text(family = base_family),
          panel_border = element_blank(),
          legend_background = element_blank(),
          legend_key = element_blank(),
          panel_grid = element_line(
            color = grid_col, 
            size = 0.2
          ),
          panel_grid_major = element_line(
            color = grid_col, 
            size = 0.2
          ),
          panel_grid_minor = element_line(
            color = grid_col, 
            size = 0.15
          ),
          axis_text_x = element_text(
            size = axis_text_size,
            margin = axis_text_margin
          ),
          axis_text_y = element_text(
            size = axis_text_size,
            margin = axis_text_margin
          ),
          axis_title_x = element_text(
            ha = "right",
            size = axis_title_size,
            margin = axis_title_margin
          ),
          axis_title_y = element_text(
            ha = "left",
            va = "top",
            size = axis_title_size,
            margin = axis_title_margin,
          ),
          axis_ticks = element_blank(),
          strip_text = element_text(
            ha = "left",
            size = strip_text_size, 
            face = strip_text_face, 
            family = strip_text_family
          ),
          plot_margin = plot_margin,
          plot_title = element_text(
            ha = "left",
            size = plot_title_size, 
            family = plot_title_family, 
            face = plot_title_face,
            margin = plot_title_margin
          ),
          plot_subtitle = element_text(
            ha = "left",
            size = subtitle_size, 
            family = subtitle_family, 
            # face = subtitle_face,
            margin = subtitle_margin
          ),
          plot_caption = element_text(
            ha = "right",
            size = caption_size
          )
      )

      def __deepcopy__(self, memo):
          """
          Deep copy support for theme_ipsum
          """
          cls = self.__class__
          result = cls.__new__(cls)
          memo[id(self)] = result
          old = self.__dict__
          new = result.__dict__

          for key, item in old.items():
              if key == "_rcParams":
                  continue
              new[key] = deepcopy(old[key], memo)

          result._rcParams = {}
          for k, v in self._rcParams.items():
              try:
                  result._rcParams[k] = deepcopy(v, memo)
              except NotImplementedError:
                  result._rcParams[k] = copy(v)

          return result

