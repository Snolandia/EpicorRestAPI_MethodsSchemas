import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.QuoteAnalysisExpSvc
// Description: Quote Analysis Export Business Object
           This is not a typical business object and will not use the standard
           core/BOBase.i methods.  The only dataset used in this object is the
           browser of available QuoteDtl records.  Methods are available to do
           the Build/Delete of Quote Analysis data.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAnalysisExpSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAnalysisExpSvc/$metadata", {
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
   Summary: Invoke method BuildAnalysis
   Description: Call this method when the user already selected quote lines to process.
This method expects a LIST-DELIM delimited string of RowIds of all selected
QuoteDtl records.
   OperationID: BuildAnalysis
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/BuildAnalysis_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BuildAnalysis_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BuildAnalysis(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAnalysisExpSvc/BuildAnalysis", {
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
   Summary: Invoke method ClearAllAnalysis
   Description: Call this method to delete or clear all QuoteAnalysis records.
This method expects that the user already confirmed that records will be deleted.
   OperationID: ClearAllAnalysis
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/ClearAllAnalysis_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ClearAllAnalysis(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAnalysisExpSvc/ClearAllAnalysis", {
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

   /**  
   Summary: Invoke method GetByQuoteLine
   Description: This method finds the QuoteDtl record by QuoteNum/QuoteLine.
   OperationID: GetByQuoteLine
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetByQuoteLine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByQuoteLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetByQuoteLine(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAnalysisExpSvc/GetByQuoteLine", {
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
   Summary: Invoke method GetQuoteDtlBrw
   Description: This method assembles the QuoteDtl browse for the main data set.
   OperationID: GetQuoteDtlBrw
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetQuoteDtlBrw_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetQuoteDtlBrw_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetQuoteDtlBrw(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAnalysisExpSvc/GetQuoteDtlBrw", {
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
      @param vRowList
   */  
export interface BuildAnalysis_input{
      /**  A RowId list of selected QuoteDtl records.  */  
   vRowList:string,
}

export interface BuildAnalysis_output{
parameters : {
      /**  output parameters  */  
   vMessage:string,
}
}

export interface ClearAllAnalysis_output{
parameters : {
      /**  output parameters  */  
   vMessage:string,
}
}

export interface Erp_Tablesets_QuoteAnalysisExpTableset{
   QuoteDtlBrw:Erp_Tablesets_QuoteDtlBrwRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_QuoteDtlBrwRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Quote number to which this line item detail record is associated with. This is part of the foreign key to OrderHed file.  */  
   QuoteNum:number,
      /**  This field along with Company and QuoteNum make up the unique key to the table. The system generates this number during entry of new detail records. The system determines next available number by finding the QuoteDtl record for the Quote and the adding 1 to it.  */  
   QuoteLine:number,
      /**  Indicates if this Quote item has been ordered. This is not directly set by the user. It is updated via Order Entry when the QuoteDtl is referenced.  */  
   Ordered:boolean,
      /**   The user's Internal Part number used to identify line item part. It cannot  be blank. It does not have to exist in the Part table.

A default should be made when the QuoteDtl.XPartNum is changed.  The PartNum and XPartNum fields work together in providing defaults for each other. Default when a valid record is found in the PartXRef table. NOTE THE PART CROSS REFERENCE LOGIC IS NOT INCLUDED IN RELEASE 1.0 ... PLAN FOR FUTURE  */  
   PartNum:string,
      /**  Line Item description. The Part.Description can be used as a default.  */  
   LineDesc:string,
      /**  Optional field that contains the customers revision. Default from the Part.RevisionNum field.  */  
   RevisionNum:string,
      /**  Number that relates to the Customer master. Duplicated from QuoteHed.CustNum.  Used to allow efficient browsing of the QuoteDtl records for a specific customer.  */  
   CustNum:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Row has been selected for processing.  */  
   Selected:boolean,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

   /** Required : 
      @param ipQuoteNum
      @param ipQuoteLine
   */  
export interface GetByQuoteLine_input{
      /**  The Quote Number  */  
   ipQuoteNum:number,
      /**  The Quote Line Number  */  
   ipQuoteLine:number,
}

export interface GetByQuoteLine_output{
   returnObj:Erp_Tablesets_QuoteAnalysisExpTableset[],
}

   /** Required : 
      @param whereClauseQuoteDtl
      @param pageSize
      @param absolutePage
   */  
export interface GetQuoteDtlBrw_input{
      /**  Where clause to specify set of QuoteDtlBrw records to return  */  
   whereClauseQuoteDtl:string,
      /**  Page Size  */  
   pageSize:number,
      /**  Absolute Page  */  
   absolutePage:number,
}

export interface GetQuoteDtlBrw_output{
   returnObj:Erp_Tablesets_QuoteAnalysisExpTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
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

