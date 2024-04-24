import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Ice.LIB.InAppNotificationsSvc
// Description: Provides methods to retrieve Notifications for license/user
and to get Notification content
// Version: v1



//////////////////////////////////////////////////////////////////////////
// OData methods:
//////////////////////////////////////////////////////////////////////////

   /**  
   Summary: Get service document
   Description: Get service document for the service
   OperationID: GetServiceDocument
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => application/json
   */  
export function getServiceDocument(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<JSON>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.InAppNotificationsSvc/", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as JSON)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Get metadata document
   Description: Get service ODATA metadata in XML format
   OperationID: GetMetadata
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: Returns metadata document => content
   */  
export function get_metadata(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.InAppNotificationsSvc/$metadata", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}



//////////////////////////////////////////////////////////////////////////
// Custom methods:
//////////////////////////////////////////////////////////////////////////

   /**  
   Summary: Invoke method GetNotificationsForCurrentUserKeepIdleTime
   Description: Calls M:Ice.Services.Lib.InAppNotificationsSvc.GetNotificationsForCurrentUser(System.String,System.String,System.String,System.String,System.String) without affecting the session's last accessed time.
   OperationID: GetNotificationsForCurrentUserKeepIdleTime
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNotificationsForCurrentUserKeepIdleTime_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNotificationsForCurrentUserKeepIdleTime_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNotificationsForCurrentUserKeepIdleTime(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.InAppNotificationsSvc/GetNotificationsForCurrentUserKeepIdleTime", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNotificationsForCurrentUser
   Description: Retrieve the unread notifications for the given user
(which should be the currently logged one).
   OperationID: GetNotificationsForCurrentUser
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNotificationsForCurrentUser_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNotificationsForCurrentUser_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNotificationsForCurrentUser(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.InAppNotificationsSvc/GetNotificationsForCurrentUser", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNotificationContent
   Description: Retrieve the contents for a given Notification Id.
   OperationID: GetNotificationContent
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNotificationContent_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNotificationContent_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNotificationContent(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.InAppNotificationsSvc/GetNotificationContent", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetUserPreferences
   Description: Retrieves User Preferences.
   OperationID: GetUserPreferences
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetUserPreferences_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetUserPreferences_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetUserPreferences(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.InAppNotificationsSvc/GetUserPreferences", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}



//////////////////////////////////////////////////////////////////////////
// OData Schemas:
//////////////////////////////////////////////////////////////////////////



//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param endpoint
      @param apiKey
      @param product
      @param notificationId
   */  
export interface GetNotificationContent_input{
      /**  Notifications APIM endpoint  */  
   endpoint:string,
      /**  subscription-key  */  
   apiKey:string,
      /**  ERP  */  
   product:string,
      /**  Notification ID  */  
   notificationId:string,
}

export interface GetNotificationContent_output{
   returnObj:any,      //schema had no properties on an object.
}

   /** Required : 
      @param endpoint
      @param apiKey
      @param product
      @param licenseId
      @param userId
   */  
export interface GetNotificationsForCurrentUserKeepIdleTime_input{
   endpoint:string,
   apiKey:string,
   product:string,
   licenseId:string,
   userId:string,
}

export interface GetNotificationsForCurrentUserKeepIdleTime_output{
   returnObj:any,      //schema had no properties on an object.
}

   /** Required : 
      @param endpoint
      @param apiKey
      @param product
      @param licenseId
      @param userId
   */  
export interface GetNotificationsForCurrentUser_input{
      /**  Notifications APIM endpoint  */  
   endpoint:string,
      /**  subscription-key  */  
   apiKey:string,
      /**  ERP  */  
   product:string,
      /**  License ID  */  
   licenseId:string,
      /**  User ID  */  
   userId:string,
}

export interface GetNotificationsForCurrentUser_output{
   returnObj:any,      //schema had no properties on an object.
}

   /** Required : 
      @param userId
      @param licenseId
      @param product
   */  
export interface GetUserPreferences_input{
      /**  User ID  */  
   userId:string,
      /**  License ID  */  
   licenseId:string,
      /**  Product  */  
   product:string,
}

export interface GetUserPreferences_output{
   returnObj:any,      //schema had no properties on an object.
}

