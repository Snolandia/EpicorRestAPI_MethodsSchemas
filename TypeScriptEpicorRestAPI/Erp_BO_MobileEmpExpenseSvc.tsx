import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.MobileEmpExpenseSvc
// Description: Mobile Employee Expense Business Object
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileEmpExpenseSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileEmpExpenseSvc/$metadata", {
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

   /**  
   Summary: Calls GetRows for the service
   Description: Get MobileEmpExpenses items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_MobileEmpExpenses
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MobileEmpExpenseRow
   */  
export function get_MobileEmpExpenses(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MobileEmpExpenseRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileEmpExpenseSvc/MobileEmpExpenses", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MobileEmpExpenseRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_MobileEmpExpenses
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.MobileEmpExpenseRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.MobileEmpExpenseRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MobileEmpExpenses(requestBody:Erp_Tablesets_MobileEmpExpenseRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileEmpExpenseSvc/MobileEmpExpenses", {
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
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the MobileEmpExpense item
   Description: Calls GetByID to retrieve the MobileEmpExpense item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MobileEmpExpense
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EmpID Desc: EmpID   Required: True   Allow empty value : True
      @param EmpExpenseNum Desc: EmpExpenseNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.MobileEmpExpenseRow
   */  
export function get_MobileEmpExpenses_Company_EmpID_EmpExpenseNum(Company:string, EmpID:string, EmpExpenseNum:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_MobileEmpExpenseRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileEmpExpenseSvc/MobileEmpExpenses(" + Company + "," + EmpID + "," + EmpExpenseNum + ")", {
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
         resolve(data as Erp_Tablesets_MobileEmpExpenseRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update MobileEmpExpense for the service
   Description: Calls UpdateExt to update MobileEmpExpense. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_MobileEmpExpense
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EmpID Desc: EmpID   Required: True   Allow empty value : True
      @param EmpExpenseNum Desc: EmpExpenseNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.MobileEmpExpenseRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_MobileEmpExpenses_Company_EmpID_EmpExpenseNum(Company:string, EmpID:string, EmpExpenseNum:string, requestBody:Erp_Tablesets_MobileEmpExpenseRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileEmpExpenseSvc/MobileEmpExpenses(" + Company + "," + EmpID + "," + EmpExpenseNum + ")", {
          method: 'patch',
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
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Call UpdateExt to delete MobileEmpExpense item
   Description: Call UpdateExt to delete MobileEmpExpense item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_MobileEmpExpense
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EmpID Desc: EmpID   Required: True   Allow empty value : True
      @param EmpExpenseNum Desc: EmpExpenseNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_MobileEmpExpenses_Company_EmpID_EmpExpenseNum(Company:string, EmpID:string, EmpExpenseNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileEmpExpenseSvc/MobileEmpExpenses(" + Company + "," + EmpID + "," + EmpExpenseNum + ")", {
          method: 'delete',
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

   /**  
   Summary: Calls GetByID for the service
   Description: Get MobileEmpExpenseComments items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_MobileEmpExpenseComments1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EmpID Desc: EmpID   Required: True   Allow empty value : True
      @param EmpExpenseNum Desc: EmpExpenseNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MobileEmpExpenseCommentRow
   */  
export function get_MobileEmpExpenses_Company_EmpID_EmpExpenseNum_MobileEmpExpenseComments(Company:string, EmpID:string, EmpExpenseNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MobileEmpExpenseCommentRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileEmpExpenseSvc/MobileEmpExpenses(" + Company + "," + EmpID + "," + EmpExpenseNum + ")/MobileEmpExpenseComments", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MobileEmpExpenseCommentRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the MobileEmpExpenseComment item
   Description: Calls GetByID to retrieve the MobileEmpExpenseComment item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MobileEmpExpenseComment1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EmpID Desc: EmpID   Required: True   Allow empty value : True
      @param EmpExpenseNum Desc: EmpExpenseNum   Required: True
      @param CommentNum Desc: CommentNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.MobileEmpExpenseCommentRow
   */  
export function get_MobileEmpExpenses_Company_EmpID_EmpExpenseNum_MobileEmpExpenseComments_Company_EmpID_EmpExpenseNum_CommentNum(Company:string, EmpID:string, EmpExpenseNum:string, CommentNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_MobileEmpExpenseCommentRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileEmpExpenseSvc/MobileEmpExpenses(" + Company + "," + EmpID + "," + EmpExpenseNum + ")/MobileEmpExpenseComments(" + Company + "," + EmpID + "," + EmpExpenseNum + "," + CommentNum + ")", {
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
         resolve(data as Erp_Tablesets_MobileEmpExpenseCommentRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get MobileEmpExpenseAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_MobileEmpExpenseAttches1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EmpID Desc: EmpID   Required: True   Allow empty value : True
      @param EmpExpenseNum Desc: EmpExpenseNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MobileEmpExpenseAttchRow
   */  
export function get_MobileEmpExpenses_Company_EmpID_EmpExpenseNum_MobileEmpExpenseAttches(Company:string, EmpID:string, EmpExpenseNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MobileEmpExpenseAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileEmpExpenseSvc/MobileEmpExpenses(" + Company + "," + EmpID + "," + EmpExpenseNum + ")/MobileEmpExpenseAttches", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MobileEmpExpenseAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the MobileEmpExpenseAttch item
   Description: Calls GetByID to retrieve the MobileEmpExpenseAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MobileEmpExpenseAttch1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EmpID Desc: EmpID   Required: True   Allow empty value : True
      @param EmpExpenseNum Desc: EmpExpenseNum   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.MobileEmpExpenseAttchRow
   */  
export function get_MobileEmpExpenses_Company_EmpID_EmpExpenseNum_MobileEmpExpenseAttches_Company_EmpID_EmpExpenseNum_DrawingSeq(Company:string, EmpID:string, EmpExpenseNum:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_MobileEmpExpenseAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileEmpExpenseSvc/MobileEmpExpenses(" + Company + "," + EmpID + "," + EmpExpenseNum + ")/MobileEmpExpenseAttches(" + Company + "," + EmpID + "," + EmpExpenseNum + "," + DrawingSeq + ")", {
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
         resolve(data as Erp_Tablesets_MobileEmpExpenseAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get MobileEmpExpenseComments items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_MobileEmpExpenseComments
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MobileEmpExpenseCommentRow
   */  
export function get_MobileEmpExpenseComments(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MobileEmpExpenseCommentRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileEmpExpenseSvc/MobileEmpExpenseComments", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MobileEmpExpenseCommentRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_MobileEmpExpenseComments
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.MobileEmpExpenseCommentRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.MobileEmpExpenseCommentRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MobileEmpExpenseComments(requestBody:Erp_Tablesets_MobileEmpExpenseCommentRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileEmpExpenseSvc/MobileEmpExpenseComments", {
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
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the MobileEmpExpenseComment item
   Description: Calls GetByID to retrieve the MobileEmpExpenseComment item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MobileEmpExpenseComment
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EmpID Desc: EmpID   Required: True   Allow empty value : True
      @param EmpExpenseNum Desc: EmpExpenseNum   Required: True
      @param CommentNum Desc: CommentNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.MobileEmpExpenseCommentRow
   */  
export function get_MobileEmpExpenseComments_Company_EmpID_EmpExpenseNum_CommentNum(Company:string, EmpID:string, EmpExpenseNum:string, CommentNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_MobileEmpExpenseCommentRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileEmpExpenseSvc/MobileEmpExpenseComments(" + Company + "," + EmpID + "," + EmpExpenseNum + "," + CommentNum + ")", {
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
         resolve(data as Erp_Tablesets_MobileEmpExpenseCommentRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update MobileEmpExpenseComment for the service
   Description: Calls UpdateExt to update MobileEmpExpenseComment. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_MobileEmpExpenseComment
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EmpID Desc: EmpID   Required: True   Allow empty value : True
      @param EmpExpenseNum Desc: EmpExpenseNum   Required: True
      @param CommentNum Desc: CommentNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.MobileEmpExpenseCommentRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_MobileEmpExpenseComments_Company_EmpID_EmpExpenseNum_CommentNum(Company:string, EmpID:string, EmpExpenseNum:string, CommentNum:string, requestBody:Erp_Tablesets_MobileEmpExpenseCommentRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileEmpExpenseSvc/MobileEmpExpenseComments(" + Company + "," + EmpID + "," + EmpExpenseNum + "," + CommentNum + ")", {
          method: 'patch',
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
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Call UpdateExt to delete MobileEmpExpenseComment item
   Description: Call UpdateExt to delete MobileEmpExpenseComment item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_MobileEmpExpenseComment
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EmpID Desc: EmpID   Required: True   Allow empty value : True
      @param EmpExpenseNum Desc: EmpExpenseNum   Required: True
      @param CommentNum Desc: CommentNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_MobileEmpExpenseComments_Company_EmpID_EmpExpenseNum_CommentNum(Company:string, EmpID:string, EmpExpenseNum:string, CommentNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileEmpExpenseSvc/MobileEmpExpenseComments(" + Company + "," + EmpID + "," + EmpExpenseNum + "," + CommentNum + ")", {
          method: 'delete',
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

   /**  
   Summary: Calls GetRows for the service
   Description: Get MobileEmpExpenseAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_MobileEmpExpenseAttches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MobileEmpExpenseAttchRow
   */  
export function get_MobileEmpExpenseAttches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MobileEmpExpenseAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileEmpExpenseSvc/MobileEmpExpenseAttches", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MobileEmpExpenseAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_MobileEmpExpenseAttches
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.MobileEmpExpenseAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.MobileEmpExpenseAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MobileEmpExpenseAttches(requestBody:Erp_Tablesets_MobileEmpExpenseAttchRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileEmpExpenseSvc/MobileEmpExpenseAttches", {
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
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the MobileEmpExpenseAttch item
   Description: Calls GetByID to retrieve the MobileEmpExpenseAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MobileEmpExpenseAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EmpID Desc: EmpID   Required: True   Allow empty value : True
      @param EmpExpenseNum Desc: EmpExpenseNum   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.MobileEmpExpenseAttchRow
   */  
export function get_MobileEmpExpenseAttches_Company_EmpID_EmpExpenseNum_DrawingSeq(Company:string, EmpID:string, EmpExpenseNum:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_MobileEmpExpenseAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileEmpExpenseSvc/MobileEmpExpenseAttches(" + Company + "," + EmpID + "," + EmpExpenseNum + "," + DrawingSeq + ")", {
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
         resolve(data as Erp_Tablesets_MobileEmpExpenseAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update MobileEmpExpenseAttch for the service
   Description: Calls UpdateExt to update MobileEmpExpenseAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_MobileEmpExpenseAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EmpID Desc: EmpID   Required: True   Allow empty value : True
      @param EmpExpenseNum Desc: EmpExpenseNum   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.MobileEmpExpenseAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_MobileEmpExpenseAttches_Company_EmpID_EmpExpenseNum_DrawingSeq(Company:string, EmpID:string, EmpExpenseNum:string, DrawingSeq:string, requestBody:Erp_Tablesets_MobileEmpExpenseAttchRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileEmpExpenseSvc/MobileEmpExpenseAttches(" + Company + "," + EmpID + "," + EmpExpenseNum + "," + DrawingSeq + ")", {
          method: 'patch',
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
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Call UpdateExt to delete MobileEmpExpenseAttch item
   Description: Call UpdateExt to delete MobileEmpExpenseAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_MobileEmpExpenseAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EmpID Desc: EmpID   Required: True   Allow empty value : True
      @param EmpExpenseNum Desc: EmpExpenseNum   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_MobileEmpExpenseAttches_Company_EmpID_EmpExpenseNum_DrawingSeq(Company:string, EmpID:string, EmpExpenseNum:string, DrawingSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileEmpExpenseSvc/MobileEmpExpenseAttches(" + Company + "," + EmpID + "," + EmpExpenseNum + "," + DrawingSeq + ")", {
          method: 'delete',
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

   /**  
   Summary: Calls GetRows for the service
   Description: Get MobileApproverLists items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_MobileApproverLists
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MobileApproverListRow
   */  
export function get_MobileApproverLists(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MobileApproverListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileEmpExpenseSvc/MobileApproverLists", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MobileApproverListRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_MobileApproverLists
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.MobileApproverListRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.MobileApproverListRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MobileApproverLists(requestBody:Erp_Tablesets_MobileApproverListRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileEmpExpenseSvc/MobileApproverLists", {
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
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the MobileApproverList item
   Description: Calls GetByID to retrieve the MobileApproverList item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MobileApproverList
      @param SysRowID Desc: SysRowID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.MobileApproverListRow
   */  
export function get_MobileApproverLists_SysRowID(SysRowID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_MobileApproverListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileEmpExpenseSvc/MobileApproverLists(" + SysRowID + ")", {
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
         resolve(data as Erp_Tablesets_MobileApproverListRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update MobileApproverList for the service
   Description: Calls UpdateExt to update MobileApproverList. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_MobileApproverList
      @param SysRowID Desc: SysRowID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.MobileApproverListRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_MobileApproverLists_SysRowID(SysRowID:string, requestBody:Erp_Tablesets_MobileApproverListRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileEmpExpenseSvc/MobileApproverLists(" + SysRowID + ")", {
          method: 'patch',
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
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Call UpdateExt to delete MobileApproverList item
   Description: Call UpdateExt to delete MobileApproverList item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_MobileApproverList
      @param SysRowID Desc: SysRowID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_MobileApproverLists_SysRowID(SysRowID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileEmpExpenseSvc/MobileApproverLists(" + SysRowID + ")", {
          method: 'delete',
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MobileEmpExpenseListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MobileEmpExpenseListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileEmpExpenseSvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MobileEmpExpenseListRow)
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
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True
   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClauseMobileEmpExpense:string, whereClauseMobileEmpExpenseAttch:string, whereClauseMobileEmpExpenseComment:string, whereClauseMobileApproverList:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseMobileEmpExpense!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseMobileEmpExpense=" + whereClauseMobileEmpExpense
   }
   if(typeof whereClauseMobileEmpExpenseAttch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseMobileEmpExpenseAttch=" + whereClauseMobileEmpExpenseAttch
   }
   if(typeof whereClauseMobileEmpExpenseComment!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseMobileEmpExpenseComment=" + whereClauseMobileEmpExpenseComment
   }
   if(typeof whereClauseMobileApproverList!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseMobileApproverList=" + whereClauseMobileApproverList
   }
   if(typeof pageSize!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "pageSize=" + pageSize
   }
   if(typeof absolutePage!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "absolutePage=" + absolutePage
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetRows_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileEmpExpenseSvc/GetRows" + params, {
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
         resolve(data as GetRows_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(empID:string, empExpenseNum:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof empID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "empID=" + empID
   }
   if(typeof empExpenseNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "empExpenseNum=" + empExpenseNum
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileEmpExpenseSvc/GetByID" + params, {
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
         resolve(data as GetByID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetList
   Description: Returns a list of rows that satisfy the where clause.
   OperationID: Get_GetList
      @param whereClause Desc: An expression used to filter the rows. Can be left blank for all rows.   Required: True   Allow empty value : True
      @param pageSize Desc: The maximum number of rows to return. Leave as zero for no maximum.   Required: True
      @param absolutePage Desc: Page of rows to return.   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetList(whereClause:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClause!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClause=" + whereClause
   }
   if(typeof pageSize!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "pageSize=" + pageSize
   }
   if(typeof absolutePage!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "absolutePage=" + absolutePage
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileEmpExpenseSvc/GetList" + params, {
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
         resolve(data as GetList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetMobileEmpExpenseAttchs
   Description: Custom Method to retrieve only the MobileEmpExpenseAttch records for the current expense
   OperationID: GetMobileEmpExpenseAttchs
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetMobileEmpExpenseAttchs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetMobileEmpExpenseAttchs_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetMobileEmpExpenseAttchs(requestBody:GetMobileEmpExpenseAttchs_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetMobileEmpExpenseAttchs_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileEmpExpenseSvc/GetMobileEmpExpenseAttchs", {
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
         resolve(data as GetMobileEmpExpenseAttchs_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetMobileEmpExpenseComments
   Description: Custom Method to retrieve only the MobileEmpExpenseComment records for the current expense
   OperationID: GetMobileEmpExpenseComments
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetMobileEmpExpenseComments_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetMobileEmpExpenseComments_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetMobileEmpExpenseComments(requestBody:GetMobileEmpExpenseComments_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetMobileEmpExpenseComments_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileEmpExpenseSvc/GetMobileEmpExpenseComments", {
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
         resolve(data as GetMobileEmpExpenseComments_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method MobileGetApprovalStatus
   Description: Populates the MobileApproverList Temp Table with the current expense's approver data.
   OperationID: MobileGetApprovalStatus
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/MobileGetApprovalStatus_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MobileGetApprovalStatus_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MobileGetApprovalStatus(requestBody:MobileGetApprovalStatus_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<MobileGetApprovalStatus_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileEmpExpenseSvc/MobileGetApprovalStatus", {
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
         resolve(data as MobileGetApprovalStatus_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method MobileGetByID
   Description: GetByID method
   OperationID: MobileGetByID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/MobileGetByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MobileGetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MobileGetByID(requestBody:MobileGetByID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<MobileGetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileEmpExpenseSvc/MobileGetByID", {
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
         resolve(data as MobileGetByID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method MobileGetRows
   Description: Returns MobileEmpExpense dataset containing all rows that satisfy the where clauses
   OperationID: MobileGetRows
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/MobileGetRows_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MobileGetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MobileGetRows(requestBody:MobileGetRows_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<MobileGetRows_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileEmpExpenseSvc/MobileGetRows", {
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
         resolve(data as MobileGetRows_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method MobileGetRowsApprover
   Description: Retrieves all approver expenses to be approved / rejected / recalled from approval.
   OperationID: MobileGetRowsApprover
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/MobileGetRowsApprover_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MobileGetRowsApprover_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MobileGetRowsApprover(requestBody:MobileGetRowsApprover_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<MobileGetRowsApprover_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileEmpExpenseSvc/MobileGetRowsApprover", {
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
         resolve(data as MobileGetRowsApprover_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method MobileGetList
   Description: Get List method
   OperationID: MobileGetList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/MobileGetList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MobileGetList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MobileGetList(requestBody:MobileGetList_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<MobileGetList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileEmpExpenseSvc/MobileGetList", {
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
         resolve(data as MobileGetList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetHomePageData
   OperationID: GetHomePageData
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetHomePageData_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetHomePageData_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetHomePageData(requestBody:GetHomePageData_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetHomePageData_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileEmpExpenseSvc/GetHomePageData", {
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
         resolve(data as GetHomePageData_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method MobileGetNewEmpExpense
   Description: Create a new mobile EmpExpense dataset row
   OperationID: MobileGetNewEmpExpense
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/MobileGetNewEmpExpense_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MobileGetNewEmpExpense_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MobileGetNewEmpExpense(requestBody:MobileGetNewEmpExpense_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<MobileGetNewEmpExpense_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileEmpExpenseSvc/MobileGetNewEmpExpense", {
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
         resolve(data as MobileGetNewEmpExpense_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method MobileGetNewEmpExpenseAttch
   Description: Create a new mobile EmpExpense dataset attachment row
   OperationID: MobileGetNewEmpExpenseAttch
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/MobileGetNewEmpExpenseAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MobileGetNewEmpExpenseAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MobileGetNewEmpExpenseAttch(requestBody:MobileGetNewEmpExpenseAttch_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<MobileGetNewEmpExpenseAttch_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileEmpExpenseSvc/MobileGetNewEmpExpenseAttch", {
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
         resolve(data as MobileGetNewEmpExpenseAttch_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method MobileGetNewEmpExpenseComment
   Description: Create a new mobile EmpExpense dataset comment row
   OperationID: MobileGetNewEmpExpenseComment
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/MobileGetNewEmpExpenseComment_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MobileGetNewEmpExpenseComment_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MobileGetNewEmpExpenseComment(requestBody:MobileGetNewEmpExpenseComment_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<MobileGetNewEmpExpenseComment_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileEmpExpenseSvc/MobileGetNewEmpExpenseComment", {
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
         resolve(data as MobileGetNewEmpExpenseComment_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method MobileDelete
   Description: Method to call to delete expense records
   OperationID: MobileDelete
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/MobileDelete_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MobileDelete_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MobileDelete(requestBody:MobileDelete_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<MobileDelete_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileEmpExpenseSvc/MobileDelete", {
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
         resolve(data as MobileDelete_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method MobileSync
   Description: Method to call to synchronize draft records to the database
   OperationID: MobileSync
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/MobileSync_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MobileSync_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MobileSync(requestBody:MobileSync_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<MobileSync_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileEmpExpenseSvc/MobileSync", {
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
         resolve(data as MobileSync_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method MobileSyncSuccessful
   Description: Receives the fields needed to find and delete the validation record created when synchronization is successful
   OperationID: MobileSyncSuccessful
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/MobileSyncSuccessful_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MobileSyncSuccessful_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MobileSyncSuccessful(requestBody:MobileSyncSuccessful_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<MobileSyncSuccessful_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileEmpExpenseSvc/MobileSyncSuccessful", {
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
         resolve(data as MobileSyncSuccessful_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method MobileAttachmentUpdate
   Description: Method to call to update attachment record and upload file to the storage defined by document type (or default company storage)
   OperationID: MobileAttachmentUpdate
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/MobileAttachmentUpdate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MobileAttachmentUpdate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MobileAttachmentUpdate(requestBody:MobileAttachmentUpdate_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<MobileAttachmentUpdate_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileEmpExpenseSvc/MobileAttachmentUpdate", {
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
         resolve(data as MobileAttachmentUpdate_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method MobileUpdate
   Description: Method to call to update the table set
   OperationID: MobileUpdate
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/MobileUpdate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MobileUpdate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MobileUpdate(requestBody:MobileUpdate_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<MobileUpdate_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileEmpExpenseSvc/MobileUpdate", {
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
         resolve(data as MobileUpdate_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetVersion
   Description: Returns BO Version
   OperationID: GetVersion
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetVersion_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetVersion(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetVersion_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileEmpExpenseSvc/GetVersion", {
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
         resolve(data as GetVersion_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method RecallEmpExpense
   Description: Method to call when recalling submitted expense records
   OperationID: RecallEmpExpense
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/RecallEmpExpense_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RecallEmpExpense_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RecallEmpExpense(requestBody:RecallEmpExpense_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<RecallEmpExpense_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileEmpExpenseSvc/RecallEmpExpense", {
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
         resolve(data as RecallEmpExpense_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SubmitSelected
   Description: Method to call to submit selected expenses
   OperationID: SubmitSelected
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/SubmitSelected_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SubmitSelected_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SubmitSelected(requestBody:SubmitSelected_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<SubmitSelected_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileEmpExpenseSvc/SubmitSelected", {
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
         resolve(data as SubmitSelected_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckRecallFromApproval
   Description: The procedure is called prior to performing a recall.  It will check
if subsequent approvals have occurred.  If they have the user
will have the opportunity to cancel the recall.
   OperationID: CheckRecallFromApproval
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckRecallFromApproval_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckRecallFromApproval_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckRecallFromApproval(requestBody:CheckRecallFromApproval_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckRecallFromApproval_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileEmpExpenseSvc/CheckRecallFromApproval", {
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
         resolve(data as CheckRecallFromApproval_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method RecallFromApproval
   Description: Method to call when recalling from approval entry
   OperationID: RecallFromApproval
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/RecallFromApproval_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RecallFromApproval_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RecallFromApproval(requestBody:RecallFromApproval_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<RecallFromApproval_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileEmpExpenseSvc/RecallFromApproval", {
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
         resolve(data as RecallFromApproval_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ApproveReject
   Description: The procedure is called when the user selects EmpExpense records for reject or approve
   OperationID: ApproveReject
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ApproveReject_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ApproveReject_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ApproveReject(requestBody:ApproveReject_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ApproveReject_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileEmpExpenseSvc/ApproveReject", {
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
         resolve(data as ApproveReject_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CopyEmpExpense
   Description: Method to copy the vales from one EmpExpense record to a new EmpExpense record.
   OperationID: CopyEmpExpense
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CopyEmpExpense_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CopyEmpExpense_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CopyEmpExpense(requestBody:CopyEmpExpense_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CopyEmpExpense_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileEmpExpenseSvc/CopyEmpExpense", {
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
         resolve(data as CopyEmpExpense_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewMobileEmpExpense
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewMobileEmpExpense
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewMobileEmpExpense_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewMobileEmpExpense_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewMobileEmpExpense(requestBody:GetNewMobileEmpExpense_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewMobileEmpExpense_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileEmpExpenseSvc/GetNewMobileEmpExpense", {
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
         resolve(data as GetNewMobileEmpExpense_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewMobileEmpExpenseAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewMobileEmpExpenseAttch
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewMobileEmpExpenseAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewMobileEmpExpenseAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewMobileEmpExpenseAttch(requestBody:GetNewMobileEmpExpenseAttch_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewMobileEmpExpenseAttch_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileEmpExpenseSvc/GetNewMobileEmpExpenseAttch", {
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
         resolve(data as GetNewMobileEmpExpenseAttch_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewMobileEmpExpenseComment
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewMobileEmpExpenseComment
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewMobileEmpExpenseComment_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewMobileEmpExpenseComment_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewMobileEmpExpenseComment(requestBody:GetNewMobileEmpExpenseComment_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewMobileEmpExpenseComment_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileEmpExpenseSvc/GetNewMobileEmpExpenseComment", {
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
         resolve(data as GetNewMobileEmpExpenseComment_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DeleteByID
   Description: Deletes a row given its ID.
   OperationID: DeleteByID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DeleteByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteByID(requestBody:DeleteByID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DeleteByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileEmpExpenseSvc/DeleteByID", {
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
         resolve(data as DeleteByID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetBySysRowID
   OperationID: Get_GetBySysRowID
   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBySysRowID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetBySysRowID(id:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof id!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "id=" + id
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetBySysRowID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileEmpExpenseSvc/GetBySysRowID" + params, {
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
         resolve(data as GetBySysRowID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetBySysRowIDs
   OperationID: Get_GetBySysRowIDs
   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBySysRowIDs_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetBySysRowIDs(ids:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof ids!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "ids=" + ids
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetBySysRowIDs_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileEmpExpenseSvc/GetBySysRowIDs" + params, {
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
         resolve(data as GetBySysRowIDs_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method Update
   Description: Commits the DataSet changes to the data store.
   OperationID: Update
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/Update_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Update_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_Update(requestBody:Update_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Update_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileEmpExpenseSvc/Update", {
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
         resolve(data as Update_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UpdateExt
   Description: Apply input data to service by calling GetByID/GetNew/Update methods.
   OperationID: UpdateExt
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/UpdateExt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateExt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateExt(requestBody:UpdateExt_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<UpdateExt_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileEmpExpenseSvc/UpdateExt", {
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
         resolve(data as UpdateExt_output)
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MobileApproverListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_MobileApproverListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MobileEmpExpenseAttchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_MobileEmpExpenseAttchRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MobileEmpExpenseCommentRow{
   "odatametadata":string,
   "value":Erp_Tablesets_MobileEmpExpenseCommentRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MobileEmpExpenseListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_MobileEmpExpenseListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MobileEmpExpenseRow{
   "odatametadata":string,
   "value":Erp_Tablesets_MobileEmpExpenseRow,
}

export interface Erp_Tablesets_MobileApproverListRow{
      /**  The status of the current approval task.  */  
   "ApprovalStatus":string,
      /**  Company Identifier.  */  
   "Company":string,
      /**  Date when the approval task was completed.  */  
   "CompleteDate":string,
      /**  Major component of the foreign key of the related master record. For a task related to an Expense this field would contain the related EmployeeID. For a task related to Labor this field would contain the related LaborHed.  */  
   "Key1":string,
      /**  Second component of the foreign key to the related master record. For a task related to an Expense, this field would contain the related ExpenseID. For a task related to Labor, this field would contain the related LaborDtl.  */  
   "Key2":string,
      /**  The master file to which the task is related.  */  
   "RelatedToFile":string,
      /**  The SalesRep that this task is assigned to.  */  
   "SalesRepCode":string,
      /**  Name corresponding to the SalesRepCode.  */  
   "SalesRepName":string,
      /**  Number used to display the records in their correct sequence in the mobile app.  */  
   "SequenceNum":number,
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_MobileEmpExpenseAttchRow{
   "Company":string,
   "EmpID":string,
   "EmpExpenseNum":number,
   "DrawingSeq":number,
   "XFileRefNum":number,
   "SysRevID":number,
   "SysRowID":string,
   "ForeignSysRowID":string,
   "DrawDesc":string,
   "FileName":string,
   "PDMDocID":string,
   "DocTypeID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_MobileEmpExpenseCommentRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The employee the expense comment record is for.  */  
   "EmpID":string,
      /**  Internal identifier of the EmpExpense record.  This with EmpID links the comment to a specific EmpExpense record.  */  
   "EmpExpenseNum":number,
      /**  Internal identifier of the comment record.  Used in conjunction with EmpExpenseNum to make the record unique.  */  
   "CommentNum":number,
      /**   The comment type of this record.  Values are:
"SUB" Submit
"APP" Approve
"REJ" Reject  */  
   "CommentType":string,
      /**  The comment text.  */  
   "CommentText":string,
      /**  Userid of the user who created the record.  */  
   "CreatedBy":string,
      /**  The date the record was created.  */  
   "CreateDate":string,
      /**  The time the record was created (in seconds since midnight)  */  
   "CreateTime":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_MobileEmpExpenseListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The employee the expense record is for.  */  
   "EmpID":string,
      /**  Internal identifier of the EmpExpense record.  This with EmpID makes the record unique.  */  
   "EmpExpenseNum":number,
      /**  The date of the expense.  */  
   "ExpenseDate":string,
      /**  Brief description of the expense.  Can be used to group expense entries together, for example, all time entries incurred on the same trip can be assigned the same reference.  */  
   "ClaimRef":string,
      /**  Quick entry code.  Reference to the QuickEntry table.  Can be used to default information into the expense record.  */  
   "QuickEntryCode":string,
      /**  Indicates if the expense is related to a project.  A value of true indicates the record is not related to a project.  */  
   "Indirect":boolean,
      /**  The project the expense is related to.  */  
   "ProjectID":string,
      /**  The project phase the expense is related to.  */  
   "PhaseID":string,
      /**  The payment method of the expense.  */  
   "PMUID":number,
      /**  The number of units of this expense.  */  
   "Units":number,
      /**  Rate per unit of the expense.  */  
   "UnitRate":number,
      /**  The currency the expense occurred in.  */  
   "ExpCurrencyCode":string,
      /**  The Tax Region for this expense.  */  
   "TaxRegionCode":string,
      /**  The tax of the expense in the expense currency.  */  
   "DocExpenseTaxAmt":number,
      /**  The amount of the expense in the expense currency.  */  
   "DocExpenseAmt":number,
      /**  Indicates if the expense amount includes tax.  */  
   "TaxIncluded":boolean,
      /**   The status of the expense.  Values are:
Blank
E - Entered
S - Submitted
P - Partially Approved
A - Approved
R - Rejected  */  
   "ExpenseStatus":string,
      /**  The date the expense received final approval.  */  
   "ApprovedDate":string,
      /**  The miscellaneous charge code for this expense.  */  
   "MiscCode":string,
      /**  The user who submitted the expense  */  
   "SubmittedBy":string,
      /**  Indicates if approval is required for this transaction.  */  
   "ApprovalRequired":boolean,
      /**  Indicates if the record is tax exempt.  If field is non-blank it is considered exempt.  */  
   "TaxExempt":string,
      /**  Indicates if the expense is reimbursable.  */  
   "Reimbursable":boolean,
      /**  The expense category.  */  
   "ExpenseCategory":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_MobileEmpExpenseRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The employee the expense record is for.  */  
   "EmpID":string,
      /**  Internal identifier of the EmpExpense record.  This with EmpID makes the record unique.  */  
   "EmpExpenseNum":number,
      /**  The date of the expense.  */  
   "ExpenseDate":string,
      /**  Brief description of the expense.  Can be used to group expense entries together, for example, all time entries incurred on the same trip can be assigned the same reference.  */  
   "ClaimRef":string,
      /**  Quick entry code.  Reference to the QuickEntry table.  Can be used to default information into the expense record.  */  
   "QuickEntryCode":string,
      /**  Indicates if the expense is related to a project.  A value of true indicates the record is not related to a project.  */  
   "Indirect":boolean,
      /**  The project the expense is related to.  */  
   "ProjectID":string,
      /**  The project phase the expense is related to.  */  
   "PhaseID":string,
      /**  The payment method of the expense.  */  
   "PMUID":number,
      /**  The number of units of this expense.  */  
   "Units":number,
      /**  Rate per unit of the expense.  */  
   "UnitRate":number,
      /**  The currency the expense occurred in.  */  
   "ExpCurrencyCode":string,
      /**  The Tax Region for this expense.  */  
   "TaxRegionCode":string,
      /**  The amount of the expense in the expense currency.  */  
   "DocExpenseAmt":number,
      /**  Indicates if the expense amount includes tax.  */  
   "TaxIncluded":boolean,
      /**  The total amount of the expense in the expense currency.  This value includes taxes.  */  
   "DocTotalExpenseAmt":number,
      /**   The status of the expense.  Values are:
Blank
E - Entered
S - Submitted
P - Partially Approved
A - Approved
R - Rejected  */  
   "ExpenseStatus":string,
      /**  The date the expense received final approval.  */  
   "ApprovedDate":string,
      /**  The currency the claim amounts are in.  */  
   "ClaimCurrencyCode":string,
      /**  The miscellaneous charge code for this expense.  */  
   "MiscCode":string,
      /**  The user who submitted the expense  */  
   "SubmittedBy":string,
      /**  Indicates if approval is required for this transaction.  */  
   "ApprovalRequired":boolean,
      /**  Indicates if the record is tax exempt.  If field is non-blank it is considered exempt.  */  
   "TaxExempt":string,
      /**  Indicates if the expense is reimbursable.  */  
   "Reimbursable":boolean,
      /**  Expense Comment  */  
   "ExpCommentText":string,
      /**  Expense Comment Instruction  */  
   "ExpCommentInstr":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  External field to display a descriptive status of the record  */  
   "DisplayStatus":string,
      /**  Indicates if the copy button is enabled  */  
   "EnableCopy":boolean,
      /**  Indicates if the recall button is enabled  */  
   "EnableRecall":boolean,
      /**  Indicates if recall is available in approval entry  */  
   "EnableRecallAprv":boolean,
      /**  Indicates if the submit button is enabled  */  
   "EnableSubmit":boolean,
   "ExpenseDisableDelete":boolean,
   "ExpenseDisableUpdate":boolean,
      /**  Indicates if the expense detail has attachments  */  
   "HasAttachments":boolean,
      /**  Indicates if the expense detail has comments  */  
   "HasComments":boolean,
      /**  Indicates if UnitRate is enabled  */  
   "EnableUnitRate":boolean,
   "SalesRepCode":string,
      /**  MobileGetApprovalStatus  */  
   "ApprovedBy":string,
      /**  A list of people who need to approve the expense.  */  
   "PendingApprovalBy":string,
   "BitFlag":number,
   "EmpBasicName":string,
   "ExpCurrencyCurrSymbol":string,
   "ExpCurrencyDocumentDesc":string,
   "ExpCurrencyCurrName":string,
   "ExpCurrencyCurrDesc":string,
   "ExpCurrencyCurrencyID":string,
   "PayMethodReimbursable":boolean,
   "PayMethodSummarizePerCustomer":boolean,
   "PayMethodName":string,
   "PayMethodType":number,
   "ProjectDescription":string,
   "ProjPhaseDescription":string,
   "PurMiscDescription":string,
   "PurMiscExpUnitBased":boolean,
   "TaxRgnDescription":string,
      /**  RowMod  */  
   "RowMod":string,
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
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param salesRepCode
      @param action
      @param comment
      @param ds
   */  
export interface ApproveReject_input{
      /**  The sales Rep Code of the approver.  */  
   salesRepCode:string,
      /**  Action to take A = approver, R = reject.  */  
   action:string,
      /**  Comment text if comments are to be created.  */  
   comment:string,
   ds:Erp_Tablesets_MobileEmpExpenseTableset[],
}

export interface ApproveReject_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MobileEmpExpenseTableset,
   outMessage:string,
}
}

   /** Required : 
      @param salesRepCode
      @param ds
   */  
export interface CheckRecallFromApproval_input{
      /**  The sales Rep Code of the approver.  */  
   salesRepCode:string,
   ds:Erp_Tablesets_MobileEmpExpenseTableset[],
}

export interface CheckRecallFromApproval_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MobileEmpExpenseTableset,
   outRecallMsg:string,
}
}

   /** Required : 
      @param ds
   */  
export interface CopyEmpExpense_input{
   ds:Erp_Tablesets_MobileEmpExpenseTableset[],
}

export interface CopyEmpExpense_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MobileEmpExpenseTableset,
   messageText:string,
}
}

   /** Required : 
      @param empID
      @param empExpenseNum
   */  
export interface DeleteByID_input{
   empID:string,
   empExpenseNum:number,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_MobileApproverListRow{
      /**  The status of the current approval task.  */  
   ApprovalStatus:string,
      /**  Company Identifier.  */  
   Company:string,
      /**  Date when the approval task was completed.  */  
   CompleteDate:string,
      /**  Major component of the foreign key of the related master record. For a task related to an Expense this field would contain the related EmployeeID. For a task related to Labor this field would contain the related LaborHed.  */  
   Key1:string,
      /**  Second component of the foreign key to the related master record. For a task related to an Expense, this field would contain the related ExpenseID. For a task related to Labor, this field would contain the related LaborDtl.  */  
   Key2:string,
      /**  The master file to which the task is related.  */  
   RelatedToFile:string,
      /**  The SalesRep that this task is assigned to.  */  
   SalesRepCode:string,
      /**  Name corresponding to the SalesRepCode.  */  
   SalesRepName:string,
      /**  Number used to display the records in their correct sequence in the mobile app.  */  
   SequenceNum:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_MobileEmpExpenseAttchRow{
   Company:string,
   EmpID:string,
   EmpExpenseNum:number,
   DrawingSeq:number,
   XFileRefNum:number,
   SysRevID:number,
   SysRowID:string,
   ForeignSysRowID:string,
   DrawDesc:string,
   FileName:string,
   PDMDocID:string,
   DocTypeID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_MobileEmpExpenseCommentRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The employee the expense comment record is for.  */  
   EmpID:string,
      /**  Internal identifier of the EmpExpense record.  This with EmpID links the comment to a specific EmpExpense record.  */  
   EmpExpenseNum:number,
      /**  Internal identifier of the comment record.  Used in conjunction with EmpExpenseNum to make the record unique.  */  
   CommentNum:number,
      /**   The comment type of this record.  Values are:
"SUB" Submit
"APP" Approve
"REJ" Reject  */  
   CommentType:string,
      /**  The comment text.  */  
   CommentText:string,
      /**  Userid of the user who created the record.  */  
   CreatedBy:string,
      /**  The date the record was created.  */  
   CreateDate:string,
      /**  The time the record was created (in seconds since midnight)  */  
   CreateTime:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_MobileEmpExpenseListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The employee the expense record is for.  */  
   EmpID:string,
      /**  Internal identifier of the EmpExpense record.  This with EmpID makes the record unique.  */  
   EmpExpenseNum:number,
      /**  The date of the expense.  */  
   ExpenseDate:string,
      /**  Brief description of the expense.  Can be used to group expense entries together, for example, all time entries incurred on the same trip can be assigned the same reference.  */  
   ClaimRef:string,
      /**  Quick entry code.  Reference to the QuickEntry table.  Can be used to default information into the expense record.  */  
   QuickEntryCode:string,
      /**  Indicates if the expense is related to a project.  A value of true indicates the record is not related to a project.  */  
   Indirect:boolean,
      /**  The project the expense is related to.  */  
   ProjectID:string,
      /**  The project phase the expense is related to.  */  
   PhaseID:string,
      /**  The payment method of the expense.  */  
   PMUID:number,
      /**  The number of units of this expense.  */  
   Units:number,
      /**  Rate per unit of the expense.  */  
   UnitRate:number,
      /**  The currency the expense occurred in.  */  
   ExpCurrencyCode:string,
      /**  The Tax Region for this expense.  */  
   TaxRegionCode:string,
      /**  The tax of the expense in the expense currency.  */  
   DocExpenseTaxAmt:number,
      /**  The amount of the expense in the expense currency.  */  
   DocExpenseAmt:number,
      /**  Indicates if the expense amount includes tax.  */  
   TaxIncluded:boolean,
      /**   The status of the expense.  Values are:
Blank
E - Entered
S - Submitted
P - Partially Approved
A - Approved
R - Rejected  */  
   ExpenseStatus:string,
      /**  The date the expense received final approval.  */  
   ApprovedDate:string,
      /**  The miscellaneous charge code for this expense.  */  
   MiscCode:string,
      /**  The user who submitted the expense  */  
   SubmittedBy:string,
      /**  Indicates if approval is required for this transaction.  */  
   ApprovalRequired:boolean,
      /**  Indicates if the record is tax exempt.  If field is non-blank it is considered exempt.  */  
   TaxExempt:string,
      /**  Indicates if the expense is reimbursable.  */  
   Reimbursable:boolean,
      /**  The expense category.  */  
   ExpenseCategory:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_MobileEmpExpenseListTableset{
   MobileEmpExpenseList:Erp_Tablesets_MobileEmpExpenseListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_MobileEmpExpenseRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The employee the expense record is for.  */  
   EmpID:string,
      /**  Internal identifier of the EmpExpense record.  This with EmpID makes the record unique.  */  
   EmpExpenseNum:number,
      /**  The date of the expense.  */  
   ExpenseDate:string,
      /**  Brief description of the expense.  Can be used to group expense entries together, for example, all time entries incurred on the same trip can be assigned the same reference.  */  
   ClaimRef:string,
      /**  Quick entry code.  Reference to the QuickEntry table.  Can be used to default information into the expense record.  */  
   QuickEntryCode:string,
      /**  Indicates if the expense is related to a project.  A value of true indicates the record is not related to a project.  */  
   Indirect:boolean,
      /**  The project the expense is related to.  */  
   ProjectID:string,
      /**  The project phase the expense is related to.  */  
   PhaseID:string,
      /**  The payment method of the expense.  */  
   PMUID:number,
      /**  The number of units of this expense.  */  
   Units:number,
      /**  Rate per unit of the expense.  */  
   UnitRate:number,
      /**  The currency the expense occurred in.  */  
   ExpCurrencyCode:string,
      /**  The Tax Region for this expense.  */  
   TaxRegionCode:string,
      /**  The amount of the expense in the expense currency.  */  
   DocExpenseAmt:number,
      /**  Indicates if the expense amount includes tax.  */  
   TaxIncluded:boolean,
      /**  The total amount of the expense in the expense currency.  This value includes taxes.  */  
   DocTotalExpenseAmt:number,
      /**   The status of the expense.  Values are:
Blank
E - Entered
S - Submitted
P - Partially Approved
A - Approved
R - Rejected  */  
   ExpenseStatus:string,
      /**  The date the expense received final approval.  */  
   ApprovedDate:string,
      /**  The currency the claim amounts are in.  */  
   ClaimCurrencyCode:string,
      /**  The miscellaneous charge code for this expense.  */  
   MiscCode:string,
      /**  The user who submitted the expense  */  
   SubmittedBy:string,
      /**  Indicates if approval is required for this transaction.  */  
   ApprovalRequired:boolean,
      /**  Indicates if the record is tax exempt.  If field is non-blank it is considered exempt.  */  
   TaxExempt:string,
      /**  Indicates if the expense is reimbursable.  */  
   Reimbursable:boolean,
      /**  Expense Comment  */  
   ExpCommentText:string,
      /**  Expense Comment Instruction  */  
   ExpCommentInstr:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  External field to display a descriptive status of the record  */  
   DisplayStatus:string,
      /**  Indicates if the copy button is enabled  */  
   EnableCopy:boolean,
      /**  Indicates if the recall button is enabled  */  
   EnableRecall:boolean,
      /**  Indicates if recall is available in approval entry  */  
   EnableRecallAprv:boolean,
      /**  Indicates if the submit button is enabled  */  
   EnableSubmit:boolean,
   ExpenseDisableDelete:boolean,
   ExpenseDisableUpdate:boolean,
      /**  Indicates if the expense detail has attachments  */  
   HasAttachments:boolean,
      /**  Indicates if the expense detail has comments  */  
   HasComments:boolean,
      /**  Indicates if UnitRate is enabled  */  
   EnableUnitRate:boolean,
   SalesRepCode:string,
      /**  MobileGetApprovalStatus  */  
   ApprovedBy:string,
      /**  A list of people who need to approve the expense.  */  
   PendingApprovalBy:string,
   BitFlag:number,
   EmpBasicName:string,
   ExpCurrencyCurrSymbol:string,
   ExpCurrencyDocumentDesc:string,
   ExpCurrencyCurrName:string,
   ExpCurrencyCurrDesc:string,
   ExpCurrencyCurrencyID:string,
   PayMethodReimbursable:boolean,
   PayMethodSummarizePerCustomer:boolean,
   PayMethodName:string,
   PayMethodType:number,
   ProjectDescription:string,
   ProjPhaseDescription:string,
   PurMiscDescription:string,
   PurMiscExpUnitBased:boolean,
   TaxRgnDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_MobileEmpExpenseTableset{
   MobileEmpExpense:Erp_Tablesets_MobileEmpExpenseRow[],
   MobileEmpExpenseAttch:Erp_Tablesets_MobileEmpExpenseAttchRow[],
   MobileEmpExpenseComment:Erp_Tablesets_MobileEmpExpenseCommentRow[],
   MobileApproverList:Erp_Tablesets_MobileApproverListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtMobileEmpExpenseTableset{
   MobileEmpExpense:Erp_Tablesets_MobileEmpExpenseRow[],
   MobileEmpExpenseAttch:Erp_Tablesets_MobileEmpExpenseAttchRow[],
   MobileEmpExpenseComment:Erp_Tablesets_MobileEmpExpenseCommentRow[],
   MobileApproverList:Erp_Tablesets_MobileApproverListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param empID
      @param empExpenseNum
   */  
export interface GetByID_input{
   empID:string,
   empExpenseNum:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_MobileEmpExpenseTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_MobileEmpExpenseTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_MobileEmpExpenseTableset[],
}

   /** Required : 
      @param employeeID
      @param salesRepCode
      @param numberOfDays
   */  
export interface GetHomePageData_input{
   employeeID:string,
   salesRepCode:string,
   numberOfDays:number,
}

export interface GetHomePageData_output{
parameters : {
      /**  output parameters  */  
   entered:number,
   submitted:number,
   approved:number,
   rejected:number,
   forApproval:number,
   oldestRecordDate:string,
   submittedTotal:number,
   enteredTotal:number,
   approvedTotal:number,
   rejectedTotal:number,
   forApprovalTotal:number,
}
}

   /** Required : 
      @param whereClause
      @param pageSize
      @param absolutePage
   */  
export interface GetList_input{
      /**  An expression used to filter the rows. Can be left blank for all rows.  */  
   whereClause:string,
      /**  The maximum number of rows to return. Leave as zero for no maximum.  */  
   pageSize:number,
      /**  Page of rows to return.  */  
   absolutePage:number,
}

export interface GetList_output{
   returnObj:Erp_Tablesets_MobileEmpExpenseListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param empID
      @param empExpenseNum
   */  
export interface GetMobileEmpExpenseAttchs_input{
      /**  Employee ID  */  
   empID:string,
      /**  Expense Number  */  
   empExpenseNum:number,
}

export interface GetMobileEmpExpenseAttchs_output{
   returnObj:Erp_Tablesets_MobileEmpExpenseTableset[],
}

   /** Required : 
      @param empID
      @param empExpenseNum
   */  
export interface GetMobileEmpExpenseComments_input{
      /**  Employee ID  */  
   empID:string,
      /**  Expense Number  */  
   empExpenseNum:number,
}

export interface GetMobileEmpExpenseComments_output{
   returnObj:Erp_Tablesets_MobileEmpExpenseTableset[],
}

   /** Required : 
      @param ds
      @param empID
      @param empExpenseNum
   */  
export interface GetNewMobileEmpExpenseAttch_input{
   ds:Erp_Tablesets_MobileEmpExpenseTableset[],
   empID:string,
   empExpenseNum:number,
}

export interface GetNewMobileEmpExpenseAttch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MobileEmpExpenseTableset,
}
}

   /** Required : 
      @param ds
      @param empID
      @param empExpenseNum
   */  
export interface GetNewMobileEmpExpenseComment_input{
   ds:Erp_Tablesets_MobileEmpExpenseTableset[],
   empID:string,
   empExpenseNum:number,
}

export interface GetNewMobileEmpExpenseComment_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MobileEmpExpenseTableset,
}
}

   /** Required : 
      @param ds
      @param empID
   */  
export interface GetNewMobileEmpExpense_input{
   ds:Erp_Tablesets_MobileEmpExpenseTableset[],
   empID:string,
}

export interface GetNewMobileEmpExpense_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MobileEmpExpenseTableset,
}
}

   /** Required : 
      @param whereClauseMobileEmpExpense
      @param whereClauseMobileEmpExpenseAttch
      @param whereClauseMobileEmpExpenseComment
      @param whereClauseMobileApproverList
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseMobileEmpExpense:string,
   whereClauseMobileEmpExpenseAttch:string,
   whereClauseMobileEmpExpenseComment:string,
   whereClauseMobileApproverList:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_MobileEmpExpenseTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

export interface GetVersion_output{
   returnObj:string,
}

export interface Ice_BOUpdErrorRow{
   TableName:string,
   ErrorLevel:string,
   ErrorType:string,
   ErrorText:string,
   ErrorSysRowID:string,
   SysRowID:string,
   RowMod:string,
}

export interface Ice_BOUpdErrorTableset{
   BOUpdError:Ice_BOUpdErrorRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
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
      @param ds
      @param docTypeID
      @param parentTable
      @param fileName
      @param data
      @param metadata
   */  
export interface MobileAttachmentUpdate_input{
   ds:Erp_Tablesets_MobileEmpExpenseTableset[],
      /**  Document Type ID  */  
   docTypeID:string,
      /**  Parent Table e.g. LaborDtl  */  
   parentTable:string,
      /**  Physical name of the file  */  
   fileName:string,
      /**  Array of bytes representing the data of the attachment  */  
   data:string,
      /**  Metadata  */  
   metadata:any,      //schema had no properties on an object.
}

export interface MobileAttachmentUpdate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MobileEmpExpenseTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface MobileDelete_input{
   ds:Erp_Tablesets_MobileEmpExpenseTableset[],
}

export interface MobileDelete_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MobileEmpExpenseTableset,
}
}

   /** Required : 
      @param key1
      @param key2
      @param approvedBy
      @param pendingApprovalBy
   */  
export interface MobileGetApprovalStatus_input{
   key1:string,
   key2:string,
   approvedBy:string,
   pendingApprovalBy:string,
}

export interface MobileGetApprovalStatus_output{
   returnObj:Erp_Tablesets_MobileEmpExpenseTableset[],
}

   /** Required : 
      @param empID
      @param empExpenseNum
   */  
export interface MobileGetByID_input{
   empID:string,
   empExpenseNum:number,
}

export interface MobileGetByID_output{
   returnObj:Erp_Tablesets_MobileEmpExpenseTableset[],
}

   /** Required : 
      @param mobileEmpExpenseWhereClause
      @param pageSize
      @param absolutePage
   */  
export interface MobileGetList_input{
   mobileEmpExpenseWhereClause:string,
   pageSize:number,
   absolutePage:number,
}

export interface MobileGetList_output{
   returnObj:Erp_Tablesets_MobileEmpExpenseListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param empID
      @param empExpenseNum
   */  
export interface MobileGetNewEmpExpenseAttch_input{
   ds:Erp_Tablesets_MobileEmpExpenseTableset[],
      /**  The employee id  */  
   empID:string,
      /**  The expense number  */  
   empExpenseNum:number,
}

export interface MobileGetNewEmpExpenseAttch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MobileEmpExpenseTableset,
}
}

   /** Required : 
      @param ds
      @param empID
      @param empExpenseNum
   */  
export interface MobileGetNewEmpExpenseComment_input{
   ds:Erp_Tablesets_MobileEmpExpenseTableset[],
      /**  The employee id  */  
   empID:string,
      /**  The expense number  */  
   empExpenseNum:number,
}

export interface MobileGetNewEmpExpenseComment_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MobileEmpExpenseTableset,
}
}

   /** Required : 
      @param ds
      @param empID
   */  
export interface MobileGetNewEmpExpense_input{
   ds:Erp_Tablesets_MobileEmpExpenseTableset[],
      /**  The employee id  */  
   empID:string,
}

export interface MobileGetNewEmpExpense_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MobileEmpExpenseTableset,
}
}

   /** Required : 
      @param salesRepCode
      @param empID
      @param expenseDateFrom
      @param expenseDateTo
      @param expenseStatuses
      @param expenseTypes
      @param amountMinimum
      @param amountMaximum
      @param groupBy
      @param pageSize
      @param absolutePage
   */  
export interface MobileGetRowsApprover_input{
   salesRepCode:string,
   empID:string,
   expenseDateFrom:string,
   expenseDateTo:string,
   expenseStatuses:string,
   expenseTypes:string,
   amountMinimum:number,
   amountMaximum:number,
   groupBy:string,
   pageSize:number,
   absolutePage:number,
}

export interface MobileGetRowsApprover_output{
   returnObj:Erp_Tablesets_MobileEmpExpenseTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClauseMobileEmpExpense
      @param whereClauseMobileEmpExpenseAttch
      @param whereClauseMobileEmpExpenseComment
      @param pageSize
      @param absolutePage
   */  
export interface MobileGetRows_input{
   whereClauseMobileEmpExpense:string,
   whereClauseMobileEmpExpenseAttch:string,
   whereClauseMobileEmpExpenseComment:string,
   pageSize:number,
   absolutePage:number,
}

export interface MobileGetRows_output{
   returnObj:Erp_Tablesets_MobileEmpExpenseTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param company
      @param tableName
      @param sysRowID
   */  
export interface MobileSyncSuccessful_input{
      /**  Company where the record was created  */  
   company:string,
      /**  Name of the table related to the patch field  */  
   tableName:string,
      /**  SysRowID of the record on the Mobile  */  
   sysRowID:string,
}

export interface MobileSyncSuccessful_output{
}

   /** Required : 
      @param tableName
      @param ds
      @param comments
      @param salesRepCode
   */  
export interface MobileSync_input{
      /**  Name of the table that is being synchronized.  */  
   tableName:string,
   ds:Erp_Tablesets_MobileEmpExpenseTableset[],
      /**  Comments for approved and rejected records  */  
   comments:string,
      /**  Sales Rep Code  */  
   salesRepCode:string,
}

export interface MobileSync_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MobileEmpExpenseTableset,
   outMessage:string,
}
}

   /** Required : 
      @param ds
   */  
export interface MobileUpdate_input{
   ds:Erp_Tablesets_MobileEmpExpenseTableset[],
}

export interface MobileUpdate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MobileEmpExpenseTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface RecallEmpExpense_input{
   ds:Erp_Tablesets_MobileEmpExpenseTableset[],
}

export interface RecallEmpExpense_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MobileEmpExpenseTableset,
}
}

   /** Required : 
      @param salesRepCode
      @param ds
   */  
export interface RecallFromApproval_input{
      /**  The sales Rep Code of the approver.  */  
   salesRepCode:string,
   ds:Erp_Tablesets_MobileEmpExpenseTableset[],
}

export interface RecallFromApproval_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MobileEmpExpenseTableset,
   outMessage:string,
}
}

   /** Required : 
      @param ds
   */  
export interface SubmitSelected_input{
   ds:Erp_Tablesets_MobileEmpExpenseTableset[],
}

export interface SubmitSelected_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MobileEmpExpenseTableset,
   outMessage:string,
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtMobileEmpExpenseTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtMobileEmpExpenseTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_MobileEmpExpenseTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MobileEmpExpenseTableset,
}
}

