module Main exposing (..)

import Browser
import Html exposing (Html, div, h1, text)

main =
  Browser.sandbox { init = init, update = update, view = view }

init : ()
init = ()

type Msg
  = Noop

update : Msg -> () -> ()
update _ _ = ()


view : () -> Html Msg
view model =
  div []
    [ h1 [] [ text "Hello world!" ] ]
