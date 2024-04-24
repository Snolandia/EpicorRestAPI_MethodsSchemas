import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.AutoTranReversalSvc
// Description: SrcGLTran
           Give the user the ability to select a group of GLJrnDtl lines, with one Journal Number.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoTranReversalSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoTranReversalSvc/$metadata", {
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

   /**  
   Summary: Calls GetList for the service
   Description: Get list of items<div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetList
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLJrnDtlListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLJrnDtlListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoTranReversalSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLJrnDtlListRow)
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
   Summary: Invoke method CheckReverseDate
   Description: Check if New Reversing Apply Date is valid or not.
   OperationID: CheckReverseDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckReverseDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckReverseDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckReverseDate(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLJrnDtlListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoTranReversalSvc/CheckReverseDate", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLJrnDtlListRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckReverseDateRowMod
   Description: Check if New Reversing Apply Date is valid or not. Returns updated row with RowMod = 'U'
   OperationID: CheckReverseDateRowMod
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckReverseDateRowMod_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckReverseDateRowMod_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckReverseDateRowMod(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoTranReversalSvc/CheckReverseDateRowMod", {
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
   Summary: Invoke method ClosePeriodChanged
   Description: Fiscal period should be recalculated if closing period changed
   OperationID: ClosePeriodChanged
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ClosePeriodChanged_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ClosePeriodChanged_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ClosePeriodChanged(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoTranReversalSvc/ClosePeriodChanged", {
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
   Summary: Invoke method ClosePeriodChangedRowMod
   Description: Fiscal period should be recalculated if closing period changed. Returns updated row with RowMod = 'U'
   OperationID: ClosePeriodChangedRowMod
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ClosePeriodChangedRowMod_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ClosePeriodChangedRowMod_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ClosePeriodChangedRowMod(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoTranReversalSvc/ClosePeriodChangedRowMod", {
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
   Summary: Invoke method DeleteLinkingMemos
   Description: Delete linking memos is posting was not run.
   OperationID: DeleteLinkingMemos
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteLinkingMemos_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteLinkingMemos_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteLinkingMemos(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoTranReversalSvc/DeleteLinkingMemos", {
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
   Summary: Invoke method GetGLTranList
   Description: Get a list of GL journal Lines.
   OperationID: GetGLTranList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetGLTranList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetGLTranList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetGLTranList(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoTranReversalSvc/GetGLTranList", {
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
   Summary: Invoke method GetListCurrentCompany
   Description: Returns a list of rows that satisfy the where clause.
   OperationID: GetListCurrentCompany
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListCurrentCompany_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListCurrentCompany_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetListCurrentCompany(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoTranReversalSvc/GetListCurrentCompany", {
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
   Summary: Invoke method GetList
   Description: Returns a list of rows that satisfy the where clause.
   OperationID: GetList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetList(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoTranReversalSvc/GetList", {
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
   Summary: Invoke method OnChangeAmtToReverse
   Description: Purpose:  validate amount to reverse and update totals
Parameters:
<param name="ipAmtToReverse">amount to reverse</param><param name="ds">Epicor.Mfg.BO.AutoTranReversalDataSet</param>
Notes:
   OperationID: OnChangeAmtToReverse
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeAmtToReverse_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeAmtToReverse_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeAmtToReverse(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoTranReversalSvc/OnChangeAmtToReverse", {
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
   Summary: Invoke method OnChangeAmtToReverseRowMod
   Description: Purpose:  validate amount to reverse and update totals. Returns updated row with RowMod = 'U'
Parameters:
<param name="ipAmtToReverse">amount to reverse</param><param name="ds">Epicor.Mfg.BO.AutoTranReversalDataSet</param>
Notes:
   OperationID: OnChangeAmtToReverseRowMod
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeAmtToReverseRowMod_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeAmtToReverseRowMod_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeAmtToReverseRowMod(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoTranReversalSvc/OnChangeAmtToReverseRowMod", {
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
   Summary: Invoke method OnChangeAmtStatToReverse
   Description: Purpose:  validate amount to reverse and update totals
Parameters:
<param name="ipAmtStatToReverse">amount to reverse</param><param name="ds">Epicor.Mfg.BO.AutoTranReversalDataSet</param>
Notes:
   OperationID: OnChangeAmtStatToReverse
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeAmtStatToReverse_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeAmtStatToReverse_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeAmtStatToReverse(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoTranReversalSvc/OnChangeAmtStatToReverse", {
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
   Summary: Invoke method OnChangeAmtStatToReverseRowMod
   Description: Purpose:  validate amount to reverse and update totals. Returns updated row with RowMod = 'U'
Parameters:
<param name="ipAmtStatToReverse">amount to reverse</param><param name="ds">Epicor.Mfg.BO.AutoTranReversalDataSet</param>
Notes:
   OperationID: OnChangeAmtStatToReverseRowMod
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeAmtStatToReverseRowMod_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeAmtStatToReverseRowMod_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeAmtStatToReverseRowMod(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoTranReversalSvc/OnChangeAmtStatToReverseRowMod", {
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
   Summary: Invoke method OnChangeSelected
   Description: Purpose:  Update totals
Parameters:
<param name="ipSelected">boolean indicating if the line is selected or deselected</param><param name="ds">Epicor.Mfg.BO.AutoTranReversalDataSet</param>
Notes:
   OperationID: OnChangeSelected
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeSelected_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeSelected_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeSelected(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoTranReversalSvc/OnChangeSelected", {
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
   Summary: Invoke method OnChangeSelectedRowMod
   Description: Purpose:  Update totals. Returns updated row with RowMod = 'U'
Parameters:
<param name="ipSelected">boolean indicating if the line is selected or deselected</param><param name="ds">Epicor.Mfg.BO.AutoTranReversalDataSet</param>
Notes:
   OperationID: OnChangeSelectedRowMod
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeSelectedRowMod_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeSelectedRowMod_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeSelectedRowMod(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoTranReversalSvc/OnChangeSelectedRowMod", {
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
   Summary: Invoke method Post
   Description: Post
   OperationID: Post
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Post_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Post_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_Post(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AutoTranReversalSvc/Post", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLJrnDtlListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_GLJrnDtlListRow[],
}

export interface Erp_Tablesets_GLJrnDtlListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Fiscal year that entry applies to.  */  
   "FiscalYear":number,
      /**  Number that is assigned by the system. The Journal number is a way of relating the detail entries into a group that would normally balance.  The system assigns this number by finding  the journalnum of the last record for the fiscal year and adding one.  */  
   "JournalNum":number,
      /**  A system assigned number to which is used along with the company, FiscalYear and JournalNum to uniquely identify the record.  System determines number by reading last record for a specific Company/FiscalYear/JournalNum combination and adding 1.  */  
   "JournalLine":number,
      /**  Describes the journal transaction. Defaulted from GLJrnHed in journal entry program.  */  
   "Description":string,
      /**  Date for this journal transaction entry.  */  
   "JEDate":string,
      /**  The data entry Group that the journal entry is assigned to. This field is not directly maintainable, it is assigned by the entry program using the GroupID of the "current" group that the user is working with.  It is used as a selection criteria during the posting process.  */  
   "GroupID":string,
      /**  Date that this transaction was posted to the G/L files.  */  
   "PostedDate":string,
      /**  A code that defines a journal.  A  journal Identifies/groups entries together. See JrnlCode table.  */  
   "JournalCode":string,
   "TotCredit":number,
   "TotDebit":number,
      /**  Indicates that the transaction is a reversing entry created during the journal entry post for GLJrnHed transactions when flagged as Reverse = YES.  */  
   "Reverse":boolean,
      /**  Unique Book Identifier  */  
   "BookID":string,
      /**  Legal Number of source document  */  
   "LegalNumber":string,
      /**  Fiscal year suffix.  */  
   "FiscalYearSuffix":string,
      /**  this field equas ABTUID which was created during posting  */  
   "ABTUID":string,
      /**  This field shows Debit value of transaction recalculated from DebitAmount according to Currency of mentioned Book  */  
   "BookDebitAmount":number,
      /**  This field shows Credit value of transaction recalculated from CreditAmount according to Currency of mentioned Book  */  
   "BookCreditAmount":number,
      /**  if has reverse line  */  
   "HasReverseLine":boolean,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Journal Sequence Number  */  
   "Sequence":number,
   "BookCurrencyCode":string,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param reverseDate
      @param bookID
      @param ds
   */  
export interface CheckReverseDateRowMod_input{
      /**  Reversing Apply Date  */  
   reverseDate:string,
      /**  BookID  */  
   bookID:string,
   ds:Erp_Tablesets_AutoTranReversalTableset[],
}

export interface CheckReverseDateRowMod_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AutoTranReversalTableset[],
}
}

   /** Required : 
      @param reverseDate
      @param bookID
      @param ds
   */  
export interface CheckReverseDate_input{
      /**  Reversing Apply Date  */  
   reverseDate:string,
      /**  BookID  */  
   bookID:string,
   ds:Erp_Tablesets_AutoTranReversalTableset[],
}

export interface CheckReverseDate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AutoTranReversalTableset[],
}
}

   /** Required : 
      @param closePeriod
      @param ds
   */  
export interface ClosePeriodChangedRowMod_input{
      /**  Close Fiscal Period  */  
   closePeriod:number,
   ds:Erp_Tablesets_AutoTranReversalTableset[],
}

export interface ClosePeriodChangedRowMod_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AutoTranReversalTableset[],
}
}

   /** Required : 
      @param closePeriod
      @param ds
   */  
export interface ClosePeriodChanged_input{
      /**  Close Fiscal Period  */  
   closePeriod:number,
   ds:Erp_Tablesets_AutoTranReversalTableset[],
}

export interface ClosePeriodChanged_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AutoTranReversalTableset[],
}
}

   /** Required : 
      @param iABTUID
      @param ds
   */  
export interface DeleteLinkingMemos_input{
      /**  ABTUID of GLTransaction.  */  
   iABTUID:string,
   ds:Erp_Tablesets_AutoTranReversalTableset[],
}

export interface DeleteLinkingMemos_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AutoTranReversalTableset[],
}
}

export interface Erp_Tablesets_AutoTranReversalListTableset{
   GLJrnDtlList:Erp_Tablesets_GLJrnDtlListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_AutoTranReversalTableset{
   GLJournalLine:Erp_Tablesets_GLJournalLineRow[],
   GLJrnDtlMnlDEASch:Erp_Tablesets_GLJrnDtlMnlDEASchRow[],
   GLJrnLineReference:Erp_Tablesets_GLJrnLineReferenceRow[],
   SrcGLTran:Erp_Tablesets_SrcGLTranRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_GLJournalLineRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Fiscal year that entry applies to.  */  
   FiscalYear:number,
      /**  Number that is assigned by the system. The Journal number is a way of relating the detail entries into a group that would normally balance.  The system assigns this number by finding  the journalnum of the last record for the fiscal year and adding one.  */  
   JournalNum:number,
      /**  A system assigned number to which is used along with the company, FiscalYear and JournalNum to uniquely identify the record.  System determines number by reading last record for a specific Company/FiscalYear/JournalNum combination and adding 1.  */  
   JournalLine:number,
      /**  Describes the journal transaction. Defaulted from GLJrnHed in journal entry program.  */  
   Description:string,
      /**  Date for this journal transaction entry.  */  
   JEDate:string,
      /**  Fiscal period that this journal entry applies to.  */  
   FiscalPeriod:number,
      /**  The data entry Group that the journal entry is assigned to. This field is not directly maintainable, it is assigned by the entry program using the GroupID of the "current" group that the user is working with.  It is used as a selection criteria during the posting process.  */  
   GroupID:string,
      /**  User ID that posted this translation.  */  
   PostedBy:string,
      /**  Date that this transaction was posted to the G/L files.  */  
   PostedDate:string,
      /**  Indicates if this entry has been posted to the G/L master balance files. Unposted entries are excluded from all G/L reports.  */  
   Posted:boolean,
      /**   Indicates the module that created this journal entry.  This is assigned by the system.
Values can be; AR, AP, GL, PR.  */  
   SourceModule:string,
      /**  The Internal VendorNum that ties back to the Vendor master file.  This field is not directly maintainable.  */  
   VendorNum:number,
      /**  Vendor's invoice number.  */  
   APInvoiceNum:string,
      /**  A code that defines a journal.  A  journal Identifies/groups entries together. See JrnlCode table.  */  
   JournalCode:string,
      /**  If this field is left blank the system assigns the next available #. The next available # is the greater of last # on file plus one or the XaSyst.StartInvNum.  */  
   ARInvoiceNum:number,
      /**  BankAcctId of the BankAcct master that this check was drawn  against.  */  
   BankAcctID:string,
      /**  Check number.  */  
   CheckNum:number,
      /**  Cash Receipts reference field.  */  
   CRHeadNum:number,
      /**  Indicates that the transaction is a reversing entry created during the journal entry post for GLJrnHed transactions when flagged as Reverse = YES.  */  
   Reverse:boolean,
      /**  Bank Transaction Number.  Used when a transaction is a direct transfer from one bank account to another.  */  
   BankTranNum:number,
      /**   The identifier of the Bank Slip document (bank statement).  The user enters a bank slip during the reconciliation process.  This is then written into the related GLJrnDtl records.
Pertains to transactions related to a bank (checks, receipts, transfers, adjustments)  */  
   BankSlip:string,
      /**  Link to the related GLRefTyp.RefType.  */  
   RefType:string,
      /**  Link to the related Code in GLRefCod.RefCode  */  
   RefCode:string,
      /**  Global Company identifier.  Used in Multi-Company Journal.  */  
   ExtCompanyID:string,
      /**  Multi-Company G/L Reference Type from the external company.  This is used by the Multi-Company Journal.  */  
   ExtRefType:string,
      /**  Multi-Company G/L Reference Code from the external company.  This is used by the Multi-Company Journal.  */  
   ExtRefCode:string,
      /**  The Journal Number assigned at the destination or target company when this Multi-Company Journal is created.  */  
   GlbJournalNum:number,
      /**  The Journal Line assigned at the destination or target company when this Multi-Company Journal is created.  */  
   GlbJournalLine:number,
      /**  Journal Code used by the Multi-Company Journal when it gets created at the target external company.  */  
   GlbJournalCode:string,
      /**  Global Vendor number.  Used by Multi-Company Journal.  */  
   GlbVendorNum:number,
      /**  Global AP Invoice identifier.  Used by Multi-Company Journal.  */  
   GlbAPInvoiceNum:string,
      /**  Flag to indicate that a separate journal entry will be created at the target company for the Multi-Company G/L Account entered in this journal line.  */  
   MultiCompany:boolean,
      /**  Linked to a Multi-Company Journal.  */  
   Linked:boolean,
      /**  Extended text to describe the journal line entry.  Defaults from GLJrnHed.CommentText.  */  
   CommentText:string,
      /**  Global Company identifier.  Used in Multi-Company Journal.  */  
   GlbCompanyID:string,
      /**  The fiscal year for this journal transaction header from the external company. Assigned from GLJrnGrp.FiscalYear.  */  
   GlbFiscalYear:number,
      /**  Fiscal period from the external company that this journal entry applies to.  */  
   GlbFiscalPeriod:number,
      /**  The data entry Group from the external company that the journal entry is assigned to.  */  
   GlbGroupID:string,
      /**  Chart of Account ID  */  
   COACode:string,
      /**  Full GL account containing the controlled segment valid combinations up to 200 characters including the internal segment separator.  This is the unique identifier for the GL Account and is stored in physical segment number sequence with the vertical bar as its separator.  This field is not intended for end user display.  It is used internally as a unique identifier.  The display format GL Account is found in table GLAcctDisp.  */  
   GLAccount:string,
      /**  SegmentValue 1.  See COASegment segment number 1 for a description of this field.  */  
   SegValue1:string,
      /**  SegmentValue 2.  See COASegment segment number 2 for a description of this field.  */  
   SegValue2:string,
      /**  SegmentValue 3.  See COASegment segment number 3 for a description of this field.  */  
   SegValue3:string,
      /**  SegmentValue 4.  See COASegment segment number 4 for a description of this field.  */  
   SegValue4:string,
      /**  SegmentValue 5.  See COASegment segment number 5 for a description of this field.  */  
   SegValue5:string,
      /**  SegmentValue 6.  See COASegment segment number 6 for a description of this field.  */  
   SegValue6:string,
      /**  SegmentValue 7.  See COASegment segment number 7 for a description of this field.  */  
   SegValue7:string,
      /**  SegmentValue 8.  See COASegment segment number 8 for a description of this field.  */  
   SegValue8:string,
      /**  SegmentValue 9.  See COASegment segment number 9 for a description of this field.  */  
   SegValue9:string,
      /**  SegmentValue 10.  See COASegment segment number 10 for a description of this field.  */  
   SegValue10:string,
      /**  SegmentValue 11.  See COASegment segment number 11 for a description of this field.  */  
   SegValue11:string,
      /**  SegmentValue 12.  See COASegment segment number 12 for a description of this field.  */  
   SegValue12:string,
      /**  SegmentValue 13.  See COASegment segment number 13 for a description of this field.  */  
   SegValue13:string,
      /**  SegmentValue 14.  See COASegment segment number 14 for a description of this field.  */  
   SegValue14:string,
      /**  SegmentValue 15.  See COASegment segment number 15 for a description of this field.  */  
   SegValue15:string,
      /**  SegmentValue 16.  See COASegment segment number 16 for a description of this field.  */  
   SegValue16:string,
      /**  SegmentValue 17.  See COASegment segment number 17 for a description of this field.  */  
   SegValue17:string,
      /**  SegmentValue 18.  See COASegment segment number 18 for a description of this field.  */  
   SegValue18:string,
      /**  SegmentValue 19.  See COASegment segment number 19 for a description of this field.  */  
   SegValue19:string,
      /**  SegmentValue 20.  See COASegment segment number 20 for a description of this field.  */  
   SegValue20:string,
      /**  Full GL account containing the controlled segment valid combinations up to 200 characters including the internal segment separator.  This is the unique identifier for the GL Account and is stored in physical segment number sequence with the vertical bar as its separator.  This field is not intended for end user display.  It is used internally as a unique identifier.  The display format GL Account is found in table GLAcctDisp.  */  
   ExtGLAccount:string,
      /**  External Segment Value 1  */  
   ExtSegValue1:string,
      /**  External Segment Value 2  */  
   ExtSegValue2:string,
      /**  External Segment Value 3  */  
   ExtSegValue3:string,
      /**  External Segment Value 4  */  
   ExtSegValue4:string,
      /**  External Segment Value 5  */  
   ExtSegValue5:string,
      /**  External Segment Value 6  */  
   ExtSegValue6:string,
      /**  External Segment Value 7  */  
   ExtSegValue7:string,
      /**  External Segment Value 8  */  
   ExtSegValue8:string,
      /**  External Segment Value 9  */  
   ExtSegValue9:string,
      /**  External Segment Value 10  */  
   ExtSegValue10:string,
      /**  External Segment Value 11  */  
   ExtSegValue11:string,
      /**  External Segment Value 12  */  
   ExtSegValue12:string,
      /**  External Segment Value 13  */  
   ExtSegValue13:string,
      /**  External Segment Value 14  */  
   ExtSegValue14:string,
      /**  External Segment Value 15  */  
   ExtSegValue15:string,
      /**  External Segment Value 16  */  
   ExtSegValue16:string,
      /**  External Segment Value 17  */  
   ExtSegValue17:string,
      /**  External Segment Value 18  */  
   ExtSegValue18:string,
      /**  External Segment Value 19  */  
   ExtSegValue19:string,
      /**  External Segment Value 20  */  
   ExtSegValue20:string,
      /**  Unique Book Identifier  */  
   BookID:string,
      /**  Date record was created  */  
   CreateDate:string,
      /**  A unique code that identifies the document currency.  */  
   CurrencyCode:string,
      /**  Legal Number of source document  */  
   LegalNumber:string,
      /**  Indicates if this record has been processed by the balance logic.  Yes - the record has been processed.  No - the record needs to be processed.  */  
   PerBalFlag:boolean,
      /**  Indicates if this record has been processed by the balance logic.  Yes - the record has been processed.  No - the record needs to be processed.  */  
   TBFlag:boolean,
      /**  Indicates if this record has been processed by the balance logic.  Yes - the record has been processed.  No - the record needs to be processed.  */  
   DailyBalFlag:boolean,
      /**  Fiscal year suffix.  */  
   FiscalYearSuffix:string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   FiscalCalendarID:string,
      /**  Fiscal year suffix.  */  
   GlbFiscalYearSuffix:string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   GlbFiscalCalendarID:string,
      /**  Identifies the journal entry as one processed by consolidation posting mode where the data transfer is immediate and an intermediate book is used.  */  
   IntermediateProc:boolean,
      /**  Internal system calculated sequence number not inteneded for external use.  */  
   GenID:number,
      /**  Source Company Identifier.  Identifies the company where this GLJrnDtl originated from.  */  
   SrcCompany:string,
      /**  Unique Book Identifier  This is the book that is being consolidated into a target book.  */  
   SrcBook:string,
      /**  Full GL account containing the controlled segment valid combinations up to 200 characters including the internal segment separator.  This is the unique identifier for the GL Account and is stored in physical segment number sequence with the vertical bar as its separator.  This field is not intended for end user display.  It is used internally as a unique identifier.  The display format GL Account is found in table GLAcctDisp.  */  
   SrcGLAccount:string,
      /**  Source Journal Code  */  
   SrcJrnlCode:string,
      /**  Source Journal Number  */  
   SrcJournalNum:number,
      /**  Source Journal Line  */  
   SrcJournalLine:number,
      /**   P = derived from Periodic Consolidation.
C = derived from GLJrnDtl via Continuous Consolidation.
A = derived from Advanced Allocations.  */  
   SrcType:string,
      /**  this field equas ABTUID which was created during posting  */  
   ABTUID:string,
      /**  This field shows Debit value of transaction  */  
   DebitAmount:number,
      /**  This field shows Credit value of transaction  */  
   CreditAmount:number,
      /**  This field shows Debit value of transaction recalculated from DebitAmount according to Currency of mentioned Book  */  
   BookDebitAmount:number,
      /**  This field shows Credit value of transaction recalculated from CreditAmount according to Currency of mentioned Book  */  
   BookCreditAmount:number,
      /**  If the current line is reversal, then this field is used for link with original journal line. It equals SysRowID of original line.  */  
   ParentRUID:string,
      /**  if has reverse line  */  
   HasReverseLine:boolean,
      /**  This is the resolved balance account the period balance, currency balance and/or daily balance records were written under for this GL Journal Detail GL Account.  */  
   BalanceAcct:string,
      /**  This is the resolved balance account the trial balance records were written under for this GL Journal Detail GL Account.  */  
   TrialAcct:string,
      /**  When a posting rule creates a pair of journal details balancing each other, each detail in the pair should reference the other one. This allows to show correspondence of accounts in reports. Support of reports that allow this being visible is not in the scope of this change.  */  
   CorrAccUID:number,
      /**  This is the last allocation stamp that affected this GLJrnDtl.  */  
   AllocationStamp:string,
      /**  Identifies the allocation batch this journal entry was processed under.  */  
   BatchID:string,
      /**  This is the allocation id that processed this journal entry.  */  
   AllocID:string,
      /**  The allocation run number is a unique sequential number that identifies which run of an allocation batch this journal entry was created under.  */  
   RunNbr:number,
      /**  Intended for internal use only.  Updated by the Advanced Allocations Engine.  This identifies the last allocation run number that used this GLJrnDtl as a source record.  */  
   AllocRunNbr:number,
      /**  Internal next number sequence used to keep the records unique.  Not intended for display or use by the end user.  */  
   AllocTgtNbr:number,
      /**  Internal next number sequence used to keep the records unique.  Not intended for display or use by the end user.  */  
   AllocTgtSeq:number,
      /**  External COA Code  */  
   ExtCOACode:string,
      /**  MatchCode is used to match two or more journal detail records together.  */  
   MatchCode:string,
      /**  MatchDate is set when the journal detail record is matched to other journal detail records.  */  
   MatchDate:string,
      /**  Indicates whether or not the transaction has been flagged as reconciled.  */  
   Reconciled:boolean,
      /**   Identifies if statistical information may be entered for the natural (chart) account.
Accounts can be used only for monetary amounts, both monetary and statistical amounts or only for statistical amounts.
0 = Only used for monetary amounts.
1 = Used for both monetary and statistical amounts.
2 = Only used for statistical amounts.  */  
   Statistical:number,
      /**  Statistical UOM code.  */  
   StatUOMCode:string,
      /**  This field shows Debit statistical amount.  */  
   DebitStatAmt:number,
      /**  This field shows Credit statistical amount.  */  
   CreditStatAmt:number,
      /**  PaymentNumber  */  
   PaymentNumber:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Journal Sequence Number  */  
   Sequence:number,
      /**  Transaction Document Type  */  
   TranDocTypeID:string,
      /**  The Internal CustNum that ties back to the Customer master file.  */  
   CustNum:number,
      /**  CloseFiscalPeriod  */  
   CloseFiscalPeriod:number,
      /**  SourcePlant  */  
   SourcePlant:string,
      /**  Plant  */  
   Plant:string,
      /**  Used for integrations - system type for URL specified in ExtSysURL - B = BisTrack / L = LumberTrack / F = FiberTrack / blank = Building Supply  */  
   ExtSysType:string,
      /**  URL for drill back to an integrated external system  */  
   ExtSysURL:string,
      /**  Difference between statistical amount and the statistical amount previously reversed.  */  
   AmtStatAvailToReverse:number,
      /**  Statistical Amount to Reverse  */  
   AmtStatToReverse:number,
      /**  Book Amount to reverse.  */  
   AmtToReverse:number,
      /**  Transaction amount to reverse.  Prorated based upon the total book amount of the transaction and the amount currently being reversed.  */  
   AmtToReverseTrans:number,
      /**  Book Currency Code  */  
   BookCurrencyCode:string,
      /**  DEA Code  */  
   DEACodeDesc:string,
      /**  DEA End Date  */  
   DEAEndDate:string,
      /**  DEA Start Date  */  
   DEAStartDate:string,
      /**  Deferred Expense  */  
   DeferredExp:boolean,
      /**  DEA Distributed Amount  */  
   Distributed:number,
      /**  DEA Distributed Amount in Doc Currency  */  
   DocDistributed:number,
      /**  DEA Expense Amount in Doc Currency  */  
   DocExpense:number,
      /**  DEA Recognized Amount in Doc Currency  */  
   DocRecognized:number,
      /**  DEA Remaining Amount in Doc Currency  */  
   DocRemaining:number,
      /**  DEA Unrecognized Amount in Doc Currency  */  
   DocUnrecognized:number,
      /**  DEA Expense Amount  */  
   Expense:number,
      /**  JournalLine is recognized Deferred Expense Amortization  */  
   IsDEAJournalLine:boolean,
   IsDebitAmount:boolean,
   MemoJournalLine:number,
      /**  Logical that indicates if the current GLJrnDtl has been partially reversed.  */  
   PartiallyReversed:boolean,
      /**  DEA Recognized Amount  */  
   Recognized:number,
      /**  DEA Remaining Amount  */  
   Remaining:number,
      /**  Amount previously reversed.  */  
   ReversedAmt:number,
      /**  Total transaction amount reversed.  */  
   ReversedAmtTrans:number,
   ReversedStatAmt:number,
      /**  Logical indicating the journal line is selected for reversal.  */  
   Selected:boolean,
   StatAmt:number,
   StornoLineDescr:string,
   TransAmt:number,
      /**  DEA Unrecognized Amount  */  
   Unrecognized:number,
      /**  Difference between book amount and the amount previously reversed.  */  
   AmtAvailToReverse:number,
   BitFlag:number,
   GLAcctDispGLAcctDisp:string,
   GLAcctDispAccountDesc:string,
   GLAcctDispGLShortAcct:string,
   StatUOMStatUOMDesc:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_GLJrnDtlListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Fiscal year that entry applies to.  */  
   FiscalYear:number,
      /**  Number that is assigned by the system. The Journal number is a way of relating the detail entries into a group that would normally balance.  The system assigns this number by finding  the journalnum of the last record for the fiscal year and adding one.  */  
   JournalNum:number,
      /**  A system assigned number to which is used along with the company, FiscalYear and JournalNum to uniquely identify the record.  System determines number by reading last record for a specific Company/FiscalYear/JournalNum combination and adding 1.  */  
   JournalLine:number,
      /**  Describes the journal transaction. Defaulted from GLJrnHed in journal entry program.  */  
   Description:string,
      /**  Date for this journal transaction entry.  */  
   JEDate:string,
      /**  The data entry Group that the journal entry is assigned to. This field is not directly maintainable, it is assigned by the entry program using the GroupID of the "current" group that the user is working with.  It is used as a selection criteria during the posting process.  */  
   GroupID:string,
      /**  Date that this transaction was posted to the G/L files.  */  
   PostedDate:string,
      /**  A code that defines a journal.  A  journal Identifies/groups entries together. See JrnlCode table.  */  
   JournalCode:string,
   TotCredit:number,
   TotDebit:number,
      /**  Indicates that the transaction is a reversing entry created during the journal entry post for GLJrnHed transactions when flagged as Reverse = YES.  */  
   Reverse:boolean,
      /**  Unique Book Identifier  */  
   BookID:string,
      /**  Legal Number of source document  */  
   LegalNumber:string,
      /**  Fiscal year suffix.  */  
   FiscalYearSuffix:string,
      /**  this field equas ABTUID which was created during posting  */  
   ABTUID:string,
      /**  This field shows Debit value of transaction recalculated from DebitAmount according to Currency of mentioned Book  */  
   BookDebitAmount:number,
      /**  This field shows Credit value of transaction recalculated from CreditAmount according to Currency of mentioned Book  */  
   BookCreditAmount:number,
      /**  if has reverse line  */  
   HasReverseLine:boolean,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Journal Sequence Number  */  
   Sequence:number,
   BookCurrencyCode:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_GLJrnDtlMnlDEASchRow{
      /**  Company  */  
   Company:string,
      /**  FiscalCalendarID  */  
   FiscalCalendarID:string,
      /**  FiscalYear  */  
   FiscalYear:number,
      /**  FiscalYearSuffix  */  
   FiscalYearSuffix:string,
      /**  BookID  */  
   BookID:string,
      /**  JournalCode  */  
   JournalCode:string,
      /**  JournalNum  */  
   JournalNum:number,
      /**  JournalLine  */  
   JournalLine:number,
      /**  AmortSeq  */  
   AmortSeq:number,
      /**  SchFiscalCalendarID  */  
   SchFiscalCalendarID:string,
      /**  SchFiscalYear  */  
   SchFiscalYear:number,
      /**  SchFiscalYearSuffix  */  
   SchFiscalYearSuffix:string,
      /**  SchFiscalPeriod  */  
   SchFiscalPeriod:number,
      /**  AmortDate  */  
   AmortDate:string,
      /**  AmortPercent  */  
   AmortPercent:number,
      /**  AmortAmt  */  
   AmortAmt:number,
      /**  DocAmortAmt  */  
   DocAmortAmt:number,
      /**  Posted  */  
   Posted:boolean,
      /**  PostedDate  */  
   PostedDate:string,
      /**  TranDocTypeID  */  
   TranDocTypeID:string,
      /**  LegalNumber  */  
   LegalNumber:string,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  Rpt1AmortAmt  */  
   Rpt1AmortAmt:number,
   GroupID:string,
      /**  Document currency  */  
   CurrencyCode:string,
      /**  Rpt2AmortAmt  */  
   Rpt2AmortAmt:number,
      /**  Rpt3AmortAmt  */  
   Rpt3AmortAmt:number,
      /**  Used for Tracker only for records from GLJournalEntry. BookID in GLJrnDtl. The same as BookID field value for Single-book mode.  */  
   GLBookID:string,
      /**  Used for Tracker only for records from GLJournalEntry. Journal Number in GLJrnDtl. The same as JournalNum field value for Single-book mode.  */  
   GLJournalNum:number,
      /**  DispAmortAmt  */  
   DispAmortAmt:number,
      /**  DispDocAmortAmt  */  
   DispDocAmortAmt:number,
      /**  Indicates if this recognized Deferred Expense Amortization transaction has reverse lines  */  
   HasReverseLines:boolean,
      /**  Account Currency  */  
   CurrencyCodeAcct:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_GLJrnLineReferenceRow{
      /**  Identifier refers to GLJrnLine  */  
   GLJrnLineID:string,
      /**  Name of reference  */  
   RefType:string,
   RefValue:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_SrcGLTranRow{
   Company:string,
   ABTUID:string,
   BookID:string,
   BookDescription:string,
   JournalNum:number,
   JournalCode:string,
   GroupID:string,
   ApplyDate:string,
   PostedDate:string,
   Description:string,
   Reverse:boolean,
   RedStorno:boolean,
   LegalNumber:string,
   BookCreditAmount:number,
   BookDebitAmount:number,
   BookBalance:number,
   CreditAmount:number,
   DebitAmount:number,
   Balance:number,
   BookCurrencyCode:string,
   TranState:string,
      /**  This value is used for search Memos for reverse lines  */  
   MemoABTUID:string,
      /**  This value is used for search memos reverse GL Journal lines.  */  
   MemoGLTranDesc:string,
   FiscalYear:number,
   ReverseDate:string,
   FiscalYearSuffix:string,
      /**  Used by the UI for enabling/disabling the Red Storno prompt  */  
   RedStornoOpt:string,
      /**  Total Book Selected Debit Amount  */  
   TotBookSelDB:number,
      /**  Total Book Selected Credit Amount  */  
   TotBookSelCR:number,
      /**  Total Book Selected Balance.  This is the difference between the TotBookSelDB and TotBookSelCR.  */  
   TotBookSelBal:number,
      /**  Logical indicating the journal transaction has been partially reversed.  */  
   TranPartiallyReversed:boolean,
      /**  logical indicating if the transaction has been completely reversed  */  
   TranCompletelyReversed:boolean,
   FiscalPeriod:number,
   JournalCodeDesc:string,
      /**  Closing fiscal period number  */  
   CloseFiscalPeriod:number,
      /**  Flag for Last Year Date validation  */  
   YearLastDate:boolean,
      /**  Available for selection closing periods  */  
   CloseFiscalPeriodList:string,
      /**  Source GL Transaction currency code. GLJrnDtl.CurrencyCode  */  
   CurrencyCode:string,
   StatAmt:number,
   TotStatAmt:number,
   CurrencyCodeDesc:string,
   OrigFiscalPeriod:number,
   OrigFiscalYear:number,
   OrigFiscalYearSuffix:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

   /** Required : 
      @param abtUID
   */  
export interface GetGLTranList_input{
      /**  ABTUID for the search.  */  
   abtUID:string,
}

export interface GetGLTranList_output{
   returnObj:Erp_Tablesets_AutoTranReversalTableset[],
}

   /** Required : 
      @param whereClause
      @param pageSize
      @param absolutePage
   */  
export interface GetListCurrentCompany_input{
      /**  An expression used to filter the rows. Can be left blank for all rows.  */  
   whereClause:string,
      /**  The maximum number of rows to return. Leave as zero for no maximum.  */  
   pageSize:number,
      /**  Page of rows to return.  */  
   absolutePage:number,
}

export interface GetListCurrentCompany_output{
   returnObj:Erp_Tablesets_AutoTranReversalListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClause
      @param pageSize
      @param absolutePage
      @param NO_COMPANY
   */  
export interface GetList_input{
      /**  An expression used to filter the rows. Can be left blank for all rows.  */  
   whereClause:string,
      /**  The maximum number of rows to return. Leave as zero for no maximum.  */  
   pageSize:number,
      /**  Page of rows to return.  */  
   absolutePage:number,
      /**  Is company in the where clause.  */  
   NO_COMPANY:string,
}

export interface GetList_output{
   returnObj:Erp_Tablesets_AutoTranReversalListTableset[],
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

   /** Required : 
      @param ipAmtStatToReverse
      @param ds
   */  
export interface OnChangeAmtStatToReverseRowMod_input{
   ipAmtStatToReverse:number,
   ds:Erp_Tablesets_AutoTranReversalTableset[],
}

export interface OnChangeAmtStatToReverseRowMod_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AutoTranReversalTableset[],
}
}

   /** Required : 
      @param ipAmtStatToReverse
      @param ds
   */  
export interface OnChangeAmtStatToReverse_input{
   ipAmtStatToReverse:number,
   ds:Erp_Tablesets_AutoTranReversalTableset[],
}

export interface OnChangeAmtStatToReverse_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AutoTranReversalTableset[],
}
}

   /** Required : 
      @param ipAmtToReverse
      @param ds
   */  
export interface OnChangeAmtToReverseRowMod_input{
   ipAmtToReverse:number,
   ds:Erp_Tablesets_AutoTranReversalTableset[],
}

export interface OnChangeAmtToReverseRowMod_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AutoTranReversalTableset[],
}
}

   /** Required : 
      @param ipAmtToReverse
      @param ds
   */  
export interface OnChangeAmtToReverse_input{
   ipAmtToReverse:number,
   ds:Erp_Tablesets_AutoTranReversalTableset[],
}

export interface OnChangeAmtToReverse_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AutoTranReversalTableset[],
}
}

   /** Required : 
      @param ipSelected
      @param ds
   */  
export interface OnChangeSelectedRowMod_input{
   ipSelected:boolean,
   ds:Erp_Tablesets_AutoTranReversalTableset[],
}

export interface OnChangeSelectedRowMod_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AutoTranReversalTableset[],
}
}

   /** Required : 
      @param ipSelected
      @param ds
   */  
export interface OnChangeSelected_input{
   ipSelected:boolean,
   ds:Erp_Tablesets_AutoTranReversalTableset[],
}

export interface OnChangeSelected_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AutoTranReversalTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface Post_input{
   ds:Erp_Tablesets_AutoTranReversalTableset[],
}

export interface Post_output{
parameters : {
      /**  output parameters  */  
   outErrorMessage:string,
}
}

