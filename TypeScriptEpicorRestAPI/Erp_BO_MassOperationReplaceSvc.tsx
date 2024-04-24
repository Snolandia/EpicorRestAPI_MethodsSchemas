import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.MassOperationReplaceSvc
// Description: Use this function to replace Mass Operation
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MassOperationReplaceSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MassOperationReplaceSvc/$metadata", {
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
   Summary: Invoke method ChangeFromOpCode
   Description: Validates the FromOpCode field and poplutes the From OpCode description.  Is called when
the From Op Code changes.  If the code is not valid, an exception will be thrown.
   OperationID: ChangeFromOpCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFromOpCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFromOpCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeFromOpCode(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MassOperationReplaceSvc/ChangeFromOpCode", {
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
   Summary: Invoke method ChangeToOpCode
   Description: Validates the ToOpCode field and poplutes the To OpCode description.  Is called when
the To Op Code changes.  If the code is not valid, an exception will be thrown.
   OperationID: ChangeToOpCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeToOpCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeToOpCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeToOpCode(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MassOperationReplaceSvc/ChangeToOpCode", {
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
   Summary: Invoke method RunMassOperationReplace
   Description: Peforms the Mass Operation Replace.
   OperationID: RunMassOperationReplace
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RunMassOperationReplace_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RunMassOperationReplace_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RunMassOperationReplace(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MassOperationReplaceSvc/RunMassOperationReplace", {
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
   Summary: Invoke method MassOperationReplaceGetNew
   Description: Creates a temporary record to store information needed for the mass operation replace process.
   OperationID: MassOperationReplaceGetNew
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/MassOperationReplaceGetNew_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MassOperationReplaceGetNew(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MassOperationReplaceSvc/MassOperationReplaceGetNew", {
          method: 'post',
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
// OData Schemas:
//////////////////////////////////////////////////////////////////////////



//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param cFromOpCode
      @param ds
   */  
export interface ChangeFromOpCode_input{
      /**  The proposed from operation code  */  
   cFromOpCode:string,
   ds:Erp_Tablesets_MassOperationReplaceTableset[],
}

export interface ChangeFromOpCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MassOperationReplaceTableset[],
}
}

   /** Required : 
      @param cToOpCode
      @param ds
   */  
export interface ChangeToOpCode_input{
      /**  The proposed To operation code  */  
   cToOpCode:string,
   ds:Erp_Tablesets_MassOperationReplaceTableset[],
}

export interface ChangeToOpCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MassOperationReplaceTableset[],
}
}

export interface Erp_Tablesets_MassOperationReplaceRow{
   Company:string,
   FromOpCode:string,
   FromOpCodeDesc:string,
   ToOpCode:string,
   ToOpCodeDesc:string,
      /**  Indicates whether or not to refresh Operation Description with the new Operation Description.  */  
   RefreshOpDesc:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_MassOperationReplaceTableset{
   MassOperationReplace:Erp_Tablesets_MassOperationReplaceRow[],
   MassOperationResults:Erp_Tablesets_MassOperationResultsRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_MassOperationResultsRow{
   Company:string,
   PartNum:string,
   RevisionNum:string,
   PartDescription:string,
   OprSeq:number,
   AltMethod:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Extensions_ExtensionRow{
   ColumnValues:object
   RowMod:string,
   SysRowID:string,
}

export interface Ice_Extensions_ExtensionTableColumn{
   ColumnName:string,
   ColumnType:string,
}

export interface Ice_Extensions_ExtensionTableData{
   Table:Ice_Extensions_ExtensionRow[],
   SystemCode:string,
   TableName:string,
   Columns:Ice_Extensions_ExtensionTableColumn[],
   PrimaryKeyColumns:string,
   PeerTableSystemCode:string,
   PeerTableName:string,
}

export interface MassOperationReplaceGetNew_output{
   returnObj:Erp_Tablesets_MassOperationReplaceTableset[],
}

   /** Required : 
      @param ds
   */  
export interface RunMassOperationReplace_input{
   ds:Erp_Tablesets_MassOperationReplaceTableset[],
}

export interface RunMassOperationReplace_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MassOperationReplaceTableset[],
}
}

