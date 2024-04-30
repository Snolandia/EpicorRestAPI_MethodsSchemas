import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.EpicorAgentSvc
// Description: Epicor Virtual Assistant main object
// Version: v1
*/ 



//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
// OData methods:
//////////////////////////////////////////////////////////////////////////

   /**  
   Summary: Get service document
   Description: Get service document for the service
   OperationID: GetServiceDocument
      @param epicorHeaders A string representing the epicor log in information to be used, 
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EpicorAgentSvc/", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EpicorAgentSvc/$metadata", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}



//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
// Custom methods:
//////////////////////////////////////////////////////////////////////////

   /**  
   Summary: Invoke method ProcessSkill
   Description: Invoked by Epicor Agent framework to cause a selected skill to be fully processed.
Has the potential of making state changes (alter database state)
   OperationID: ProcessSkill
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ProcessSkill_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ProcessSkill_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ProcessSkill(requestBody:ProcessSkill_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ProcessSkill_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EpicorAgentSvc/ProcessSkill", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ProcessSkill_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetSkillVersion
   Description: Gets the API version with which a given skill is registered.
This returns the first api version for a given skill that is found.
   OperationID: GetSkillVersion
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetSkillVersion_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSkillVersion_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetSkillVersion(requestBody:GetSkillVersion_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetSkillVersion_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EpicorAgentSvc/GetSkillVersion", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetSkillVersion_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateEntity
   Description: Performs validation of user-supplied (typically) parameters/entities for a given skill
   OperationID: ValidateEntity
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateEntity_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateEntity_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateEntity(requestBody:ValidateEntity_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateEntity_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EpicorAgentSvc/ValidateEntity", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ValidateEntity_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SkillSupported
   Description: Verify if requested skill is supported by this platform
   OperationID: SkillSupported
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/SkillSupported_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SkillSupported_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SkillSupported(requestBody:SkillSupported_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<SkillSupported_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EpicorAgentSvc/SkillSupported", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as SkillSupported_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetSupportedSkills
   Description: Return the list of skills supported for the specified api version
   OperationID: GetSupportedSkills
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetSupportedSkills_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSupportedSkills_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetSupportedSkills(requestBody:GetSupportedSkills_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetSupportedSkills_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EpicorAgentSvc/GetSupportedSkills", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetSupportedSkills_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetProviderId
   Description: Return unique identifier for this system previously set by <seealso cref="M:Erp.Services.BO.EpicorAgentSvc.SetProviderId(System.String)" />
   OperationID: GetProviderId
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetProviderId_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetProviderId(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetProviderId_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EpicorAgentSvc/GetProviderId", {
          method: 'post',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetProviderId_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SetProviderId
   Description: Persist unique identifier assigned to this system by Epicor Agent framework
   OperationID: SetProviderId
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/SetProviderId_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetProviderId_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SetProviderId(requestBody:SetProviderId_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<SetProviderId_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EpicorAgentSvc/SetProviderId", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as SetProviderId_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}



//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
// OData Schemas:
//////////////////////////////////////////////////////////////////////////



//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
export interface AssistantDataModel_AssistantAttachment{
   ContentType:string,
   Content:any,      //schema had no properties on an object.
   ContentUrl:string,
   ContentId:string,
   Name:string,
   ThumbnailUrl:string,
   TokenDictionary:any,      //schema had no properties on an object.
}

export interface AssistantDataModel_AssistantChoice{
   Description:string,
   PlatformObject:any,      //schema had no properties on an object.
   Synonyms:string,
   SecondaryContextId:string,
}

export interface AssistantDataModel_AssistantDialogState{
   IntentId:string,
   Entities:any,      //schema had no properties on an object.
   CurrentEntityIndex:number,
}

export interface AssistantDataModel_AssistantEntity{
   UserInput:string,
   Description:string,
   PlatformObject:any,      //schema had no properties on an object.
   SecondaryContextId:string,
   IsValid:boolean,
   EntityDefinition:AssistantDataModel_AssistantEntityDefinition[],
}

export interface AssistantDataModel_AssistantEntityDefinition{
   EntityId:string,
   IsUserInput:boolean,
   IsSavedToContext:boolean,
   IsInformational:boolean,
   RequiresSecondaryContext:boolean,
}

export interface AssistantDataModel_AssistantProcessRequest{
   UserId:string,
   PlatformUrl:string,
   Token:string,
   Locale:string,
   State:AssistantDataModel_AssistantDialogState[],
}

export interface AssistantDataModel_AssistantResponse{
   State:AssistantDataModel_AssistantDialogState[],
   IsValid:boolean,
   ResponseToUser:string,
   Choices:AssistantDataModel_AssistantChoice[],
   Attachment:AssistantDataModel_AssistantAttachment[],
}

export interface AssistantDataModel_AssistantValidationRequest{
   UserId:string,
   PlatformUrl:string,
   Token:string,
   Locale:string,
   EntityId:string,
   ValueToValidate:string,
   State:AssistantDataModel_AssistantDialogState[],
}

export interface GetProviderId_output{
      /**  String identifier of this platform for use of Agent framework  */  
   returnObj:string,
}

   /** Required : 
      @param skillIntentId
   */  
export interface GetSkillVersion_input{
      /**  Agent skill identifier  */  
   skillIntentId:string,
}

export interface GetSkillVersion_output{
   returnObj:string,
}

   /** Required : 
      @param apiVersion
   */  
export interface GetSupportedSkills_input{
      /**  Api version to permit coexistence of different iterations of skills  */  
   apiVersion:string,
}

export interface GetSupportedSkills_output{
   returnObj:string,
}

   /** Required : 
      @param skillIntentId
      @param request
      @param apiVersion
   */  
export interface ProcessSkill_input{
      /**  Agent skill to invoke  */  
   skillIntentId:string,
   request:AssistantDataModel_AssistantProcessRequest[],
      /**  Api version to permit coexistence of different iterations of skills  */  
   apiVersion:string,
}

export interface ProcessSkill_output{
   returnObj:AssistantDataModel_AssistantResponse[],
}

   /** Required : 
      @param providerId
   */  
export interface SetProviderId_input{
      /**  Unique identifier for this system  */  
   providerId:string,
}

export interface SetProviderId_output{
}

   /** Required : 
      @param skillIntentId
      @param apiVersion
   */  
export interface SkillSupported_input{
      /**  Epicor agent skill identifier  */  
   skillIntentId:string,
      /**  Api version to permit coexistence of different iterations of skills  */  
   apiVersion:string,
}

export interface SkillSupported_output{
   returnObj:boolean,
}

   /** Required : 
      @param skillIntentId
      @param request
      @param apiVersion
   */  
export interface ValidateEntity_input{
      /**  Agent skill identifier  */  
   skillIntentId:string,
   request:AssistantDataModel_AssistantValidationRequest[],
      /**  Api version to permit coexistence of different iterations of skills  */  
   apiVersion:string,
}

export interface ValidateEntity_output{
   returnObj:AssistantDataModel_AssistantResponse[],
}

