module Main exposing (main)

import Browser
import Html exposing (..)
import Html.Attributes exposing (..)
import Html.Events exposing (onClick, onInput)
import Http
import Json.Decode exposing (Decoder, field, int)


main =
    Browser.element
        { init = init
        , update = update
        , subscriptions = subscriptions
        , view = view
        }


type Model
    = Waiting String
    | Failure
    | Loading String
    | Success Int


init : () -> ( Model, Cmd Msg )
init _ =
    ( Waiting "", Cmd.none )


type Msg
    = GotData (Result Http.Error Int)
    | UpdateDateInput String
    | Submit String


update : Msg -> Model -> ( Model, Cmd Msg )
update msg model =
    case msg of
        Submit date ->
            ( Loading date, getCovidData ("http://localhost:5000/covid/confirmed/total/" ++ date) )

        GotData result ->
            case result of
                Ok data ->
                    ( Success data, Cmd.none )

                Err _ ->
                    ( Failure, Cmd.none )

        UpdateDateInput string ->
            ( Waiting string, Cmd.none )


subscriptions : Model -> Sub Msg
subscriptions model =
    Sub.none


view : Model -> Html Msg
view model =
    let
        buildInputForm currentValue =
            [ input [ type_ "text", placeholder "date", value currentValue, onInput UpdateDateInput ] []
            , button [ onClick (Submit currentValue) ] [ text "Submit" ]
            ]

        ( headerText, inputForm ) =
            case model of
                Failure ->
                    ( "Something went wrong", buildInputForm "" )

                Success data ->
                    ( "Got some data! " ++ String.fromInt data, buildInputForm "" )

                Loading url ->
                    ( "Loading " ++ url, [] )

                Waiting url ->
                    ( "Enter a date (YYYY-MM-DD) for total US confirmed cases:", buildInputForm url )
    in
    div []
        [ h1 [] [ text headerText ], div [] inputForm ]


getCovidData : String -> Cmd Msg
getCovidData url =
    Http.get
        { url = url
        , expect = Http.expectJson GotData covidDecoder
        }


covidDecoder : Decoder Int
covidDecoder =
    field "US" int
