
export var epicorURL = "YOUR_EPICOR_API_URL_HERE"
/** Used to encode a string to base64 encoding */
export const encode = (str: string):string => Buffer.from(str, 'binary').toString('base64');
export var epicorHeaders: Headers = new Headers({'Content-Type': 'application/json','Accept': 'application/json'})

export function encodeToBase64(username:string, password:string){
    return encode(username + ":" + password)
}

export function setEpicorURL(str:string){
    epicorURL = str
}

export function getEpicorURL(){
    return epicorURL
}

export function setEpicorHeader(header:Headers){
    epicorHeaders = header
}

export function setEpicorHeaderAuthoriziation(username:string, password:string){
    epicorHeaders.set('Authorization', "Basic " + encode(username + ':' + password))
}
export interface EpicorJsonObject{
   "odata.metadata" : string
   value : any
}


