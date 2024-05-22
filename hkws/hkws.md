### Directory specification
The design concept of Hikvision SDK is a functional programming. It does not go to the object -oriented direction very powerful, so it is a bit around for the use of the object -oriented partner for trial.

Directory specifications The following functions:
1. The functional library is classified according to Hikvision's hardware products, loading SDK, and the function of all hardware products contains the function of all hardware products is BASE_ADAPTER
2. Derivatively derived the second -level function of hardware products and constructed on the basis of Base_adapter with a inherited style.The CM_CAMERA_ADPT here is a general camera adapter. AI is the unique function of the adapter that needs to be derived on this basis., Other hardware equipment functions are perfectly pushed in order
