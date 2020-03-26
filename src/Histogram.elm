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
    Browser.sandbox { init = init, update = update, view = view }



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


type alias Model =
    { width : Float
    , height : Float
    }


init : Model
init =
    { width = 100
    , height = 100
    }



-- Update


type Msg
    = Reset


update : Msg -> Model -> Model
update msg model =
    case msg of
        Reset ->
            { model
                | width = 500
                , height = 500
            }



-- View


view : Model -> Html Msg
view model =
    div []
        [ button [ onClick Reset ] [ text "x" ]
        , div [] []
        , svg [ viewBox 0 0 800 600 ] [ rectangle model.width model.height ]
        ]
