package security

default allow := false

allow if {
    input.environment == "production"
    input.https_enabled == true
}

allow if {
    input.environment != "production"
}