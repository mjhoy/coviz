module Histogram exposing (main)

import Browser
import Color
import Html exposing (Html, button, div, text)
import Html.Events exposing (onClick)
import Random exposing (Generator, Seed)
import TypedSvg exposing (g, rect, svg)
import TypedSvg.Attributes exposing (fill, stroke, strokeWidth, viewBox)
import TypedSvg.Attributes.InPx exposing (height, width, x, y)
import TypedSvg.Core exposing (Svg)
import TypedSvg.Types exposing (Paint(..), px)


main =
    Browser.element
      { init = init
      , update = update
      , view = view
      , subscriptions = subscriptions
      }



-- Helpers


generator : Generator Float
generator =
    Random.float 1 200


seed : Seed
seed =
    -- chosen by fair dice roll
    Random.initialSeed 227852860


rectangle : Float -> Float -> Svg msg
rectangle w h =
    rect
        [ x 100
        , y 100
        , width w
        , height h
        , fill <| Paint Color.blue
        , strokeWidth (px 2)
        , stroke <| Paint <| Color.rgba 0.8 0 0 0.5
        ]
        []



-- Model


type Model = Model Float

type Msg
    = Reset
    | Update Float

init : () -> (Model, Cmd Msg)
init flags = (Model 100, Cmd.none)


subscriptions : Model -> Sub Msg
subscriptions model =
  Sub.none

-- Update



update : Msg -> Model -> (Model, Cmd Msg)
update msg model =
    case msg of
        Reset -> (model, Random.generate Update (Random.float 1 1000))
        Update width -> (Model width, Cmd.none)



-- View


view : Model -> Html Msg
view (Model width) =
    div []
        [ button [ onClick Reset ] [ text "x" ]
        , div [] []
        , svg [ viewBox 0 0 800 600 ] [ rectangle width width ]
        ]
