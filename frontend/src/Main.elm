module Main exposing (..)

import Browser
import Html exposing (Html, div, h1, text)
import Http
import String exposing (left)
import Json.Decode exposing (Decoder, field, int)


main =
    Browser.element
        { init = init
        , update = update
        , subscriptions = subscriptions
        , view = view
        }


type Model
    = Failure
    | Loading
    | Success Int


init : () -> (Model, Cmd Msg)
init _ = (Loading, getCovidData)


type Msg
    = GotData (Result Http.Error Int)


update : Msg -> Model -> (Model, Cmd Msg)
update msg model =
    case msg of
        GotData result ->
            case result of
                Ok data ->
                    (Success data, Cmd.none)
                Err _ ->
                    (Failure, Cmd.none)


subscriptions : Model -> Sub Msg
subscriptions model = Sub.none


view : Model -> Html Msg
view model =
    let headerText =
            case model of
                Failure -> "Something went wrong"
                Success data -> "Got some data! " ++ (String.fromInt data)
                Loading -> "Loading..."
    in
        div []
            [ h1 [] [ text headerText ] ]


getCovidData : Cmd Msg
getCovidData =
    Http.get
        { url = "http://localhost:5000/covid/confirmed/total/2020-03-28"
        , expect = Http.expectJson GotData covidDecoder
        }


covidDecoder : Decoder Int
covidDecoder =
    field "US" int

