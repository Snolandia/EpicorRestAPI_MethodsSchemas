import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.EmpExpenseSvc
// Description: Employee Expense Business Object
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/$metadata", {
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
   Summary: Calls GetRows for the service
   Description: Get EmpExpenses items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_EmpExpenses
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.EmpExpenseRow
   */  
export function get_EmpExpenses(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EmpExpenseRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/EmpExpenses", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EmpExpenseRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_EmpExpenses
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.EmpExpenseRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.EmpExpenseRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_EmpExpenses(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/EmpExpenses", {
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
   Summary: Calls GetByID to retrieve the EmpExpense item
   Description: Calls GetByID to retrieve the EmpExpense item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EmpExpense
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EmpID Desc: EmpID   Required: True   Allow empty value : True
      @param EmpExpenseNum Desc: EmpExpenseNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.EmpExpenseRow
   */  
export function get_EmpExpenses_Company_EmpID_EmpExpenseNum(Company:string, EmpID:string, EmpExpenseNum:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_EmpExpenseRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/EmpExpenses(" + Company + "," + EmpID + "," + EmpExpenseNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_EmpExpenseRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update EmpExpense for the service
   Description: Calls UpdateExt to update EmpExpense. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_EmpExpense
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EmpID Desc: EmpID   Required: True   Allow empty value : True
      @param EmpExpenseNum Desc: EmpExpenseNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.EmpExpenseRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_EmpExpenses_Company_EmpID_EmpExpenseNum(Company:string, EmpID:string, EmpExpenseNum:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/EmpExpenses(" + Company + "," + EmpID + "," + EmpExpenseNum + ")", {
          method: 'patch',
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
   Summary: Call UpdateExt to delete EmpExpense item
   Description: Call UpdateExt to delete EmpExpense item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_EmpExpense
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EmpID Desc: EmpID   Required: True   Allow empty value : True
      @param EmpExpenseNum Desc: EmpExpenseNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_EmpExpenses_Company_EmpID_EmpExpenseNum(Company:string, EmpID:string, EmpExpenseNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/EmpExpenses(" + Company + "," + EmpID + "," + EmpExpenseNum + ")", {
          method: 'delete',
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
   Summary: Calls GetByID for the service
   Description: Get EmpExpenseComments items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_EmpExpenseComments1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EmpID Desc: EmpID   Required: True   Allow empty value : True
      @param EmpExpenseNum Desc: EmpExpenseNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.EmpExpenseCommentRow
   */  
export function get_EmpExpenses_Company_EmpID_EmpExpenseNum_EmpExpenseComments(Company:string, EmpID:string, EmpExpenseNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EmpExpenseCommentRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/EmpExpenses(" + Company + "," + EmpID + "," + EmpExpenseNum + ")/EmpExpenseComments", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EmpExpenseCommentRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the EmpExpenseComment item
   Description: Calls GetByID to retrieve the EmpExpenseComment item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EmpExpenseComment1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EmpID Desc: EmpID   Required: True   Allow empty value : True
      @param EmpExpenseNum Desc: EmpExpenseNum   Required: True
      @param CommentNum Desc: CommentNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.EmpExpenseCommentRow
   */  
export function get_EmpExpenses_Company_EmpID_EmpExpenseNum_EmpExpenseComments_Company_EmpID_EmpExpenseNum_CommentNum(Company:string, EmpID:string, EmpExpenseNum:string, CommentNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_EmpExpenseCommentRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/EmpExpenses(" + Company + "," + EmpID + "," + EmpExpenseNum + ")/EmpExpenseComments(" + Company + "," + EmpID + "," + EmpExpenseNum + "," + CommentNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_EmpExpenseCommentRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get EmpExpenseTaxes items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_EmpExpenseTaxes1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EmpID Desc: EmpID   Required: True   Allow empty value : True
      @param EmpExpenseNum Desc: EmpExpenseNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.EmpExpenseTaxRow
   */  
export function get_EmpExpenses_Company_EmpID_EmpExpenseNum_EmpExpenseTaxes(Company:string, EmpID:string, EmpExpenseNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EmpExpenseTaxRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/EmpExpenses(" + Company + "," + EmpID + "," + EmpExpenseNum + ")/EmpExpenseTaxes", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EmpExpenseTaxRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the EmpExpenseTax item
   Description: Calls GetByID to retrieve the EmpExpenseTax item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EmpExpenseTax1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EmpID Desc: EmpID   Required: True   Allow empty value : True
      @param EmpExpenseNum Desc: EmpExpenseNum   Required: True
      @param TaxCode Desc: TaxCode   Required: True   Allow empty value : True
      @param RateCode Desc: RateCode   Required: True   Allow empty value : True
      @param ECAcquisitionSeq Desc: ECAcquisitionSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.EmpExpenseTaxRow
   */  
export function get_EmpExpenses_Company_EmpID_EmpExpenseNum_EmpExpenseTaxes_Company_EmpID_EmpExpenseNum_TaxCode_RateCode_ECAcquisitionSeq(Company:string, EmpID:string, EmpExpenseNum:string, TaxCode:string, RateCode:string, ECAcquisitionSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_EmpExpenseTaxRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/EmpExpenses(" + Company + "," + EmpID + "," + EmpExpenseNum + ")/EmpExpenseTaxes(" + Company + "," + EmpID + "," + EmpExpenseNum + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_EmpExpenseTaxRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get EmpExpenseAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_EmpExpenseAttches1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EmpID Desc: EmpID   Required: True   Allow empty value : True
      @param EmpExpenseNum Desc: EmpExpenseNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.EmpExpenseAttchRow
   */  
export function get_EmpExpenses_Company_EmpID_EmpExpenseNum_EmpExpenseAttches(Company:string, EmpID:string, EmpExpenseNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EmpExpenseAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/EmpExpenses(" + Company + "," + EmpID + "," + EmpExpenseNum + ")/EmpExpenseAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EmpExpenseAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the EmpExpenseAttch item
   Description: Calls GetByID to retrieve the EmpExpenseAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EmpExpenseAttch1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EmpID Desc: EmpID   Required: True   Allow empty value : True
      @param EmpExpenseNum Desc: EmpExpenseNum   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.EmpExpenseAttchRow
   */  
export function get_EmpExpenses_Company_EmpID_EmpExpenseNum_EmpExpenseAttches_Company_EmpID_EmpExpenseNum_DrawingSeq(Company:string, EmpID:string, EmpExpenseNum:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_EmpExpenseAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/EmpExpenses(" + Company + "," + EmpID + "," + EmpExpenseNum + ")/EmpExpenseAttches(" + Company + "," + EmpID + "," + EmpExpenseNum + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_EmpExpenseAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get EmpExpenseComments items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_EmpExpenseComments
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.EmpExpenseCommentRow
   */  
export function get_EmpExpenseComments(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EmpExpenseCommentRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/EmpExpenseComments", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EmpExpenseCommentRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_EmpExpenseComments
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.EmpExpenseCommentRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.EmpExpenseCommentRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_EmpExpenseComments(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/EmpExpenseComments", {
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
   Summary: Calls GetByID to retrieve the EmpExpenseComment item
   Description: Calls GetByID to retrieve the EmpExpenseComment item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EmpExpenseComment
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EmpID Desc: EmpID   Required: True   Allow empty value : True
      @param EmpExpenseNum Desc: EmpExpenseNum   Required: True
      @param CommentNum Desc: CommentNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.EmpExpenseCommentRow
   */  
export function get_EmpExpenseComments_Company_EmpID_EmpExpenseNum_CommentNum(Company:string, EmpID:string, EmpExpenseNum:string, CommentNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_EmpExpenseCommentRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/EmpExpenseComments(" + Company + "," + EmpID + "," + EmpExpenseNum + "," + CommentNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_EmpExpenseCommentRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update EmpExpenseComment for the service
   Description: Calls UpdateExt to update EmpExpenseComment. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_EmpExpenseComment
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EmpID Desc: EmpID   Required: True   Allow empty value : True
      @param EmpExpenseNum Desc: EmpExpenseNum   Required: True
      @param CommentNum Desc: CommentNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.EmpExpenseCommentRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_EmpExpenseComments_Company_EmpID_EmpExpenseNum_CommentNum(Company:string, EmpID:string, EmpExpenseNum:string, CommentNum:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/EmpExpenseComments(" + Company + "," + EmpID + "," + EmpExpenseNum + "," + CommentNum + ")", {
          method: 'patch',
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
   Summary: Call UpdateExt to delete EmpExpenseComment item
   Description: Call UpdateExt to delete EmpExpenseComment item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_EmpExpenseComment
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EmpID Desc: EmpID   Required: True   Allow empty value : True
      @param EmpExpenseNum Desc: EmpExpenseNum   Required: True
      @param CommentNum Desc: CommentNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_EmpExpenseComments_Company_EmpID_EmpExpenseNum_CommentNum(Company:string, EmpID:string, EmpExpenseNum:string, CommentNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/EmpExpenseComments(" + Company + "," + EmpID + "," + EmpExpenseNum + "," + CommentNum + ")", {
          method: 'delete',
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
   Summary: Calls GetRows for the service
   Description: Get EmpExpenseTaxes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_EmpExpenseTaxes
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.EmpExpenseTaxRow
   */  
export function get_EmpExpenseTaxes(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EmpExpenseTaxRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/EmpExpenseTaxes", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EmpExpenseTaxRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_EmpExpenseTaxes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.EmpExpenseTaxRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.EmpExpenseTaxRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_EmpExpenseTaxes(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/EmpExpenseTaxes", {
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
   Summary: Calls GetByID to retrieve the EmpExpenseTax item
   Description: Calls GetByID to retrieve the EmpExpenseTax item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EmpExpenseTax
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EmpID Desc: EmpID   Required: True   Allow empty value : True
      @param EmpExpenseNum Desc: EmpExpenseNum   Required: True
      @param TaxCode Desc: TaxCode   Required: True   Allow empty value : True
      @param RateCode Desc: RateCode   Required: True   Allow empty value : True
      @param ECAcquisitionSeq Desc: ECAcquisitionSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.EmpExpenseTaxRow
   */  
export function get_EmpExpenseTaxes_Company_EmpID_EmpExpenseNum_TaxCode_RateCode_ECAcquisitionSeq(Company:string, EmpID:string, EmpExpenseNum:string, TaxCode:string, RateCode:string, ECAcquisitionSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_EmpExpenseTaxRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/EmpExpenseTaxes(" + Company + "," + EmpID + "," + EmpExpenseNum + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_EmpExpenseTaxRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update EmpExpenseTax for the service
   Description: Calls UpdateExt to update EmpExpenseTax. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_EmpExpenseTax
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EmpID Desc: EmpID   Required: True   Allow empty value : True
      @param EmpExpenseNum Desc: EmpExpenseNum   Required: True
      @param TaxCode Desc: TaxCode   Required: True   Allow empty value : True
      @param RateCode Desc: RateCode   Required: True   Allow empty value : True
      @param ECAcquisitionSeq Desc: ECAcquisitionSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.EmpExpenseTaxRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_EmpExpenseTaxes_Company_EmpID_EmpExpenseNum_TaxCode_RateCode_ECAcquisitionSeq(Company:string, EmpID:string, EmpExpenseNum:string, TaxCode:string, RateCode:string, ECAcquisitionSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/EmpExpenseTaxes(" + Company + "," + EmpID + "," + EmpExpenseNum + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")", {
          method: 'patch',
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
   Summary: Call UpdateExt to delete EmpExpenseTax item
   Description: Call UpdateExt to delete EmpExpenseTax item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_EmpExpenseTax
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EmpID Desc: EmpID   Required: True   Allow empty value : True
      @param EmpExpenseNum Desc: EmpExpenseNum   Required: True
      @param TaxCode Desc: TaxCode   Required: True   Allow empty value : True
      @param RateCode Desc: RateCode   Required: True   Allow empty value : True
      @param ECAcquisitionSeq Desc: ECAcquisitionSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_EmpExpenseTaxes_Company_EmpID_EmpExpenseNum_TaxCode_RateCode_ECAcquisitionSeq(Company:string, EmpID:string, EmpExpenseNum:string, TaxCode:string, RateCode:string, ECAcquisitionSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/EmpExpenseTaxes(" + Company + "," + EmpID + "," + EmpExpenseNum + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")", {
          method: 'delete',
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
   Summary: Calls GetRows for the service
   Description: Get EmpExpenseAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_EmpExpenseAttches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.EmpExpenseAttchRow
   */  
export function get_EmpExpenseAttches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EmpExpenseAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/EmpExpenseAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EmpExpenseAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_EmpExpenseAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.EmpExpenseAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.EmpExpenseAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_EmpExpenseAttches(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/EmpExpenseAttches", {
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
   Summary: Calls GetByID to retrieve the EmpExpenseAttch item
   Description: Calls GetByID to retrieve the EmpExpenseAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EmpExpenseAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EmpID Desc: EmpID   Required: True   Allow empty value : True
      @param EmpExpenseNum Desc: EmpExpenseNum   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.EmpExpenseAttchRow
   */  
export function get_EmpExpenseAttches_Company_EmpID_EmpExpenseNum_DrawingSeq(Company:string, EmpID:string, EmpExpenseNum:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_EmpExpenseAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/EmpExpenseAttches(" + Company + "," + EmpID + "," + EmpExpenseNum + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_EmpExpenseAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update EmpExpenseAttch for the service
   Description: Calls UpdateExt to update EmpExpenseAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_EmpExpenseAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EmpID Desc: EmpID   Required: True   Allow empty value : True
      @param EmpExpenseNum Desc: EmpExpenseNum   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.EmpExpenseAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_EmpExpenseAttches_Company_EmpID_EmpExpenseNum_DrawingSeq(Company:string, EmpID:string, EmpExpenseNum:string, DrawingSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/EmpExpenseAttches(" + Company + "," + EmpID + "," + EmpExpenseNum + "," + DrawingSeq + ")", {
          method: 'patch',
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
   Summary: Call UpdateExt to delete EmpExpenseAttch item
   Description: Call UpdateExt to delete EmpExpenseAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_EmpExpenseAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EmpID Desc: EmpID   Required: True   Allow empty value : True
      @param EmpExpenseNum Desc: EmpExpenseNum   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_EmpExpenseAttches_Company_EmpID_EmpExpenseNum_DrawingSeq(Company:string, EmpID:string, EmpExpenseNum:string, DrawingSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/EmpExpenseAttches(" + Company + "," + EmpID + "," + EmpExpenseNum + "," + DrawingSeq + ")", {
          method: 'delete',
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.EmpExpenseListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EmpExpenseListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EmpExpenseListRow)
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
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClauseEmpExpense:string, whereClauseEmpExpenseAttch:string, whereClauseEmpExpenseComment:string, whereClauseEmpExpenseTax:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseEmpExpense!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseEmpExpense=" + whereClauseEmpExpense
   }
   if(typeof whereClauseEmpExpenseAttch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseEmpExpenseAttch=" + whereClauseEmpExpenseAttch
   }
   if(typeof whereClauseEmpExpenseComment!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseEmpExpenseComment=" + whereClauseEmpExpenseComment
   }
   if(typeof whereClauseEmpExpenseTax!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseEmpExpenseTax=" + whereClauseEmpExpenseTax
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

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/GetRows" + params, {
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
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
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

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/GetByID" + params, {
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
   Summary: Invoke method GetList
   Description: Returns a list of rows that satisfy the where clause.
   OperationID: Get_GetList
      @param whereClause Desc: An expression used to filter the rows. Can be left blank for all rows.   Required: True   Allow empty value : True
      @param pageSize Desc: The maximum number of rows to return. Leave as zero for no maximum.   Required: True
      @param absolutePage Desc: Page of rows to return.   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
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

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/GetList" + params, {
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
   Summary: Invoke method ApproveReject
   Description: The procedure is called when the user selects EmpExpense records for reject or approve
   OperationID: ApproveReject
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ApproveReject_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ApproveReject_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ApproveReject(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/ApproveReject", {
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
   Summary: Invoke method ChangeEmpExpenseClaimCurrencyCode
   Description: Method to call when changing the Claim Currency Code.  Exchange rate
is reevaluted
   OperationID: ChangeEmpExpenseClaimCurrencyCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeEmpExpenseClaimCurrencyCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeEmpExpenseClaimCurrencyCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeEmpExpenseClaimCurrencyCode(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/ChangeEmpExpenseClaimCurrencyCode", {
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
   Summary: Invoke method ChangeEmpExpenseClaimExchangeRate
   Description: Method to call when changing the claim exchange rate.
   OperationID: ChangeEmpExpenseClaimExchangeRate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeEmpExpenseClaimExchangeRate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeEmpExpenseClaimExchangeRate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeEmpExpenseClaimExchangeRate(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/ChangeEmpExpenseClaimExchangeRate", {
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
   Summary: Invoke method ChangeEmpExpenseClaimLockRate
   Description: Method to call when changing the Claim Lock Rate.  Exchange rate
is reevaluted
   OperationID: ChangeEmpExpenseClaimLockRate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeEmpExpenseClaimLockRate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeEmpExpenseClaimLockRate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeEmpExpenseClaimLockRate(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/ChangeEmpExpenseClaimLockRate", {
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
   Summary: Invoke method ChangeEmpExpenseClaimRateGrpCode
   Description: Method to call when changing the Claim Rate Group Code.  Exchange rate
is reevaluted
   OperationID: ChangeEmpExpenseClaimRateGrpCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeEmpExpenseClaimRateGrpCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeEmpExpenseClaimRateGrpCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeEmpExpenseClaimRateGrpCode(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/ChangeEmpExpenseClaimRateGrpCode", {
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
   Summary: Invoke method ChangeEmpExpenseDispClaimAmt
   Description: Method to call when changing the Claim Amount.  The field DispClaimAmt
is the field that should trigger the call to this procedure.
   OperationID: ChangeEmpExpenseDispClaimAmt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeEmpExpenseDispClaimAmt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeEmpExpenseDispClaimAmt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeEmpExpenseDispClaimAmt(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/ChangeEmpExpenseDispClaimAmt", {
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
   Summary: Invoke method ChangeEmpExpenseDocExpenseAmt
   Description: Method to call when changing the Doc Expense Amount.
   OperationID: ChangeEmpExpenseDocExpenseAmt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeEmpExpenseDocExpenseAmt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeEmpExpenseDocExpenseAmt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeEmpExpenseDocExpenseAmt(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/ChangeEmpExpenseDocExpenseAmt", {
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
   Summary: Invoke method ChangeEmpExpenseExpCurrencyCode
   Description: Method to call when changing the Expense Currency Code.  Exchange rate
is reevaluted
   OperationID: ChangeEmpExpenseExpCurrencyCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeEmpExpenseExpCurrencyCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeEmpExpenseExpCurrencyCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeEmpExpenseExpCurrencyCode(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/ChangeEmpExpenseExpCurrencyCode", {
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
   Summary: Invoke method ChangeEmpExpenseExpenseDate
   Description: Method to call when changing the Expense Date.  This can affect the exchange rate.
   OperationID: ChangeEmpExpenseExpenseDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeEmpExpenseExpenseDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeEmpExpenseExpenseDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeEmpExpenseExpenseDate(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/ChangeEmpExpenseExpenseDate", {
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
   Summary: Invoke method ChangeEmpExpenseIndirect
   Description: Method to call when changing Indirect.
   OperationID: ChangeEmpExpenseIndirect
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeEmpExpenseIndirect_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeEmpExpenseIndirect_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeEmpExpenseIndirect(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/ChangeEmpExpenseIndirect", {
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
   Summary: Invoke method ChangeEmpExpenseMiscCode
   Description: Method to call when changing the Miscellaneous Code.
   OperationID: ChangeEmpExpenseMiscCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeEmpExpenseMiscCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeEmpExpenseMiscCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeEmpExpenseMiscCode(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/ChangeEmpExpenseMiscCode", {
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
   Summary: Invoke method ChangeEmpExpensePayMethod
   Description: Method to call when changing the Payment Method.
   OperationID: ChangeEmpExpensePayMethod
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeEmpExpensePayMethod_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeEmpExpensePayMethod_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeEmpExpensePayMethod(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/ChangeEmpExpensePayMethod", {
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
   Summary: Invoke method ChangeEmpExpensePhaseID
   Description: Method to call when changing the WBS Phase ID.
   OperationID: ChangeEmpExpensePhaseID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeEmpExpensePhaseID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeEmpExpensePhaseID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeEmpExpensePhaseID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/ChangeEmpExpensePhaseID", {
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
   Summary: Invoke method ChangeEmpExpenseProjectID
   Description: Method to call when changing the Project ID.
   OperationID: ChangeEmpExpenseProjectID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeEmpExpenseProjectID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeEmpExpenseProjectID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeEmpExpenseProjectID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/ChangeEmpExpenseProjectID", {
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
   Summary: Invoke method ChangeEmpExpenseQuickEntryCode
   Description: Method to call when changing the quick entry code.  Quick entry values
are used for default values on the expense.
   OperationID: ChangeEmpExpenseQuickEntryCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeEmpExpenseQuickEntryCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeEmpExpenseQuickEntryCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeEmpExpenseQuickEntryCode(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/ChangeEmpExpenseQuickEntryCode", {
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
   Summary: Invoke method ChangeEmpExpenseUnitRate
   Description: Method to call when changing the Unit Rate.
   OperationID: ChangeEmpExpenseUnitRate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeEmpExpenseUnitRate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeEmpExpenseUnitRate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeEmpExpenseUnitRate(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/ChangeEmpExpenseUnitRate", {
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
   Summary: Invoke method ChangeEmpExpenseUnits
   Description: Method to call when changing the Units.
   OperationID: ChangeEmpExpenseUnits
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeEmpExpenseUnits_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeEmpExpenseUnits_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeEmpExpenseUnits(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/ChangeEmpExpenseUnits", {
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
   Summary: Invoke method CheckRecallFromApproval
   Description: The procedure is called prior to performing a recall.  It will check
if subsequent approvals have occurred.  If they have the user
will have the opportunity to cancel the recall.
   OperationID: CheckRecallFromApproval
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckRecallFromApproval_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckRecallFromApproval_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckRecallFromApproval(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/CheckRecallFromApproval", {
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
   Summary: Invoke method CopyEmpExpense
   Description: Method to copy the vales from one EmpExpense record to a new EmpExpense record.
   OperationID: CopyEmpExpense
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CopyEmpExpense_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CopyEmpExpense_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CopyEmpExpense(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/CopyEmpExpense", {
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
   Summary: Invoke method GetListExpenses
   Description: This method returns a list of Expenses to be viewed in the Time and Expense Entry
screen based on Claim Reference, Invoice Num, Invoice Status and Expense Status.
This method builds the where clause instead of having the UI build the where clause
on their end.
   OperationID: GetListExpenses
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListExpenses_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListExpenses_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetListExpenses(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/GetListExpenses", {
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
   Summary: Invoke method MobileGetRowsTran
   Description: Called from Mobile time and expense application to retrieve expense transactions and to also check
whether we are retrieving comments / attachments as part of the dataset.
   OperationID: MobileGetRowsTran
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MobileGetRowsTran_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MobileGetRowsTran_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MobileGetRowsTran(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/MobileGetRowsTran", {
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
   Summary: Invoke method GetRowsTran
   Description: Called from Approvals screen to get related task expense transactions
   OperationID: GetRowsTran
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsTran_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsTran_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRowsTran(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/GetRowsTran", {
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
   Summary: Invoke method RecallEmpExpense
   Description: Method to call when recalling submitted expense records
   OperationID: RecallEmpExpense
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RecallEmpExpense_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RecallEmpExpense_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RecallEmpExpense(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/RecallEmpExpense", {
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
   Summary: Invoke method RecallFromApproval
   Description: Method to call when recalling from approval entry
   OperationID: RecallFromApproval
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RecallFromApproval_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RecallFromApproval_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RecallFromApproval(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/RecallFromApproval", {
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
   Summary: Invoke method SubmitSelected
   Description: Method to call to submit selected expenses
   OperationID: SubmitSelected
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SubmitSelected_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SubmitSelected_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SubmitSelected(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/SubmitSelected", {
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
   Summary: Invoke method GetRateCodeInfo
   Description: This method updates the dataset when the RateCode field changes
   OperationID: GetRateCodeInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRateCodeInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRateCodeInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRateCodeInfo(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/GetRateCodeInfo", {
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
   Summary: Invoke method EmpExpenseAfterGetRowsWrapper
   Description: Calls EmpExpenseAfterGetRows for the passed in EmpExpense row
   OperationID: EmpExpenseAfterGetRowsWrapper
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/EmpExpenseAfterGetRowsWrapper_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/EmpExpenseAfterGetRowsWrapper_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_EmpExpenseAfterGetRowsWrapper(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/EmpExpenseAfterGetRowsWrapper", {
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
   Summary: Invoke method EmpExpenseCommentAfterGetRowsWrapper
   Description: Calls EmpExpenseCommentAfterGetRows for the passed in EmpExpenseComment row
   OperationID: EmpExpenseCommentAfterGetRowsWrapper
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/EmpExpenseCommentAfterGetRowsWrapper_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/EmpExpenseCommentAfterGetRowsWrapper_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_EmpExpenseCommentAfterGetRowsWrapper(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/EmpExpenseCommentAfterGetRowsWrapper", {
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
   Summary: Invoke method GetNewEmpExpenseForDate
   Description: Create a new EmpExpense record for a specific date
   OperationID: GetNewEmpExpenseForDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewEmpExpenseForDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewEmpExpenseForDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewEmpExpenseForDate(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/GetNewEmpExpenseForDate", {
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
   Summary: Invoke method EmpExpenseRetrieveOptionsClause
   Description: Returns a string that contains EmpExpense retrieve options based on user settings.  This string
is intended to be appended to an existing where clause for GetRows/GetList calls.
   OperationID: EmpExpenseRetrieveOptionsClause
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/EmpExpenseRetrieveOptionsClause_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_EmpExpenseRetrieveOptionsClause(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/EmpExpenseRetrieveOptionsClause", {
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
   Summary: Invoke method SubmitForApprovalBySelected
   Description: Method to submit Expense records for Approval using RowSelected flag.
   OperationID: SubmitForApprovalBySelected
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SubmitForApprovalBySelected_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SubmitForApprovalBySelected_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SubmitForApprovalBySelected(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/SubmitForApprovalBySelected", {
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
   Summary: Invoke method RecallFromApprovalBySelected
   Description: Method to recall EmpExpense for Approval using RowSelected flag.
   OperationID: RecallFromApprovalBySelected
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RecallFromApprovalBySelected_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RecallFromApprovalBySelected_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RecallFromApprovalBySelected(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/RecallFromApprovalBySelected", {
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
   Summary: Invoke method CopyEmpExpenseByID
   Description: Method to copy EmpExpense by Expense ID
   OperationID: CopyEmpExpenseByID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CopyEmpExpenseByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CopyEmpExpenseByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CopyEmpExpenseByID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/CopyEmpExpenseByID", {
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
   Summary: Invoke method DeleteExpense
   Description: Method to delete multiple expenses by ExpNum
   OperationID: DeleteExpense
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteExpense_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteExpense_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteExpense(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/DeleteExpense", {
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
   Summary: Invoke method GetNewEmpExpense
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewEmpExpense
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewEmpExpense_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewEmpExpense_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewEmpExpense(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/GetNewEmpExpense", {
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
   Summary: Invoke method GetNewEmpExpenseAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewEmpExpenseAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewEmpExpenseAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewEmpExpenseAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewEmpExpenseAttch(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/GetNewEmpExpenseAttch", {
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
   Summary: Invoke method GetNewEmpExpenseComment
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewEmpExpenseComment
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewEmpExpenseComment_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewEmpExpenseComment_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewEmpExpenseComment(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/GetNewEmpExpenseComment", {
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
   Summary: Invoke method GetNewEmpExpenseTax
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewEmpExpenseTax
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewEmpExpenseTax_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewEmpExpenseTax_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewEmpExpenseTax(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/GetNewEmpExpenseTax", {
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
   Summary: Invoke method DeleteByID
   Description: Deletes a row given its ID.
   OperationID: DeleteByID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteByID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/DeleteByID", {
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
   Summary: Invoke method GetBySysRowID
   OperationID: Get_GetBySysRowID
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
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

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/GetBySysRowID" + params, {
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
   Summary: Invoke method GetBySysRowIDs
   OperationID: Get_GetBySysRowIDs
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
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

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/GetBySysRowIDs" + params, {
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
   Summary: Invoke method Update
   Description: Commits the DataSet changes to the data store.
   OperationID: Update
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Update_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Update_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_Update(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/Update", {
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
   Summary: Invoke method UpdateExt
   Description: Apply input data to service by calling GetByID/GetNew/Update methods.
   OperationID: UpdateExt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateExt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateExt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateExt(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EmpExpenseAttchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_EmpExpenseAttchRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EmpExpenseCommentRow{
   "odatametadata":string,
   "value":Erp_Tablesets_EmpExpenseCommentRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EmpExpenseListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_EmpExpenseListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EmpExpenseRow{
   "odatametadata":string,
   "value":Erp_Tablesets_EmpExpenseRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EmpExpenseTaxRow{
   "odatametadata":string,
   "value":Erp_Tablesets_EmpExpenseTaxRow[],
}

export interface Erp_Tablesets_EmpExpenseAttchRow{
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

export interface Erp_Tablesets_EmpExpenseCommentRow{
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
      /**  Userid of the user who made the last change to this record.  */  
   "ChangedBy":string,
      /**  The date the record was last changed.  */  
   "ChangeDate":string,
      /**  The time the record was last changed (in seconds since midnight)  */  
   "ChangeTime":number,
      /**  The identifier of the Task record the comment is related to.  Can be zero, which indicates the comment is not related to a specific task.  */  
   "TaskSeqNum":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "DspChangeTime":string,
   "DspCreateTime":string,
      /**  Submit comment instructions  */  
   "SubmitCommentInstr":string,
   "TreeNodeImageName":string,
      /**  Unique identifier of related integration record.  */  
   "IntExternalKey":string,
      /**  List of valid comment types for Expense Entry  */  
   "ExpEntryCommentTypeList":string,
   "CommentTypeDesc":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_EmpExpenseListRow{
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
      /**  The FromEffectiveDate from ExpenseTypeUnitBased that was used to determine default values for Units and UnitRate.  This combined with ExpenseTypeCode point to a unique ExpenseTypeUnitBased record.  */  
   "UBFromEffectiveDate":string,
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
      /**  The charge currency.  This is derived from the currency on the related project.  */  
   "ChargeCurrencyCode":string,
      /**  The charge exchange rate.  This is derived from the exchange rate on the related project.  */  
   "ChargeExchangeRate":number,
      /**  The charge rate group code.  This is derived from the rate group code on the related projec.t  */  
   "ChargeRateGrpCode":string,
      /**  The charge amount of the expense in the charge currency.  */  
   "DocChargeAmt":number,
      /**  The date the expense received final approval.  */  
   "ApprovedDate":string,
      /**  The supplier number used on the employee of the expense.  */  
   "VendorNum":number,
      /**  The ap invoice number the expense was invoiced on.  */  
   "InvoiceNum":string,
      /**  The invoice line created for this expense.  */  
   "InvoiceLine":number,
      /**  Link to Task set  */  
   "TaskSetID":string,
      /**  Indicates if this expense is a reversal (full or partial) of an existing expense.  */  
   "IsReversal":boolean,
      /**  Reversed Expense Number  */  
   "ReversedExpenseNum":number,
      /**  Userid of the user who created the record.  */  
   "CreatedBy":string,
      /**  The date the record was created.  */  
   "CreateDate":string,
      /**  The time the record was created (in seconds since midnight)  */  
   "CreateTime":number,
      /**  Userid of the user who made the last change to this record.  */  
   "ChangedBy":string,
      /**  The date the record was last changed.  */  
   "ChangeDate":string,
      /**  The time the record was last changed (in seconds since midnight)  */  
   "ChangeTime":number,
      /**  The Currently active Stage changing task  */  
   "ActiveTaskID":string,
      /**  The Last Complete Milestone task  */  
   "LastTaskID":string,
      /**  The currency the claim amounts are in.  */  
   "ClaimCurrencyCode":string,
      /**  The exchange rate between the claim currency and the base currency based on expense date.  */  
   "ClaimExchangeRate":number,
      /**  Used with the currency module.  When TRUE the claim currency rate can be changed by the user and cannot be changed by the system.  */  
   "ClaimLockRate":boolean,
      /**  The claim rate group code.  */  
   "ClaimRateGrpCode":string,
      /**  The tax of the claim in the claim currency.  */  
   "DocClaimTaxAmt":number,
      /**  The amount of the claim in the claim currency.  */  
   "DocClaimAmt":number,
      /**  The total amount of the claim in the claim currency.  This value includes taxes.  */  
   "DocTotalClaimAmt":number,
      /**  The miscellaneous charge code for this expense.  */  
   "MiscCode":string,
      /**  The user who submitted the expense  */  
   "SubmittedBy":string,
      /**  The identifier of the workflow stage.  */  
   "CurrentWFStageID":string,
      /**  The identifier of the workflow group  */  
   "WFGroupID":string,
      /**  This indicates if the workflow for this group is complete.  */  
   "WFComplete":boolean,
      /**  Indicates if approval is required for this transaction.  */  
   "ApprovalRequired":boolean,
      /**  Indicates if the record is tax exempt.  If field is non-blank it is considered exempt.  */  
   "TaxExempt":string,
      /**  If set to true, the tax calculation logic will retrieve the default SalesTax ids for the expense before calculating taxes. It will also be reset to true if the TaxConnectCalc flag switches from true to false.  */  
   "GetDfltTaxIds":boolean,
      /**  If true, the EmpExpenseTax records tied to this release are calculated using Tax Connect logic. If  false, taxes are calculated using the standard calc methods.  */  
   "TaxConnectCalc":boolean,
      /**  Expense Withholding Tax Amount.  */  
   "DocExpWithholdAmt":number,
      /**  Claim Withholding Tax Amount.  */  
   "DocClaimWithholdAmt":number,
      /**  Indicates if the expense is reimbursable.  */  
   "Reimbursable":boolean,
      /**  The tax of the claim in the charge currency.  */  
   "DocChargeTaxAmt":number,
      /**  The total charge amount in the charge currency.  This value includes taxes.  */  
   "DocTotalChargeAmt":number,
      /**  The exchange rate between the claim currency and the base currency.  */  
   "ClaimToBaseExchangeRate":number,
      /**  Job Number of the misc charge jobmtl record  */  
   "JobNum":string,
      /**  Assembly sequence number of the misc charge jobmtl record  */  
   "AssemblySeq":number,
      /**  Material sequence of the misc charge jobmtl record  */  
   "MtlSeq":number,
      /**  Indicates if the expense has been invoiced.  */  
   "Invoiced":boolean,
      /**  Expense Comment  */  
   "ExpCommentText":string,
      /**  Expense Comment Instruction  */  
   "ExpCommentInstr":string,
      /**  Indicates that this record has been process by the project analysis build process  */  
   "ProjProcessed":boolean,
      /**  Used by Project Analysis process.  */  
   "AsOfDate":string,
      /**  Used By Project Analysis Process  */  
   "AsOfSeq":number,
      /**  The expense category.  */  
   "ExpenseCategory":string,
      /**  The voucher or receipt number reference.  */  
   "VoucherReceiptNo":string,
      /**  The date for the voucher/receipt reference  */  
   "VoucherReceiptDate":string,
      /**  The remaining balance of the advance.  For advance request expense category, is initially set to the claim amount; will be zero for other categories.  Is reduced when other expenses that match the advance amount are invoiced.  */  
   "DocAdvanceBalance":number,
      /**  The amount that has been matched from advance requests to this expense.  */  
   "DocMatchedClaimAmt":number,
      /**  The Sales order that this expense is linked to.  */  
   "OrderNum":number,
      /**  The line number of the sales order that this expense is linked to  */  
   "OrderLine":number,
      /**  The release number of the sales order that this expense is linked to  */  
   "OrderRelNum":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  The label value for Units field.  */  
   "UnitsLabel":string,
      /**  A list of people who have approved the expense  */  
   "ApprovedBy":string,
      /**  A list of people who need to approve the expense  */  
   "PendingApprovalBy":string,
      /**  External field to display a descriptive status of the record  */  
   "DisplayStatus":string,
      /**  Exchange Rate Label  */  
   "XRateLabel":string,
      /**  Indicates if this record is selected to be submitted  */  
   "IsSelected":boolean,
      /**  The claim amount displayed to the user.  If the expense is non-reimbursable, the user will see zero for the claim amount.  */  
   "DispClaimAmt":number,
   "TreeNodeImageName":string,
      /**  Used by Time and Expense approval only, populated with the JobHead.ProjectID, not done as a linked field so it won't impact performance in processes other than Approval.  */  
   "ApprovalProjectID":string,
      /**  Used by Time and Expense approval only, populated with the Project.Description for ApprovalProjectID, not done as a linked field so it won't impact performance in processes other than Approval.  */  
   "ApprovalProjectDesc":string,
   "DspCreateTime":string,
   "DspChangeTime":string,
      /**  Used by Time and Expense approval only, populated with the JobHead.PhaseID, not done as a linked field so it won't impact performance in processes other than Approval.  */  
   "ApprovalPhaseID":string,
      /**  Used by Time and Expense approval only, not done as a linked field so it won't impact performance in processes other than Approval.  */  
   "ApprovalPhaseDesc":string,
      /**  If invoiced, the status of the invoice.  */  
   "InvoiceStatus":string,
      /**  Text to show the week date range (Sunday-Saturday) that corresponds to the EmpExpense.ExpenseDate such as "5/2/2009 - 5/9/2009"  */  
   "ExpWeek":string,
      /**  Text to show the day of the week that corresponds to the EmpExpense.ExpenseDate (Sunday, Monday, etc)  */  
   "ExpDay":string,
      /**  Text to show the month  (January, February, etc) that corresponds to the EmpExpense.ExpenseDate  */  
   "ExpMonth":string,
      /**  Indicates if the record has been submitted or not  */  
   "NotSubmitted":boolean,
      /**  The claim amount total displayed to the user.  If the expense is non-reimbursable, the user will see zero for the claim amount.  */  
   "DispTotalClaimAmt":number,
      /**  Indicates if multi-currency is licensed  */  
   "MultiCurrency":boolean,
   "ExpenseDisableDelete":boolean,
   "ExpenseDisableUpdate":boolean,
   "EnableClaimLockRate":boolean,
   "APInvLineAmt":number,
   "APInvLineTaxAmt":number,
   "APInvLineTotAmt":number,
      /**  Indicates if UnitRate is enabled  */  
   "EnableUnitRate":boolean,
   "EnableClaimCurrencyCode":boolean,
   "ExpenseCurrencyList":string,
      /**  The claim tax amount displayed to the user.  If the expense is non-reimbursable, the user will see zero for the claim tax amount.  */  
   "DispClaimTaxAmt":number,
      /**  Indicates if the submit button is enabled  */  
   "EnableSubmit":boolean,
      /**  Indicates if the recall button is enabled  */  
   "EnableRecall":boolean,
      /**  Indicates if the copy button is enabled  */  
   "EnableCopy":boolean,
      /**  Indicates if the user retrieving the record has access to view the row or not.  */  
   "HasAccessToRow":boolean,
      /**  Indicates if recall is available in approval entry  */  
   "EnableRecallAprv":boolean,
      /**  Used in approval entry.  Indicates if the approver has an open approval task.  */  
   "ApprvrHasOpenTask":boolean,
      /**  Indicates if this is the base currency.  Only one base currency is allowed  */  
   "ChargeCurrencyBaseCurr":boolean,
      /**  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  */  
   "ChargeCurrencyCurrencyID":string,
      /**   An extended description that can be used on documents such as
POs and invoices.  */  
   "ChargeCurrencyDocumentDesc":string,
      /**   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  */  
   "ChargeCurrencyCurrName":string,
      /**  Description of the currency  */  
   "ChargeCurrencyCurrDesc":string,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   "ChargeCurrencyCurrSymbol":string,
      /**  Description  */  
   "ChargeRateTypeDescription":string,
      /**   An extended description that can be used on documents such as
POs and invoices.  */  
   "ClaimCurrencyDocumentDesc":string,
      /**   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  */  
   "ClaimCurrencyCurrName":string,
      /**  Description of the currency  */  
   "ClaimCurrencyCurrDesc":string,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   "ClaimCurrencyCurrSymbol":string,
      /**  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  */  
   "ClaimCurrencyCurrencyID":string,
      /**  Indicates if this is the base currency.  Only one base currency is allowed  */  
   "ClaimCurrencyBaseCurr":boolean,
      /**  Description  */  
   "CurrRateGrpDescription":string,
      /**  This is the employee's full name. This is not directly maintainable. It is a concatenation of the FirstName + MiddleInitial + LastName fields. It exists so that it can be used in browses or where ever the complete name in a first, middle, last fashion is required.  */  
   "EmpBasicName":string,
      /**  Last name of employee  */  
   "EmpBasicLastName":string,
      /**  First name of employee.  */  
   "EmpBasicFirstName":string,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   "ExpCurrencyCurrSymbol":string,
      /**  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  */  
   "ExpCurrencyCurrencyID":string,
      /**   An extended description that can be used on documents such as
POs and invoices.  */  
   "ExpCurrencyDocumentDesc":string,
      /**   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  */  
   "ExpCurrencyCurrName":string,
      /**  Description of the currency  */  
   "ExpCurrencyCurrDesc":string,
      /**  Indicates if this is the base currency.  Only one base currency is allowed  */  
   "ExpCurrencyBaseCurr":boolean,
      /**  Reimbursable  */  
   "PayMethodReimbursable":boolean,
      /**  Indicated the type of payment with the following options:
 0 = Manual (default)
 1 = Electronic Interface
 2 = Check Printing
 3 = Payment Instrument Type 1
 4 = Payment Instrument Type 2  */  
   "PayMethodType":number,
      /**  Name of the payment method  */  
   "PayMethodName":string,
      /**   Indicates that invoices for the customer is summarized and sent as a sum to the bank without specifying the individual invoices.
A single bank transaction is created for the payment but what?s actually sent to the bank will be determined by the electronic interface plug-in program.
Only enabled if type is set to ?Electronic Interface?  */  
   "PayMethodSummarizePerCustomer":boolean,
      /**  Full description of Project Management Code.  */  
   "ProjectDescription":string,
      /**  Description  */  
   "ProjPhaseDescription":string,
      /**  When an expense charge, indicates if the code is chargeable.  */  
   "PurMiscExpChargeable":boolean,
      /**  Description of the Miscellaneous Charge. Used as a default to Orders and Invoices.  */  
   "PurMiscDescription":string,
      /**  When an expense charge, indicates if the code is unit based.  */  
   "PurMiscExpUnitBased":boolean,
      /**  Description of the task set.  */  
   "TaskSetTaskSetDescription":string,
      /**  The type of workflow of this task set.  Possible values are "CRM" - CRM related tasks and "ECO" - ECO tasks  */  
   "TaskSetWorkflowType":string,
      /**  Full description for the Tax Region.  */  
   "TaxRgnDescription":string,
      /**  Country Name. Printed as last line of mailing address. Can be blank.  */  
   "VendorCountry":string,
      /**  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  */  
   "VendorTermsCode":string,
      /**  Third address line of the Supplier  */  
   "VendorAddress3":string,
      /**  First address line of the Supplier  */  
   "VendorAddress1":string,
      /**  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  */  
   "VendorName":string,
      /**  A unique code that identifies the currency.  */  
   "VendorCurrencyCode":string,
      /**  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  */  
   "VendorVendorID":string,
      /**  City portion of the address of the Supplier  */  
   "VendorCity":string,
      /**  Can be blank.  */  
   "VendorState":string,
      /**  Second address line of the Supplier  */  
   "VendorAddress2":string,
      /**  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  */  
   "VendorDefaultFOB":string,
      /**  Postal Code or Zip code portion of the address of the Supplier  */  
   "VendorZIP":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_EmpExpenseRow{
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
      /**  The FromEffectiveDate from ExpenseTypeUnitBased that was used to determine default values for Units and UnitRate.  This combined with ExpenseTypeCode point to a unique ExpenseTypeUnitBased record.  */  
   "UBFromEffectiveDate":string,
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
      /**  The charge currency.  This is derived from the currency on the related project.  */  
   "ChargeCurrencyCode":string,
      /**  The charge exchange rate.  This is derived from the exchange rate on the related project.  */  
   "ChargeExchangeRate":number,
      /**  The charge rate group code.  This is derived from the rate group code on the related projec.t  */  
   "ChargeRateGrpCode":string,
      /**  The charge amount of the expense in the charge currency.  */  
   "DocChargeAmt":number,
      /**  The date the expense received final approval.  */  
   "ApprovedDate":string,
      /**  The supplier number used on the employee of the expense.  */  
   "VendorNum":number,
      /**  The ap invoice number the expense was invoiced on.  */  
   "InvoiceNum":string,
      /**  The invoice line created for this expense.  */  
   "InvoiceLine":number,
      /**  Link to Task set  */  
   "TaskSetID":string,
      /**  Indicates if this expense is a reversal (full or partial) of an existing expense.  */  
   "IsReversal":boolean,
      /**  Reversed Expense Number  */  
   "ReversedExpenseNum":number,
      /**  Userid of the user who created the record.  */  
   "CreatedBy":string,
      /**  The date the record was created.  */  
   "CreateDate":string,
      /**  The time the record was created (in seconds since midnight)  */  
   "CreateTime":number,
      /**  Userid of the user who made the last change to this record.  */  
   "ChangedBy":string,
      /**  The date the record was last changed.  */  
   "ChangeDate":string,
      /**  The time the record was last changed (in seconds since midnight)  */  
   "ChangeTime":number,
      /**  The Currently active Stage changing task  */  
   "ActiveTaskID":string,
      /**  The Last Complete Milestone task  */  
   "LastTaskID":string,
      /**  The currency the claim amounts are in.  */  
   "ClaimCurrencyCode":string,
      /**  The exchange rate between the claim currency and the base currency based on expense date.  */  
   "ClaimExchangeRate":number,
      /**  Used with the currency module.  When TRUE the claim currency rate can be changed by the user and cannot be changed by the system.  */  
   "ClaimLockRate":boolean,
      /**  The claim rate group code.  */  
   "ClaimRateGrpCode":string,
      /**  The tax of the claim in the claim currency.  */  
   "DocClaimTaxAmt":number,
      /**  The amount of the claim in the claim currency.  */  
   "DocClaimAmt":number,
      /**  The total amount of the claim in the claim currency.  This value includes taxes.  */  
   "DocTotalClaimAmt":number,
      /**  The miscellaneous charge code for this expense.  */  
   "MiscCode":string,
      /**  The user who submitted the expense  */  
   "SubmittedBy":string,
      /**  The identifier of the workflow stage.  */  
   "CurrentWFStageID":string,
      /**  The identifier of the workflow group  */  
   "WFGroupID":string,
      /**  This indicates if the workflow for this group is complete.  */  
   "WFComplete":boolean,
      /**  Indicates if approval is required for this transaction.  */  
   "ApprovalRequired":boolean,
      /**  Indicates if the record is tax exempt.  If field is non-blank it is considered exempt.  */  
   "TaxExempt":string,
      /**  If set to true, the tax calculation logic will retrieve the default SalesTax ids for the expense before calculating taxes. It will also be reset to true if the TaxConnectCalc flag switches from true to false.  */  
   "GetDfltTaxIds":boolean,
      /**  If true, the EmpExpenseTax records tied to this release are calculated using Tax Connect logic. If  false, taxes are calculated using the standard calc methods.  */  
   "TaxConnectCalc":boolean,
      /**  Expense Withholding Tax Amount.  */  
   "DocExpWithholdAmt":number,
      /**  Claim Withholding Tax Amount.  */  
   "DocClaimWithholdAmt":number,
      /**  Indicates if the expense is reimbursable.  */  
   "Reimbursable":boolean,
      /**  The tax of the claim in the charge currency.  */  
   "DocChargeTaxAmt":number,
      /**  The total charge amount in the charge currency.  This value includes taxes.  */  
   "DocTotalChargeAmt":number,
      /**  The exchange rate between the claim currency and the base currency.  */  
   "ClaimToBaseExchangeRate":number,
      /**  Job Number of the misc charge jobmtl record  */  
   "JobNum":string,
      /**  Assembly sequence number of the misc charge jobmtl record  */  
   "AssemblySeq":number,
      /**  Material sequence of the misc charge jobmtl record  */  
   "MtlSeq":number,
      /**  Indicates if the expense has been invoiced.  */  
   "Invoiced":boolean,
      /**  Expense Comment  */  
   "ExpCommentText":string,
      /**  Expense Comment Instruction  */  
   "ExpCommentInstr":string,
      /**  Indicates that this record has been process by the project analysis build process  */  
   "ProjProcessed":boolean,
      /**  Used by Project Analysis process.  */  
   "AsOfDate":string,
      /**  Used By Project Analysis Process  */  
   "AsOfSeq":number,
      /**  The expense category.  */  
   "ExpenseCategory":string,
      /**  The voucher or receipt number reference.  */  
   "VoucherReceiptNo":string,
      /**  The date for the voucher/receipt reference  */  
   "VoucherReceiptDate":string,
      /**  The remaining balance of the advance.  For advance request expense category, is initially set to the claim amount; will be zero for other categories.  Is reduced when other expenses that match the advance amount are invoiced.  */  
   "DocAdvanceBalance":number,
      /**  The amount that has been matched from advance requests to this expense.  */  
   "DocMatchedClaimAmt":number,
      /**  The Sales order that this expense is linked to.  */  
   "OrderNum":number,
      /**  The line number of the sales order that this expense is linked to  */  
   "OrderLine":number,
      /**  The release number of the sales order that this expense is linked to  */  
   "OrderRelNum":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  PartTranSysRowID  */  
   "PartTranSysRowID":string,
      /**  ExpenseAutoSubmit  */  
   "ExpenseAutoSubmit":boolean,
      /**  Related to Epicor FSA  */  
   "EpicorFSA":boolean,
      /**  MobileExpense  */  
   "MobileExpense":boolean,
   "APInvLineAmt":number,
   "APInvLineTaxAmt":number,
      /**  Used by Time and Expense approval only, not done as a linked field so it won't impact performance in processes other than Approval.  */  
   "ApprovalPhaseDesc":string,
      /**  Used by Time and Expense approval only, populated with the JobHead.PhaseID, not done as a linked field so it won't impact performance in processes other than Approval.  */  
   "ApprovalPhaseID":string,
      /**  Used by Time and Expense approval only, populated with the Project.Description for ApprovalProjectID, not done as a linked field so it won't impact performance in processes other than Approval.  */  
   "ApprovalProjectDesc":string,
      /**  Used by Time and Expense approval only, populated with the JobHead.ProjectID, not done as a linked field so it won't impact performance in processes other than Approval.  */  
   "ApprovalProjectID":string,
      /**  A list of people who have approved the expense  */  
   "ApprovedBy":string,
      /**  Used in approval entry.  Indicates if the approver has an open approval task.  */  
   "ApprvrHasOpenTask":boolean,
      /**  The claim amount displayed to the user.  If the expense is non-reimbursable, the user will see zero for the claim amount.  */  
   "DispClaimAmt":number,
      /**  The claim tax amount displayed to the user.  If the expense is non-reimbursable, the user will see zero for the claim tax amount.  */  
   "DispClaimTaxAmt":number,
      /**  External field to display a descriptive status of the record  */  
   "DisplayStatus":string,
      /**  The claim amount total displayed to the user.  If the expense is non-reimbursable, the user will see zero for the claim amount.  */  
   "DispTotalClaimAmt":number,
   "DspChangeTime":string,
   "DspCreateTime":string,
   "EnableClaimCurrencyCode":boolean,
   "EnableClaimLockRate":boolean,
      /**  Indicates if the copy button is enabled  */  
   "EnableCopy":boolean,
      /**  Indicates if the recall button is enabled  */  
   "EnableRecall":boolean,
      /**  Indicates if recall is available in approval entry  */  
   "EnableRecallAprv":boolean,
      /**  Indicates if the submit button is enabled  */  
   "EnableSubmit":boolean,
      /**  Indicates if UnitRate is enabled  */  
   "EnableUnitRate":boolean,
      /**  Text to show the day of the week that corresponds to the EmpExpense.ExpenseDate (Sunday, Monday, etc)  */  
   "ExpDay":string,
   "ExpenseCurrencyList":string,
   "ExpenseDisableDelete":boolean,
   "ExpenseDisableUpdate":boolean,
      /**  Text to show the month  (January, February, etc) that corresponds to the EmpExpense.ExpenseDate  */  
   "ExpMonth":string,
      /**  Text to show the week date range (Sunday-Saturday) that corresponds to the EmpExpense.ExpenseDate such as "5/2/2009 - 5/9/2009"  */  
   "ExpWeek":string,
      /**  Service Order number generated on FSA, stored on FSAExtData db table.  */  
   "FSAServiceOrderNum":number,
      /**  Service Order Resource generated on FSA, stored on FSAExtData db table.  */  
   "FSAServiceOrderResourceNum":number,
      /**  Indicates if the user retrieving the record has access to view the row or not.  */  
   "HasAccessToRow":boolean,
      /**  Indicates if the expense detail has attachments  */  
   "HasAttachments":boolean,
      /**  Indicates if the expense detail has comments  */  
   "HasComments":boolean,
      /**  If invoiced, the status of the invoice.  */  
   "InvoiceStatus":string,
      /**  Indicates if this record is selected to be submitted  */  
   "IsSelected":boolean,
      /**  Indicates if multi-currency is licensed  */  
   "MultiCurrency":boolean,
   "NewDifDateFlag":boolean,
      /**  Indicates if the record has been submitted or not  */  
   "NotSubmitted":boolean,
      /**  A list of people who need to approve the expense  */  
   "PendingApprovalBy":string,
   "TreeNodeImageName":string,
      /**  The label value for Units field.  */  
   "UnitsLabel":string,
      /**  Exchange Rate Label  */  
   "XRateLabel":string,
   "APInvLineTotAmt":number,
      /**  Indicates of the row is selected for submit or recall  */  
   "RowSelected":boolean,
      /**  Start date/time for calendar appoinment  */  
   "AppointmentStart":string,
      /**  End date/time for calendar appoinment  */  
   "AppointmentEnd":string,
      /**  Title to display for the calendar appointment  */  
   "AppointmentTitle":string,
      /**  Is calendar appointment all day  */  
   "AppointmentIsAllDay":boolean,
   "BitFlag":number,
   "ChargeCurrencyCurrSymbol":string,
   "ChargeCurrencyCurrDesc":string,
   "ChargeCurrencyCurrName":string,
   "ChargeCurrencyCurrencyID":string,
   "ChargeCurrencyDocumentDesc":string,
   "ChargeCurrencyBaseCurr":boolean,
   "ChargeRateGrpDescription":string,
   "ClaimCurrencyCurrName":string,
   "ClaimCurrencyBaseCurr":boolean,
   "ClaimCurrencyDocumentDesc":string,
   "ClaimCurrencyCurrSymbol":string,
   "ClaimCurrencyCurrDesc":string,
   "ClaimCurrencyCurrencyID":string,
   "CurrRateGrpDescription":string,
   "EmpBasicName":string,
   "EmpBasicFirstName":string,
   "EmpBasicLastName":string,
   "ExpCurrencyDocumentDesc":string,
   "ExpCurrencyCurrSymbol":string,
   "ExpCurrencyBaseCurr":boolean,
   "ExpCurrencyCurrName":string,
   "ExpCurrencyCurrDesc":string,
   "ExpCurrencyCurrencyID":string,
   "PayMethodType":number,
   "PayMethodReimbursable":boolean,
   "PayMethodSummarizePerCustomer":boolean,
   "PayMethodName":string,
   "ProjectDescription":string,
   "ProjPhaseDescription":string,
   "PurMiscExpUnitBased":boolean,
   "PurMiscExpChargeable":boolean,
   "PurMiscDescription":string,
   "TaskSetWorkflowType":string,
   "TaskSetTaskSetDescription":string,
   "TaxRgnDescription":string,
   "VendorAddress1":string,
   "VendorCurrencyCode":string,
   "VendorVendorID":string,
   "VendorAddress2":string,
   "VendorTermsCode":string,
   "VendorAddress3":string,
   "VendorState":string,
   "VendorCountry":string,
   "VendorZIP":string,
   "VendorCity":string,
   "VendorDefaultFOB":string,
   "VendorName":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_EmpExpenseTaxRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The employee the expense record is for.  */  
   "EmpID":string,
      /**  Internal identifier of the EmpExpense record.  This with EmpID makes the record unique.  */  
   "EmpExpenseNum":number,
      /**  Descriptive code assigned by user which uniquely identifies a Sales Tax master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  */  
   "TaxCode":string,
      /**  Rate code  */  
   "RateCode":string,
      /**   Used to allow a second tax record using the same tax code on an expense.  When the sales tax field EcAquisition is checked then 2 expense tax records are created.
NOTE:  This field is now used in VAT Reverse Charge logic.  If an invoice line is marked for Reverse Charge, a second line is created just like in the ECAcquisition logic. To distinguish the two scenarios, the ReverseCharge flag will be set to true if the second line is for Reverse Charge.  */  
   "ECAcquisitionSeq":number,
      /**  The reportable amount to the tax jurisdiction in the expense currency.  */  
   "ExpReportableAmt":number,
      /**  The reportable amount to the tax jurisdiction in the claim currency.  */  
   "ClaimReportableAmt":number,
      /**  Taxable Amount for this expense in the expense currency  */  
   "ExpTaxableAmt":number,
      /**  Taxable Amount for this expense in the claim currency.  */  
   "ClaimTaxableAmt":number,
      /**  The tax percentage rate that is used for this expense. This is defaulted from the SalesTax.Percent.  */  
   "Percent":number,
      /**  Sales Tax amount for the corresponding taxable sales amount in the expense currency.  */  
   "ExpTaxAmt":number,
      /**  Sales Tax amount for the corresponding taxable sales amount in the claim currency  */  
   "ClaimTaxAmt":number,
      /**  Indicates if the tax calculations are to be performed manually.  When this field is set the Reportable, Taxable, and TaxAmount fields are enabled.  When it is NOT set these fields are DISABLED and the system will perform all of the Reportable, Taxable, and TaxAmount calculations.  Defaults from the SalesTax.Manual field.  */  
   "Manual":boolean,
      /**  Userid of the user who created the record.  */  
   "CreatedBy":string,
      /**  The date the record was created.  */  
   "CreateDate":string,
      /**  The time the record was created (in seconds since midnight)  */  
   "CreateTime":number,
      /**  Userid of user who made the last change to this record.  */  
   "ChangedBy":string,
      /**  The date that the record was last changed  */  
   "ChangeDate":string,
      /**  The time that the record was last change (seconds since midnight)  */  
   "ChangeTime":number,
      /**  Reverse Charge.  */  
   "ReverseCharge":boolean,
      /**  Collection Type  */  
   "CollectionType":number,
      /**  Timing of when to report taxes  */  
   "Timing":number,
      /**  Exemption Type  */  
   "ExemptType":number,
      /**  Exemption Percent  */  
   "ExemptPercent":number,
      /**  Resolution number  */  
   "ResolutionNum":string,
      /**  Resolution Date  */  
   "ResolutionDate":string,
      /**  Tax Rate Date  */  
   "TaxRateDate":string,
      /**  Balance of the Taxable amount that has been deferred until payment.  In expense currency  */  
   "ExpDefTaxableAmt":number,
      /**  Balance of the Taxable amount that has been deferred until payment.  In claim currency.  */  
   "ClaimDefTaxableAmt":number,
      /**  Balance of the Tax amount that has been deferred until payment.  In expense currency.  */  
   "ExpDefTaxAmt":number,
      /**  Balance of the Tax amount that has been deferred until payment.  In claim currency  */  
   "ClaimDefTaxAmt":number,
      /**  This record was manually added (not in Liability) but will use the standard calculations  */  
   "ManAdd":boolean,
      /**  Deducatable Tax Amount in expense currency  */  
   "ExpDedTaxAmt":number,
      /**  Deducatable Tax Amount in claim currency  */  
   "ClaimDedTaxAmt":number,
      /**  Fixed Tax Amount in expense currency  */  
   "ExpFixedAmount":number,
      /**  Document Fixed Tax Amount in claim currency  */  
   "ClaimFixedAmount":number,
      /**  Unique Identifier for Legal Text  */  
   "TextCode":string,
      /**  Difference between tax calculated in document rate less tax calculated in tax rate in expense currency  */  
   "ExpTaxAmtVar":number,
      /**  Difference between tax calculated in document rate less tax calculated in tax rate in claim currency  */  
   "ClaimTaxAmtVar":number,
      /**  System calculated Taxable amount for this expense in the claim currency  */  
   "SysCalcClaimTaxableAmt":number,
      /**  System calculated Taxable amount for this expense in the expense currency.  */  
   "SysCalcExpTaxableAmt":number,
      /**  System calculated reportable amount to the tax jurisdiction in the expense currency  */  
   "SysCalcExpReportableAmt":number,
      /**  System calculated reportable sales amount to the tax jurisdiction expressed in the claim currency.  */  
   "SysCalcClaimReportableAmt":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "ExpCurrencyCode":string,
   "ExpCurrencyDesc":string,
   "ClaimCurrencyCode":string,
   "ClaimCurrencyDesc":string,
      /**  Unique identifier of related integration record.  */  
   "IntExternalKey":string,
   "BitFlag":number,
   "RateCodeDescription":string,
   "TaxCodeDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param ipSalesRepCode
      @param ipAction
      @param ipComment
      @param ds
   */  
export interface ApproveReject_input{
      /**  The sales Rep Code of the approver.  */  
   ipSalesRepCode:string,
      /**  Action to take A = approver, R = reject.  */  
   ipAction:string,
      /**  Comment text if comments are to be created.  */  
   ipComment:string,
   ds:Erp_Tablesets_EmpExpenseTableset[],
}

export interface ApproveReject_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EmpExpenseTableset[],
   outMessage:string,
}
}

   /** Required : 
      @param ProposedClaimCurrencyCode
      @param ds
   */  
export interface ChangeEmpExpenseClaimCurrencyCode_input{
      /**  The proposed claim currency code  */  
   ProposedClaimCurrencyCode:string,
   ds:Erp_Tablesets_EmpExpenseTableset[],
}

export interface ChangeEmpExpenseClaimCurrencyCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EmpExpenseTableset[],
}
}

   /** Required : 
      @param ProposedClaimExchangeRate
      @param ds
   */  
export interface ChangeEmpExpenseClaimExchangeRate_input{
      /**  The proposed claim exchange rate  */  
   ProposedClaimExchangeRate:number,
   ds:Erp_Tablesets_EmpExpenseTableset[],
}

export interface ChangeEmpExpenseClaimExchangeRate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EmpExpenseTableset[],
}
}

   /** Required : 
      @param ProposedClaimLockRate
      @param ds
   */  
export interface ChangeEmpExpenseClaimLockRate_input{
      /**  The proposed claim lock rate  */  
   ProposedClaimLockRate:boolean,
   ds:Erp_Tablesets_EmpExpenseTableset[],
}

export interface ChangeEmpExpenseClaimLockRate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EmpExpenseTableset[],
}
}

   /** Required : 
      @param ProposedClaimRateGrpCode
      @param ds
   */  
export interface ChangeEmpExpenseClaimRateGrpCode_input{
      /**  The proposed expense currency code  */  
   ProposedClaimRateGrpCode:string,
   ds:Erp_Tablesets_EmpExpenseTableset[],
}

export interface ChangeEmpExpenseClaimRateGrpCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EmpExpenseTableset[],
}
}

   /** Required : 
      @param ProposedDispClaimAmt
      @param ds
   */  
export interface ChangeEmpExpenseDispClaimAmt_input{
      /**  The proposed claim amount  */  
   ProposedDispClaimAmt:number,
   ds:Erp_Tablesets_EmpExpenseTableset[],
}

export interface ChangeEmpExpenseDispClaimAmt_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EmpExpenseTableset[],
}
}

   /** Required : 
      @param ProposedDocExpenseAmt
      @param ds
   */  
export interface ChangeEmpExpenseDocExpenseAmt_input{
      /**  The proposed doc expense amount  */  
   ProposedDocExpenseAmt:number,
   ds:Erp_Tablesets_EmpExpenseTableset[],
}

export interface ChangeEmpExpenseDocExpenseAmt_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EmpExpenseTableset[],
}
}

   /** Required : 
      @param ProposedExpCurrencyCode
      @param ds
   */  
export interface ChangeEmpExpenseExpCurrencyCode_input{
      /**  The proposed expense currency code  */  
   ProposedExpCurrencyCode:string,
   ds:Erp_Tablesets_EmpExpenseTableset[],
}

export interface ChangeEmpExpenseExpCurrencyCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EmpExpenseTableset[],
}
}

   /** Required : 
      @param ProposedExpenseDate
      @param ds
   */  
export interface ChangeEmpExpenseExpenseDate_input{
      /**  The proposed expense date  */  
   ProposedExpenseDate:string,
   ds:Erp_Tablesets_EmpExpenseTableset[],
}

export interface ChangeEmpExpenseExpenseDate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EmpExpenseTableset[],
}
}

   /** Required : 
      @param ProposedIndirect
      @param ds
   */  
export interface ChangeEmpExpenseIndirect_input{
      /**  The proposed indirect value  */  
   ProposedIndirect:boolean,
   ds:Erp_Tablesets_EmpExpenseTableset[],
}

export interface ChangeEmpExpenseIndirect_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EmpExpenseTableset[],
}
}

   /** Required : 
      @param ProposedMiscCode
      @param ds
   */  
export interface ChangeEmpExpenseMiscCode_input{
      /**  The proposed miscellaneous code  */  
   ProposedMiscCode:string,
   ds:Erp_Tablesets_EmpExpenseTableset[],
}

export interface ChangeEmpExpenseMiscCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EmpExpenseTableset[],
}
}

   /** Required : 
      @param ProposedPMUID
      @param ds
   */  
export interface ChangeEmpExpensePayMethod_input{
      /**  The proposed pay method id  */  
   ProposedPMUID:number,
   ds:Erp_Tablesets_EmpExpenseTableset[],
}

export interface ChangeEmpExpensePayMethod_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EmpExpenseTableset[],
}
}

   /** Required : 
      @param ProposedPhaseID
      @param ds
   */  
export interface ChangeEmpExpensePhaseID_input{
      /**  The proposed phase  */  
   ProposedPhaseID:string,
   ds:Erp_Tablesets_EmpExpenseTableset[],
}

export interface ChangeEmpExpensePhaseID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EmpExpenseTableset[],
}
}

   /** Required : 
      @param ProposedProjectID
      @param ds
   */  
export interface ChangeEmpExpenseProjectID_input{
      /**  The proposed project  */  
   ProposedProjectID:string,
   ds:Erp_Tablesets_EmpExpenseTableset[],
}

export interface ChangeEmpExpenseProjectID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EmpExpenseTableset[],
}
}

   /** Required : 
      @param ProposedQuickEntryCode
      @param ds
   */  
export interface ChangeEmpExpenseQuickEntryCode_input{
      /**  The proposed quick entry code  */  
   ProposedQuickEntryCode:string,
   ds:Erp_Tablesets_EmpExpenseTableset[],
}

export interface ChangeEmpExpenseQuickEntryCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EmpExpenseTableset[],
}
}

   /** Required : 
      @param ProposedUnitRate
      @param ds
   */  
export interface ChangeEmpExpenseUnitRate_input{
      /**  The proposed unit rate  */  
   ProposedUnitRate:number,
   ds:Erp_Tablesets_EmpExpenseTableset[],
}

export interface ChangeEmpExpenseUnitRate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EmpExpenseTableset[],
}
}

   /** Required : 
      @param ProposedUnits
      @param ds
   */  
export interface ChangeEmpExpenseUnits_input{
      /**  The proposed units  */  
   ProposedUnits:number,
   ds:Erp_Tablesets_EmpExpenseTableset[],
}

export interface ChangeEmpExpenseUnits_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EmpExpenseTableset[],
}
}

   /** Required : 
      @param ipSalesRepCode
      @param ds
   */  
export interface CheckRecallFromApproval_input{
      /**  The sales Rep Code of the approver.  */  
   ipSalesRepCode:string,
   ds:Erp_Tablesets_EmpExpenseTableset[],
}

export interface CheckRecallFromApproval_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EmpExpenseTableset[],
   outRecallMsg:string,
}
}

   /** Required : 
      @param ds
      @param empID
      @param empExpenseNum
   */  
export interface CopyEmpExpenseByID_input{
   ds:Erp_Tablesets_EmpExpenseTableset[],
      /**  Employee ID  */  
   empID:string,
      /**  EmpExpense Number  */  
   empExpenseNum:number,
}

export interface CopyEmpExpenseByID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EmpExpenseTableset[],
   messageText:string,
}
}

   /** Required : 
      @param ds
   */  
export interface CopyEmpExpense_input{
   ds:Erp_Tablesets_EmpExpenseTableset[],
}

export interface CopyEmpExpense_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EmpExpenseTableset[],
   cMessageText:string,
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

   /** Required : 
      @param ds
   */  
export interface DeleteExpense_input{
   ds:Erp_Tablesets_EmpExpenseTableset[],
}

export interface DeleteExpense_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EmpExpenseTableset[],
}
}

   /** Required : 
      @param empExpenseRow
   */  
export interface EmpExpenseAfterGetRowsWrapper_input{
   empExpenseRow:Erp_Tablesets_EmpExpenseRow[],
}

export interface EmpExpenseAfterGetRowsWrapper_output{
parameters : {
      /**  output parameters  */  
   empExpenseRow:Erp_Tablesets_EmpExpenseRow[],
}
}

   /** Required : 
      @param empExpenseCommentRow
   */  
export interface EmpExpenseCommentAfterGetRowsWrapper_input{
   empExpenseCommentRow:Erp_Tablesets_EmpExpenseCommentRow[],
}

export interface EmpExpenseCommentAfterGetRowsWrapper_output{
parameters : {
      /**  output parameters  */  
   empExpenseCommentRow:Erp_Tablesets_EmpExpenseCommentRow[],
}
}

export interface EmpExpenseRetrieveOptionsClause_output{
parameters : {
      /**  output parameters  */  
   empExpenseRetrieveOptionsClause:string,
}
}

export interface Erp_Tablesets_EmpExpenseAttchRow{
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

export interface Erp_Tablesets_EmpExpenseCommentRow{
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
      /**  Userid of the user who made the last change to this record.  */  
   ChangedBy:string,
      /**  The date the record was last changed.  */  
   ChangeDate:string,
      /**  The time the record was last changed (in seconds since midnight)  */  
   ChangeTime:number,
      /**  The identifier of the Task record the comment is related to.  Can be zero, which indicates the comment is not related to a specific task.  */  
   TaskSeqNum:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   DspChangeTime:string,
   DspCreateTime:string,
      /**  Submit comment instructions  */  
   SubmitCommentInstr:string,
   TreeNodeImageName:string,
      /**  Unique identifier of related integration record.  */  
   IntExternalKey:string,
      /**  List of valid comment types for Expense Entry  */  
   ExpEntryCommentTypeList:string,
   CommentTypeDesc:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_EmpExpenseListRow{
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
      /**  The FromEffectiveDate from ExpenseTypeUnitBased that was used to determine default values for Units and UnitRate.  This combined with ExpenseTypeCode point to a unique ExpenseTypeUnitBased record.  */  
   UBFromEffectiveDate:string,
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
      /**  The charge currency.  This is derived from the currency on the related project.  */  
   ChargeCurrencyCode:string,
      /**  The charge exchange rate.  This is derived from the exchange rate on the related project.  */  
   ChargeExchangeRate:number,
      /**  The charge rate group code.  This is derived from the rate group code on the related projec.t  */  
   ChargeRateGrpCode:string,
      /**  The charge amount of the expense in the charge currency.  */  
   DocChargeAmt:number,
      /**  The date the expense received final approval.  */  
   ApprovedDate:string,
      /**  The supplier number used on the employee of the expense.  */  
   VendorNum:number,
      /**  The ap invoice number the expense was invoiced on.  */  
   InvoiceNum:string,
      /**  The invoice line created for this expense.  */  
   InvoiceLine:number,
      /**  Link to Task set  */  
   TaskSetID:string,
      /**  Indicates if this expense is a reversal (full or partial) of an existing expense.  */  
   IsReversal:boolean,
      /**  Reversed Expense Number  */  
   ReversedExpenseNum:number,
      /**  Userid of the user who created the record.  */  
   CreatedBy:string,
      /**  The date the record was created.  */  
   CreateDate:string,
      /**  The time the record was created (in seconds since midnight)  */  
   CreateTime:number,
      /**  Userid of the user who made the last change to this record.  */  
   ChangedBy:string,
      /**  The date the record was last changed.  */  
   ChangeDate:string,
      /**  The time the record was last changed (in seconds since midnight)  */  
   ChangeTime:number,
      /**  The Currently active Stage changing task  */  
   ActiveTaskID:string,
      /**  The Last Complete Milestone task  */  
   LastTaskID:string,
      /**  The currency the claim amounts are in.  */  
   ClaimCurrencyCode:string,
      /**  The exchange rate between the claim currency and the base currency based on expense date.  */  
   ClaimExchangeRate:number,
      /**  Used with the currency module.  When TRUE the claim currency rate can be changed by the user and cannot be changed by the system.  */  
   ClaimLockRate:boolean,
      /**  The claim rate group code.  */  
   ClaimRateGrpCode:string,
      /**  The tax of the claim in the claim currency.  */  
   DocClaimTaxAmt:number,
      /**  The amount of the claim in the claim currency.  */  
   DocClaimAmt:number,
      /**  The total amount of the claim in the claim currency.  This value includes taxes.  */  
   DocTotalClaimAmt:number,
      /**  The miscellaneous charge code for this expense.  */  
   MiscCode:string,
      /**  The user who submitted the expense  */  
   SubmittedBy:string,
      /**  The identifier of the workflow stage.  */  
   CurrentWFStageID:string,
      /**  The identifier of the workflow group  */  
   WFGroupID:string,
      /**  This indicates if the workflow for this group is complete.  */  
   WFComplete:boolean,
      /**  Indicates if approval is required for this transaction.  */  
   ApprovalRequired:boolean,
      /**  Indicates if the record is tax exempt.  If field is non-blank it is considered exempt.  */  
   TaxExempt:string,
      /**  If set to true, the tax calculation logic will retrieve the default SalesTax ids for the expense before calculating taxes. It will also be reset to true if the TaxConnectCalc flag switches from true to false.  */  
   GetDfltTaxIds:boolean,
      /**  If true, the EmpExpenseTax records tied to this release are calculated using Tax Connect logic. If  false, taxes are calculated using the standard calc methods.  */  
   TaxConnectCalc:boolean,
      /**  Expense Withholding Tax Amount.  */  
   DocExpWithholdAmt:number,
      /**  Claim Withholding Tax Amount.  */  
   DocClaimWithholdAmt:number,
      /**  Indicates if the expense is reimbursable.  */  
   Reimbursable:boolean,
      /**  The tax of the claim in the charge currency.  */  
   DocChargeTaxAmt:number,
      /**  The total charge amount in the charge currency.  This value includes taxes.  */  
   DocTotalChargeAmt:number,
      /**  The exchange rate between the claim currency and the base currency.  */  
   ClaimToBaseExchangeRate:number,
      /**  Job Number of the misc charge jobmtl record  */  
   JobNum:string,
      /**  Assembly sequence number of the misc charge jobmtl record  */  
   AssemblySeq:number,
      /**  Material sequence of the misc charge jobmtl record  */  
   MtlSeq:number,
      /**  Indicates if the expense has been invoiced.  */  
   Invoiced:boolean,
      /**  Expense Comment  */  
   ExpCommentText:string,
      /**  Expense Comment Instruction  */  
   ExpCommentInstr:string,
      /**  Indicates that this record has been process by the project analysis build process  */  
   ProjProcessed:boolean,
      /**  Used by Project Analysis process.  */  
   AsOfDate:string,
      /**  Used By Project Analysis Process  */  
   AsOfSeq:number,
      /**  The expense category.  */  
   ExpenseCategory:string,
      /**  The voucher or receipt number reference.  */  
   VoucherReceiptNo:string,
      /**  The date for the voucher/receipt reference  */  
   VoucherReceiptDate:string,
      /**  The remaining balance of the advance.  For advance request expense category, is initially set to the claim amount; will be zero for other categories.  Is reduced when other expenses that match the advance amount are invoiced.  */  
   DocAdvanceBalance:number,
      /**  The amount that has been matched from advance requests to this expense.  */  
   DocMatchedClaimAmt:number,
      /**  The Sales order that this expense is linked to.  */  
   OrderNum:number,
      /**  The line number of the sales order that this expense is linked to  */  
   OrderLine:number,
      /**  The release number of the sales order that this expense is linked to  */  
   OrderRelNum:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  The label value for Units field.  */  
   UnitsLabel:string,
      /**  A list of people who have approved the expense  */  
   ApprovedBy:string,
      /**  A list of people who need to approve the expense  */  
   PendingApprovalBy:string,
      /**  External field to display a descriptive status of the record  */  
   DisplayStatus:string,
      /**  Exchange Rate Label  */  
   XRateLabel:string,
      /**  Indicates if this record is selected to be submitted  */  
   IsSelected:boolean,
      /**  The claim amount displayed to the user.  If the expense is non-reimbursable, the user will see zero for the claim amount.  */  
   DispClaimAmt:number,
   TreeNodeImageName:string,
      /**  Used by Time and Expense approval only, populated with the JobHead.ProjectID, not done as a linked field so it won't impact performance in processes other than Approval.  */  
   ApprovalProjectID:string,
      /**  Used by Time and Expense approval only, populated with the Project.Description for ApprovalProjectID, not done as a linked field so it won't impact performance in processes other than Approval.  */  
   ApprovalProjectDesc:string,
   DspCreateTime:string,
   DspChangeTime:string,
      /**  Used by Time and Expense approval only, populated with the JobHead.PhaseID, not done as a linked field so it won't impact performance in processes other than Approval.  */  
   ApprovalPhaseID:string,
      /**  Used by Time and Expense approval only, not done as a linked field so it won't impact performance in processes other than Approval.  */  
   ApprovalPhaseDesc:string,
      /**  If invoiced, the status of the invoice.  */  
   InvoiceStatus:string,
      /**  Text to show the week date range (Sunday-Saturday) that corresponds to the EmpExpense.ExpenseDate such as "5/2/2009 - 5/9/2009"  */  
   ExpWeek:string,
      /**  Text to show the day of the week that corresponds to the EmpExpense.ExpenseDate (Sunday, Monday, etc)  */  
   ExpDay:string,
      /**  Text to show the month  (January, February, etc) that corresponds to the EmpExpense.ExpenseDate  */  
   ExpMonth:string,
      /**  Indicates if the record has been submitted or not  */  
   NotSubmitted:boolean,
      /**  The claim amount total displayed to the user.  If the expense is non-reimbursable, the user will see zero for the claim amount.  */  
   DispTotalClaimAmt:number,
      /**  Indicates if multi-currency is licensed  */  
   MultiCurrency:boolean,
   ExpenseDisableDelete:boolean,
   ExpenseDisableUpdate:boolean,
   EnableClaimLockRate:boolean,
   APInvLineAmt:number,
   APInvLineTaxAmt:number,
   APInvLineTotAmt:number,
      /**  Indicates if UnitRate is enabled  */  
   EnableUnitRate:boolean,
   EnableClaimCurrencyCode:boolean,
   ExpenseCurrencyList:string,
      /**  The claim tax amount displayed to the user.  If the expense is non-reimbursable, the user will see zero for the claim tax amount.  */  
   DispClaimTaxAmt:number,
      /**  Indicates if the submit button is enabled  */  
   EnableSubmit:boolean,
      /**  Indicates if the recall button is enabled  */  
   EnableRecall:boolean,
      /**  Indicates if the copy button is enabled  */  
   EnableCopy:boolean,
      /**  Indicates if the user retrieving the record has access to view the row or not.  */  
   HasAccessToRow:boolean,
      /**  Indicates if recall is available in approval entry  */  
   EnableRecallAprv:boolean,
      /**  Used in approval entry.  Indicates if the approver has an open approval task.  */  
   ApprvrHasOpenTask:boolean,
      /**  Indicates if this is the base currency.  Only one base currency is allowed  */  
   ChargeCurrencyBaseCurr:boolean,
      /**  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  */  
   ChargeCurrencyCurrencyID:string,
      /**   An extended description that can be used on documents such as
POs and invoices.  */  
   ChargeCurrencyDocumentDesc:string,
      /**   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  */  
   ChargeCurrencyCurrName:string,
      /**  Description of the currency  */  
   ChargeCurrencyCurrDesc:string,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   ChargeCurrencyCurrSymbol:string,
      /**  Description  */  
   ChargeRateTypeDescription:string,
      /**   An extended description that can be used on documents such as
POs and invoices.  */  
   ClaimCurrencyDocumentDesc:string,
      /**   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  */  
   ClaimCurrencyCurrName:string,
      /**  Description of the currency  */  
   ClaimCurrencyCurrDesc:string,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   ClaimCurrencyCurrSymbol:string,
      /**  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  */  
   ClaimCurrencyCurrencyID:string,
      /**  Indicates if this is the base currency.  Only one base currency is allowed  */  
   ClaimCurrencyBaseCurr:boolean,
      /**  Description  */  
   CurrRateGrpDescription:string,
      /**  This is the employee's full name. This is not directly maintainable. It is a concatenation of the FirstName + MiddleInitial + LastName fields. It exists so that it can be used in browses or where ever the complete name in a first, middle, last fashion is required.  */  
   EmpBasicName:string,
      /**  Last name of employee  */  
   EmpBasicLastName:string,
      /**  First name of employee.  */  
   EmpBasicFirstName:string,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   ExpCurrencyCurrSymbol:string,
      /**  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  */  
   ExpCurrencyCurrencyID:string,
      /**   An extended description that can be used on documents such as
POs and invoices.  */  
   ExpCurrencyDocumentDesc:string,
      /**   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  */  
   ExpCurrencyCurrName:string,
      /**  Description of the currency  */  
   ExpCurrencyCurrDesc:string,
      /**  Indicates if this is the base currency.  Only one base currency is allowed  */  
   ExpCurrencyBaseCurr:boolean,
      /**  Reimbursable  */  
   PayMethodReimbursable:boolean,
      /**  Indicated the type of payment with the following options:
 0 = Manual (default)
 1 = Electronic Interface
 2 = Check Printing
 3 = Payment Instrument Type 1
 4 = Payment Instrument Type 2  */  
   PayMethodType:number,
      /**  Name of the payment method  */  
   PayMethodName:string,
      /**   Indicates that invoices for the customer is summarized and sent as a sum to the bank without specifying the individual invoices.
A single bank transaction is created for the payment but what?s actually sent to the bank will be determined by the electronic interface plug-in program.
Only enabled if type is set to ?Electronic Interface?  */  
   PayMethodSummarizePerCustomer:boolean,
      /**  Full description of Project Management Code.  */  
   ProjectDescription:string,
      /**  Description  */  
   ProjPhaseDescription:string,
      /**  When an expense charge, indicates if the code is chargeable.  */  
   PurMiscExpChargeable:boolean,
      /**  Description of the Miscellaneous Charge. Used as a default to Orders and Invoices.  */  
   PurMiscDescription:string,
      /**  When an expense charge, indicates if the code is unit based.  */  
   PurMiscExpUnitBased:boolean,
      /**  Description of the task set.  */  
   TaskSetTaskSetDescription:string,
      /**  The type of workflow of this task set.  Possible values are "CRM" - CRM related tasks and "ECO" - ECO tasks  */  
   TaskSetWorkflowType:string,
      /**  Full description for the Tax Region.  */  
   TaxRgnDescription:string,
      /**  Country Name. Printed as last line of mailing address. Can be blank.  */  
   VendorCountry:string,
      /**  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  */  
   VendorTermsCode:string,
      /**  Third address line of the Supplier  */  
   VendorAddress3:string,
      /**  First address line of the Supplier  */  
   VendorAddress1:string,
      /**  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  */  
   VendorName:string,
      /**  A unique code that identifies the currency.  */  
   VendorCurrencyCode:string,
      /**  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  */  
   VendorVendorID:string,
      /**  City portion of the address of the Supplier  */  
   VendorCity:string,
      /**  Can be blank.  */  
   VendorState:string,
      /**  Second address line of the Supplier  */  
   VendorAddress2:string,
      /**  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  */  
   VendorDefaultFOB:string,
      /**  Postal Code or Zip code portion of the address of the Supplier  */  
   VendorZIP:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_EmpExpenseListTableset{
   EmpExpenseList:Erp_Tablesets_EmpExpenseListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_EmpExpenseRow{
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
      /**  The FromEffectiveDate from ExpenseTypeUnitBased that was used to determine default values for Units and UnitRate.  This combined with ExpenseTypeCode point to a unique ExpenseTypeUnitBased record.  */  
   UBFromEffectiveDate:string,
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
      /**  The charge currency.  This is derived from the currency on the related project.  */  
   ChargeCurrencyCode:string,
      /**  The charge exchange rate.  This is derived from the exchange rate on the related project.  */  
   ChargeExchangeRate:number,
      /**  The charge rate group code.  This is derived from the rate group code on the related projec.t  */  
   ChargeRateGrpCode:string,
      /**  The charge amount of the expense in the charge currency.  */  
   DocChargeAmt:number,
      /**  The date the expense received final approval.  */  
   ApprovedDate:string,
      /**  The supplier number used on the employee of the expense.  */  
   VendorNum:number,
      /**  The ap invoice number the expense was invoiced on.  */  
   InvoiceNum:string,
      /**  The invoice line created for this expense.  */  
   InvoiceLine:number,
      /**  Link to Task set  */  
   TaskSetID:string,
      /**  Indicates if this expense is a reversal (full or partial) of an existing expense.  */  
   IsReversal:boolean,
      /**  Reversed Expense Number  */  
   ReversedExpenseNum:number,
      /**  Userid of the user who created the record.  */  
   CreatedBy:string,
      /**  The date the record was created.  */  
   CreateDate:string,
      /**  The time the record was created (in seconds since midnight)  */  
   CreateTime:number,
      /**  Userid of the user who made the last change to this record.  */  
   ChangedBy:string,
      /**  The date the record was last changed.  */  
   ChangeDate:string,
      /**  The time the record was last changed (in seconds since midnight)  */  
   ChangeTime:number,
      /**  The Currently active Stage changing task  */  
   ActiveTaskID:string,
      /**  The Last Complete Milestone task  */  
   LastTaskID:string,
      /**  The currency the claim amounts are in.  */  
   ClaimCurrencyCode:string,
      /**  The exchange rate between the claim currency and the base currency based on expense date.  */  
   ClaimExchangeRate:number,
      /**  Used with the currency module.  When TRUE the claim currency rate can be changed by the user and cannot be changed by the system.  */  
   ClaimLockRate:boolean,
      /**  The claim rate group code.  */  
   ClaimRateGrpCode:string,
      /**  The tax of the claim in the claim currency.  */  
   DocClaimTaxAmt:number,
      /**  The amount of the claim in the claim currency.  */  
   DocClaimAmt:number,
      /**  The total amount of the claim in the claim currency.  This value includes taxes.  */  
   DocTotalClaimAmt:number,
      /**  The miscellaneous charge code for this expense.  */  
   MiscCode:string,
      /**  The user who submitted the expense  */  
   SubmittedBy:string,
      /**  The identifier of the workflow stage.  */  
   CurrentWFStageID:string,
      /**  The identifier of the workflow group  */  
   WFGroupID:string,
      /**  This indicates if the workflow for this group is complete.  */  
   WFComplete:boolean,
      /**  Indicates if approval is required for this transaction.  */  
   ApprovalRequired:boolean,
      /**  Indicates if the record is tax exempt.  If field is non-blank it is considered exempt.  */  
   TaxExempt:string,
      /**  If set to true, the tax calculation logic will retrieve the default SalesTax ids for the expense before calculating taxes. It will also be reset to true if the TaxConnectCalc flag switches from true to false.  */  
   GetDfltTaxIds:boolean,
      /**  If true, the EmpExpenseTax records tied to this release are calculated using Tax Connect logic. If  false, taxes are calculated using the standard calc methods.  */  
   TaxConnectCalc:boolean,
      /**  Expense Withholding Tax Amount.  */  
   DocExpWithholdAmt:number,
      /**  Claim Withholding Tax Amount.  */  
   DocClaimWithholdAmt:number,
      /**  Indicates if the expense is reimbursable.  */  
   Reimbursable:boolean,
      /**  The tax of the claim in the charge currency.  */  
   DocChargeTaxAmt:number,
      /**  The total charge amount in the charge currency.  This value includes taxes.  */  
   DocTotalChargeAmt:number,
      /**  The exchange rate between the claim currency and the base currency.  */  
   ClaimToBaseExchangeRate:number,
      /**  Job Number of the misc charge jobmtl record  */  
   JobNum:string,
      /**  Assembly sequence number of the misc charge jobmtl record  */  
   AssemblySeq:number,
      /**  Material sequence of the misc charge jobmtl record  */  
   MtlSeq:number,
      /**  Indicates if the expense has been invoiced.  */  
   Invoiced:boolean,
      /**  Expense Comment  */  
   ExpCommentText:string,
      /**  Expense Comment Instruction  */  
   ExpCommentInstr:string,
      /**  Indicates that this record has been process by the project analysis build process  */  
   ProjProcessed:boolean,
      /**  Used by Project Analysis process.  */  
   AsOfDate:string,
      /**  Used By Project Analysis Process  */  
   AsOfSeq:number,
      /**  The expense category.  */  
   ExpenseCategory:string,
      /**  The voucher or receipt number reference.  */  
   VoucherReceiptNo:string,
      /**  The date for the voucher/receipt reference  */  
   VoucherReceiptDate:string,
      /**  The remaining balance of the advance.  For advance request expense category, is initially set to the claim amount; will be zero for other categories.  Is reduced when other expenses that match the advance amount are invoiced.  */  
   DocAdvanceBalance:number,
      /**  The amount that has been matched from advance requests to this expense.  */  
   DocMatchedClaimAmt:number,
      /**  The Sales order that this expense is linked to.  */  
   OrderNum:number,
      /**  The line number of the sales order that this expense is linked to  */  
   OrderLine:number,
      /**  The release number of the sales order that this expense is linked to  */  
   OrderRelNum:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  PartTranSysRowID  */  
   PartTranSysRowID:string,
      /**  ExpenseAutoSubmit  */  
   ExpenseAutoSubmit:boolean,
      /**  Related to Epicor FSA  */  
   EpicorFSA:boolean,
      /**  MobileExpense  */  
   MobileExpense:boolean,
   APInvLineAmt:number,
   APInvLineTaxAmt:number,
      /**  Used by Time and Expense approval only, not done as a linked field so it won't impact performance in processes other than Approval.  */  
   ApprovalPhaseDesc:string,
      /**  Used by Time and Expense approval only, populated with the JobHead.PhaseID, not done as a linked field so it won't impact performance in processes other than Approval.  */  
   ApprovalPhaseID:string,
      /**  Used by Time and Expense approval only, populated with the Project.Description for ApprovalProjectID, not done as a linked field so it won't impact performance in processes other than Approval.  */  
   ApprovalProjectDesc:string,
      /**  Used by Time and Expense approval only, populated with the JobHead.ProjectID, not done as a linked field so it won't impact performance in processes other than Approval.  */  
   ApprovalProjectID:string,
      /**  A list of people who have approved the expense  */  
   ApprovedBy:string,
      /**  Used in approval entry.  Indicates if the approver has an open approval task.  */  
   ApprvrHasOpenTask:boolean,
      /**  The claim amount displayed to the user.  If the expense is non-reimbursable, the user will see zero for the claim amount.  */  
   DispClaimAmt:number,
      /**  The claim tax amount displayed to the user.  If the expense is non-reimbursable, the user will see zero for the claim tax amount.  */  
   DispClaimTaxAmt:number,
      /**  External field to display a descriptive status of the record  */  
   DisplayStatus:string,
      /**  The claim amount total displayed to the user.  If the expense is non-reimbursable, the user will see zero for the claim amount.  */  
   DispTotalClaimAmt:number,
   DspChangeTime:string,
   DspCreateTime:string,
   EnableClaimCurrencyCode:boolean,
   EnableClaimLockRate:boolean,
      /**  Indicates if the copy button is enabled  */  
   EnableCopy:boolean,
      /**  Indicates if the recall button is enabled  */  
   EnableRecall:boolean,
      /**  Indicates if recall is available in approval entry  */  
   EnableRecallAprv:boolean,
      /**  Indicates if the submit button is enabled  */  
   EnableSubmit:boolean,
      /**  Indicates if UnitRate is enabled  */  
   EnableUnitRate:boolean,
      /**  Text to show the day of the week that corresponds to the EmpExpense.ExpenseDate (Sunday, Monday, etc)  */  
   ExpDay:string,
   ExpenseCurrencyList:string,
   ExpenseDisableDelete:boolean,
   ExpenseDisableUpdate:boolean,
      /**  Text to show the month  (January, February, etc) that corresponds to the EmpExpense.ExpenseDate  */  
   ExpMonth:string,
      /**  Text to show the week date range (Sunday-Saturday) that corresponds to the EmpExpense.ExpenseDate such as "5/2/2009 - 5/9/2009"  */  
   ExpWeek:string,
      /**  Service Order number generated on FSA, stored on FSAExtData db table.  */  
   FSAServiceOrderNum:number,
      /**  Service Order Resource generated on FSA, stored on FSAExtData db table.  */  
   FSAServiceOrderResourceNum:number,
      /**  Indicates if the user retrieving the record has access to view the row or not.  */  
   HasAccessToRow:boolean,
      /**  Indicates if the expense detail has attachments  */  
   HasAttachments:boolean,
      /**  Indicates if the expense detail has comments  */  
   HasComments:boolean,
      /**  If invoiced, the status of the invoice.  */  
   InvoiceStatus:string,
      /**  Indicates if this record is selected to be submitted  */  
   IsSelected:boolean,
      /**  Indicates if multi-currency is licensed  */  
   MultiCurrency:boolean,
   NewDifDateFlag:boolean,
      /**  Indicates if the record has been submitted or not  */  
   NotSubmitted:boolean,
      /**  A list of people who need to approve the expense  */  
   PendingApprovalBy:string,
   TreeNodeImageName:string,
      /**  The label value for Units field.  */  
   UnitsLabel:string,
      /**  Exchange Rate Label  */  
   XRateLabel:string,
   APInvLineTotAmt:number,
      /**  Indicates of the row is selected for submit or recall  */  
   RowSelected:boolean,
      /**  Start date/time for calendar appoinment  */  
   AppointmentStart:string,
      /**  End date/time for calendar appoinment  */  
   AppointmentEnd:string,
      /**  Title to display for the calendar appointment  */  
   AppointmentTitle:string,
      /**  Is calendar appointment all day  */  
   AppointmentIsAllDay:boolean,
   BitFlag:number,
   ChargeCurrencyCurrSymbol:string,
   ChargeCurrencyCurrDesc:string,
   ChargeCurrencyCurrName:string,
   ChargeCurrencyCurrencyID:string,
   ChargeCurrencyDocumentDesc:string,
   ChargeCurrencyBaseCurr:boolean,
   ChargeRateGrpDescription:string,
   ClaimCurrencyCurrName:string,
   ClaimCurrencyBaseCurr:boolean,
   ClaimCurrencyDocumentDesc:string,
   ClaimCurrencyCurrSymbol:string,
   ClaimCurrencyCurrDesc:string,
   ClaimCurrencyCurrencyID:string,
   CurrRateGrpDescription:string,
   EmpBasicName:string,
   EmpBasicFirstName:string,
   EmpBasicLastName:string,
   ExpCurrencyDocumentDesc:string,
   ExpCurrencyCurrSymbol:string,
   ExpCurrencyBaseCurr:boolean,
   ExpCurrencyCurrName:string,
   ExpCurrencyCurrDesc:string,
   ExpCurrencyCurrencyID:string,
   PayMethodType:number,
   PayMethodReimbursable:boolean,
   PayMethodSummarizePerCustomer:boolean,
   PayMethodName:string,
   ProjectDescription:string,
   ProjPhaseDescription:string,
   PurMiscExpUnitBased:boolean,
   PurMiscExpChargeable:boolean,
   PurMiscDescription:string,
   TaskSetWorkflowType:string,
   TaskSetTaskSetDescription:string,
   TaxRgnDescription:string,
   VendorAddress1:string,
   VendorCurrencyCode:string,
   VendorVendorID:string,
   VendorAddress2:string,
   VendorTermsCode:string,
   VendorAddress3:string,
   VendorState:string,
   VendorCountry:string,
   VendorZIP:string,
   VendorCity:string,
   VendorDefaultFOB:string,
   VendorName:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_EmpExpenseTableset{
   EmpExpense:Erp_Tablesets_EmpExpenseRow[],
   EmpExpenseAttch:Erp_Tablesets_EmpExpenseAttchRow[],
   EmpExpenseComment:Erp_Tablesets_EmpExpenseCommentRow[],
   EmpExpenseTax:Erp_Tablesets_EmpExpenseTaxRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_EmpExpenseTaxRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The employee the expense record is for.  */  
   EmpID:string,
      /**  Internal identifier of the EmpExpense record.  This with EmpID makes the record unique.  */  
   EmpExpenseNum:number,
      /**  Descriptive code assigned by user which uniquely identifies a Sales Tax master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  */  
   TaxCode:string,
      /**  Rate code  */  
   RateCode:string,
      /**   Used to allow a second tax record using the same tax code on an expense.  When the sales tax field EcAquisition is checked then 2 expense tax records are created.
NOTE:  This field is now used in VAT Reverse Charge logic.  If an invoice line is marked for Reverse Charge, a second line is created just like in the ECAcquisition logic. To distinguish the two scenarios, the ReverseCharge flag will be set to true if the second line is for Reverse Charge.  */  
   ECAcquisitionSeq:number,
      /**  The reportable amount to the tax jurisdiction in the expense currency.  */  
   ExpReportableAmt:number,
      /**  The reportable amount to the tax jurisdiction in the claim currency.  */  
   ClaimReportableAmt:number,
      /**  Taxable Amount for this expense in the expense currency  */  
   ExpTaxableAmt:number,
      /**  Taxable Amount for this expense in the claim currency.  */  
   ClaimTaxableAmt:number,
      /**  The tax percentage rate that is used for this expense. This is defaulted from the SalesTax.Percent.  */  
   Percent:number,
      /**  Sales Tax amount for the corresponding taxable sales amount in the expense currency.  */  
   ExpTaxAmt:number,
      /**  Sales Tax amount for the corresponding taxable sales amount in the claim currency  */  
   ClaimTaxAmt:number,
      /**  Indicates if the tax calculations are to be performed manually.  When this field is set the Reportable, Taxable, and TaxAmount fields are enabled.  When it is NOT set these fields are DISABLED and the system will perform all of the Reportable, Taxable, and TaxAmount calculations.  Defaults from the SalesTax.Manual field.  */  
   Manual:boolean,
      /**  Userid of the user who created the record.  */  
   CreatedBy:string,
      /**  The date the record was created.  */  
   CreateDate:string,
      /**  The time the record was created (in seconds since midnight)  */  
   CreateTime:number,
      /**  Userid of user who made the last change to this record.  */  
   ChangedBy:string,
      /**  The date that the record was last changed  */  
   ChangeDate:string,
      /**  The time that the record was last change (seconds since midnight)  */  
   ChangeTime:number,
      /**  Reverse Charge.  */  
   ReverseCharge:boolean,
      /**  Collection Type  */  
   CollectionType:number,
      /**  Timing of when to report taxes  */  
   Timing:number,
      /**  Exemption Type  */  
   ExemptType:number,
      /**  Exemption Percent  */  
   ExemptPercent:number,
      /**  Resolution number  */  
   ResolutionNum:string,
      /**  Resolution Date  */  
   ResolutionDate:string,
      /**  Tax Rate Date  */  
   TaxRateDate:string,
      /**  Balance of the Taxable amount that has been deferred until payment.  In expense currency  */  
   ExpDefTaxableAmt:number,
      /**  Balance of the Taxable amount that has been deferred until payment.  In claim currency.  */  
   ClaimDefTaxableAmt:number,
      /**  Balance of the Tax amount that has been deferred until payment.  In expense currency.  */  
   ExpDefTaxAmt:number,
      /**  Balance of the Tax amount that has been deferred until payment.  In claim currency  */  
   ClaimDefTaxAmt:number,
      /**  This record was manually added (not in Liability) but will use the standard calculations  */  
   ManAdd:boolean,
      /**  Deducatable Tax Amount in expense currency  */  
   ExpDedTaxAmt:number,
      /**  Deducatable Tax Amount in claim currency  */  
   ClaimDedTaxAmt:number,
      /**  Fixed Tax Amount in expense currency  */  
   ExpFixedAmount:number,
      /**  Document Fixed Tax Amount in claim currency  */  
   ClaimFixedAmount:number,
      /**  Unique Identifier for Legal Text  */  
   TextCode:string,
      /**  Difference between tax calculated in document rate less tax calculated in tax rate in expense currency  */  
   ExpTaxAmtVar:number,
      /**  Difference between tax calculated in document rate less tax calculated in tax rate in claim currency  */  
   ClaimTaxAmtVar:number,
      /**  System calculated Taxable amount for this expense in the claim currency  */  
   SysCalcClaimTaxableAmt:number,
      /**  System calculated Taxable amount for this expense in the expense currency.  */  
   SysCalcExpTaxableAmt:number,
      /**  System calculated reportable amount to the tax jurisdiction in the expense currency  */  
   SysCalcExpReportableAmt:number,
      /**  System calculated reportable sales amount to the tax jurisdiction expressed in the claim currency.  */  
   SysCalcClaimReportableAmt:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   ExpCurrencyCode:string,
   ExpCurrencyDesc:string,
   ClaimCurrencyCode:string,
   ClaimCurrencyDesc:string,
      /**  Unique identifier of related integration record.  */  
   IntExternalKey:string,
   BitFlag:number,
   RateCodeDescription:string,
   TaxCodeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_TaskListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The master file to which the task is related.  Opportunity/Quote, Customer, ECO Group etc...  */  
   RelatedToFile:string,
      /**  Major component of the foreign key of the related master record. For example: For a task related to a quote (Customer) this field would contain the related Customer.CustNum value.  */  
   Key1:string,
      /**  2nd component of the foreign key to the related master record.  */  
   Key2:string,
      /**  3rd component of the foreign key to the related master record.  */  
   Key3:string,
      /**  Link to the TaskMast table. Contains the TaskMast.TaskID value related to this task.  */  
   TaskID:string,
      /**  Used to uniquely identify the record.  Used so more than 1 Task can exist for a given record.  The next sequence is found by finding the last PCE with the same key fields then adding 1 to its seqnum.  */  
   TaskSeqNum:number,
      /**  Default description from the TaskMaster. TaskMast.TaskDescription. The user can override the default description for this specific task.  */  
   TaskDescription:string,
      /**  The SalesRep that this task is assigned to. Will default from Role on TaskMaster  */  
   SalesRepCode:string,
      /**  Defaults is TODAY.  */  
   StartDate:string,
      /**  The Task should be completed by this date.  */  
   DueDate:string,
      /**  Status Code. From TaskStat table  */  
   StatusCode:string,
      /**  Percent of task that is complete.  Valid values are 0-100. User maintained.  */  
   PercentComplete:number,
      /**  Indicates that this task is complete.  When checked this will trigger creation of the next task and the global alert process.  */  
   Complete:boolean,
      /**  User entered completion date.  Default to TODAY when the complete flag is checked.  */  
   CompleteDate:string,
      /**   The LOQ must be in this stage to be selected or it will be put in this stage if the LOQ is already past this stage.
Valid Choices are
Lead, Oppo = Opportunity, Quot = Quote.
Not maintainable  */  
   CurrentStage:string,
      /**  This task must be completed before the LOQ can move to the next milestone.  Not maintainable as actual task  */  
   Mandatory:boolean,
      /**  This task must be completed before the LOQ can move to the next Milestone.  Only one Milestone task can be active on a quote at one time.  Not maintainable as actual task.  */  
   Milestone:boolean,
      /**  The date the task was created.  */  
   CreateDate:string,
      /**  The UserID that created the task  */  
   CreateDcdUserID:string,
      /**  The date the task was last changed.  */  
   ChangeDate:string,
      /**  The UserID that last changed the task  */  
   ChangeDcdUserID:string,
      /**  Completion of the task will send a Global Alert  */  
   SendAlertComplete:boolean,
      /**  Valid values are 1 - 99 1 = HIGH,  99 = LOW  */  
   PriorityCode:number,
      /**  Contains comments about the Task.  */  
   TaskComment:string,
      /**  Valid values are "win" "lose" "next" "next" is the default .  This will display as a radio set.  If "win" is selected then completing this task will require a reason code from CRM Win type. A sales order will be created if all mandatory tasks at this milestone are complete.  If  "lose" is selected all tasks and the quote will close  and a CRM Lose reason code is required. If "next" is selected then the "next task" drop down is enabled and the list of possible next tasks from the task set(TaskSNxt) will be displayed, reason code will be optional  */  
   Conclusion:string,
      /**  Select from list of Win or loss reason codes depending on the setting if the conclusion field  */  
   ReasonCode:string,
      /**  When this task is completed and the conclusion is "next" this field will hold the next Milestone task to be created.  */  
   NextTaskID:string,
      /**  Indentifies the nest milestone task sequence.  */  
   NextTaskSeq:number,
      /**  The Quote that this Task is related to.  */  
   TaskQuoteNum:number,
      /**  The Customer that this task is related to  */  
   TaskCustNum:number,
      /**  The Customer Ship To that this task is related to  */  
   TaskShipToNum:string,
      /**  The Customer contact that this Task is related to.  */  
   TaskConNum:number,
      /**  Link to the task set.  */  
   TaskSetID:string,
      /**  Link to the Task Set Detail  */  
   TaskSetSeq:number,
      /**  Setting this when the opportunity is a "win" will trigger the logic that creates a sales order.  */  
   CreateOrder:boolean,
      /**  Creation of the task will send a Global Alert  */  
   SendAlertCreate:boolean,
      /**  Defines the type of task this is.  From the TaskType table.  */  
   TypeCode:string,
      /**  The Vendor number associated with this task.  */  
   TaskVendorNum:number,
      /**  The Vendor purchase point related to this task.  */  
   TaskPurPoint:string,
      /**  The purchasing contact person associated with this task.  */  
   TaskPrcConNum:number,
      /**  Link to the Marketing Campaign related to this Task.  */  
   TaskMktgCampaignID:string,
      /**  A salesperson that the assigned salesperson needs to contact to complete this task  */  
   OtherSalesRepCode:string,
      /**  Defines if this task is included in the Customer category.  Categories are used for selecting tasks for assignment to TaskSets.  */  
   CustomerCategory:boolean,
      /**  Defines if this task is included in the Engineering category.  */  
   EngineeringCategory:boolean,
      /**  Defines if this task is included in the Vendor category.  */  
   VendorCategory:boolean,
      /**  Defines if this task is included in the Personal category.  */  
   PersonalCategory:boolean,
      /**  Defines if this task is included in the Management category.  */  
   ManagementCategory:boolean,
      /**  Defines if this task is included in the Other category.  */  
   OtherCategory:boolean,
      /**  Role of person who would default as the owner of this task when the task is created. From the RoleCD table.  */  
   RoleCode:string,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  EmployeeName  */  
   EmployeeName:string,
      /**   Text to indicate if this task is for "Time" or "Expense" (translated text). Used only by Labor Approval
TaskList search for search results column.  */  
   TimeOrExp:string,
      /**  ProjectID, used only by Task Time and Expense search as a search results grid.  */  
   ProjectID:string,
      /**  Holds the date of the transaction that created the task, used by TimeExpense approval search form.  */  
   TransDate:string,
      /**  JobNum, used only by task time and expense approbal search as search results grid  */  
   JobNum:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_TaskListTableset{
   TaskList:Erp_Tablesets_TaskListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtEmpExpenseTableset{
   EmpExpense:Erp_Tablesets_EmpExpenseRow[],
   EmpExpenseAttch:Erp_Tablesets_EmpExpenseAttchRow[],
   EmpExpenseComment:Erp_Tablesets_EmpExpenseCommentRow[],
   EmpExpenseTax:Erp_Tablesets_EmpExpenseTaxRow[],
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
   returnObj:Erp_Tablesets_EmpExpenseTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_EmpExpenseTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_EmpExpenseTableset[],
}

   /** Required : 
      @param ipEmpID
      @param ipClaimRef
      @param ipExpenseStatus
      @param ipInvoiceNum
      @param ipInvoiceStatus
      @param pageSize
      @param absolutePage
   */  
export interface GetListExpenses_input{
      /**  Employee id  */  
   ipEmpID:string,
      /**  Claim Reference  */  
   ipClaimRef:string,
      /**  Expense Status  */  
   ipExpenseStatus:string,
      /**  Invoice Number  */  
   ipInvoiceNum:string,
      /**  Invoice Status  */  
   ipInvoiceStatus:string,
      /**  The page size  */  
   pageSize:number,
      /**  the absolute page  */  
   absolutePage:number,
}

export interface GetListExpenses_output{
   returnObj:Erp_Tablesets_EmpExpenseListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
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
   returnObj:Erp_Tablesets_EmpExpenseListTableset[],
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
export interface GetNewEmpExpenseAttch_input{
   ds:Erp_Tablesets_EmpExpenseTableset[],
   empID:string,
   empExpenseNum:number,
}

export interface GetNewEmpExpenseAttch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EmpExpenseTableset[],
}
}

   /** Required : 
      @param ds
      @param empID
      @param empExpenseNum
   */  
export interface GetNewEmpExpenseComment_input{
   ds:Erp_Tablesets_EmpExpenseTableset[],
   empID:string,
   empExpenseNum:number,
}

export interface GetNewEmpExpenseComment_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EmpExpenseTableset[],
}
}

   /** Required : 
      @param empID
      @param expenseDate
      @param ds
   */  
export interface GetNewEmpExpenseForDate_input{
      /**  Employee ID  */  
   empID:string,
      /**  Expense Date  */  
   expenseDate:string,
   ds:Erp_Tablesets_EmpExpenseTableset[],
}

export interface GetNewEmpExpenseForDate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EmpExpenseTableset[],
}
}

   /** Required : 
      @param ds
      @param empID
      @param empExpenseNum
      @param taxCode
      @param rateCode
   */  
export interface GetNewEmpExpenseTax_input{
   ds:Erp_Tablesets_EmpExpenseTableset[],
   empID:string,
   empExpenseNum:number,
   taxCode:string,
   rateCode:string,
}

export interface GetNewEmpExpenseTax_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EmpExpenseTableset[],
}
}

   /** Required : 
      @param ds
      @param empID
   */  
export interface GetNewEmpExpense_input{
   ds:Erp_Tablesets_EmpExpenseTableset[],
   empID:string,
}

export interface GetNewEmpExpense_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EmpExpenseTableset[],
}
}

   /** Required : 
      @param rateCode
      @param ds
   */  
export interface GetRateCodeInfo_input{
      /**  Proposed RateCode value  */  
   rateCode:string,
   ds:Erp_Tablesets_EmpExpenseTableset[],
}

export interface GetRateCodeInfo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EmpExpenseTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface GetRowsTran_input{
   ds:Erp_Tablesets_TaskListTableset[],
}

export interface GetRowsTran_output{
   returnObj:Erp_Tablesets_EmpExpenseTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TaskListTableset[],
}
}

   /** Required : 
      @param whereClauseEmpExpense
      @param whereClauseEmpExpenseAttch
      @param whereClauseEmpExpenseComment
      @param whereClauseEmpExpenseTax
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseEmpExpense:string,
   whereClauseEmpExpenseAttch:string,
   whereClauseEmpExpenseComment:string,
   whereClauseEmpExpenseTax:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_EmpExpenseTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
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
      @param includeComments
      @param includeAttachments
      @param ds
   */  
export interface MobileGetRowsTran_input{
   includeComments:boolean,
   includeAttachments:boolean,
   ds:Erp_Tablesets_TaskListTableset[],
}

export interface MobileGetRowsTran_output{
   returnObj:Erp_Tablesets_EmpExpenseTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TaskListTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface RecallEmpExpense_input{
   ds:Erp_Tablesets_EmpExpenseTableset[],
}

export interface RecallEmpExpense_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EmpExpenseTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface RecallFromApprovalBySelected_input{
   ds:Erp_Tablesets_EmpExpenseTableset[],
}

export interface RecallFromApprovalBySelected_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EmpExpenseTableset[],
}
}

   /** Required : 
      @param ipSalesRepCode
      @param ds
   */  
export interface RecallFromApproval_input{
      /**  The sales Rep Code of the approver.  */  
   ipSalesRepCode:string,
   ds:Erp_Tablesets_EmpExpenseTableset[],
}

export interface RecallFromApproval_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EmpExpenseTableset[],
   outMessage:string,
}
}

   /** Required : 
      @param ds
   */  
export interface SubmitForApprovalBySelected_input{
   ds:Erp_Tablesets_EmpExpenseTableset[],
}

export interface SubmitForApprovalBySelected_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EmpExpenseTableset[],
   messageText:string,
}
}

   /** Required : 
      @param ds
   */  
export interface SubmitSelected_input{
   ds:Erp_Tablesets_EmpExpenseTableset[],
}

export interface SubmitSelected_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EmpExpenseTableset[],
   outMessage:string,
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtEmpExpenseTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtEmpExpenseTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_EmpExpenseTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EmpExpenseTableset[],
}
}

