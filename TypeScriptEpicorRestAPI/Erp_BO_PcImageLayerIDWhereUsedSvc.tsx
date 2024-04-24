import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.PcImageLayerIDWhereUsedSvc
// Description: Determines which ConfigID's are using a specific Image Layer ID
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PcImageLayerIDWhereUsedSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PcImageLayerIDWhereUsedSvc/$metadata", {
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
   Summary: Invoke method GetImageLayerIDWhereUsed
   Description: Retrieve Configurations using the Image Layer ID passed into this method.
   OperationID: GetImageLayerIDWhereUsed
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetImageLayerIDWhereUsed_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetImageLayerIDWhereUsed_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetImageLayerIDWhereUsed(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PcImageLayerIDWhereUsedSvc/GetImageLayerIDWhereUsed", {
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
   Summary: Invoke method RebuildLayerDetails
   Description: Call this method when you want to push image layer definition changes to a configurator
   OperationID: RebuildLayerDetails
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RebuildLayerDetails_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RebuildLayerDetails_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RebuildLayerDetails(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PcImageLayerIDWhereUsedSvc/RebuildLayerDetails", {
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
export interface Erp_Tablesets_PcImageLayerIDWhereUsedRow{
      /**  Indicates the approval status of the configuration.  */  
   Approved:boolean,
      /**  Company identifier.  */  
   Company:string,
      /**  Indicates the configuration ID this Image LayerID is associated with.  */  
   ConfigID:string,
      /**  Indicates the type of configuration defined in Configuration Entry.  */  
   ConfigType:string,
      /**  Configuration description.  */  
   Description:string,
      /**  Identifies a unique Image Layer.  */  
   ImageLayerID:string,
      /**  Indicates selected status.  */  
   Selected:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PcImageLayerIDWhereUsedTableset{
   PcImageLayerIDWhereUsed:Erp_Tablesets_PcImageLayerIDWhereUsedRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param imageLayerID
   */  
export interface GetImageLayerIDWhereUsed_input{
      /**  Image Layer ID used to query configurations for their use.  */  
   imageLayerID:string,
}

export interface GetImageLayerIDWhereUsed_output{
   returnObj:Erp_Tablesets_PcImageLayerIDWhereUsedTableset[],
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

   /** Required : 
      @param pcImageLayerIDWhereUsedTS
   */  
export interface RebuildLayerDetails_input{
   pcImageLayerIDWhereUsedTS:Erp_Tablesets_PcImageLayerIDWhereUsedTableset[],
}

export interface RebuildLayerDetails_output{
parameters : {
      /**  output parameters  */  
   pcImageLayerIDWhereUsedTS:Erp_Tablesets_PcImageLayerIDWhereUsedTableset[],
}
}

