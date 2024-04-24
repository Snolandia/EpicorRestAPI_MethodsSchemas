import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.PayrollCheckEntrySvc
// Description: 
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/$metadata", {
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
   Description: Get PayrollCheckEntries items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PayrollCheckEntries
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PRCheckRow
   */  
export function get_PayrollCheckEntries(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PRCheckRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/PayrollCheckEntries", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PRCheckRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PayrollCheckEntries
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PRCheckRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PRCheckRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PayrollCheckEntries(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/PayrollCheckEntries", {
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
   Summary: Calls GetByID to retrieve the PayrollCheckEntry item
   Description: Calls GetByID to retrieve the PayrollCheckEntry item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PayrollCheckEntry
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PRCheckRow
   */  
export function get_PayrollCheckEntries_Company_HeadNum(Company:string, HeadNum:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PRCheckRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/PayrollCheckEntries(" + Company + "," + HeadNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PRCheckRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PayrollCheckEntry for the service
   Description: Calls UpdateExt to update PayrollCheckEntry. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PayrollCheckEntry
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PRCheckRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PayrollCheckEntries_Company_HeadNum(Company:string, HeadNum:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/PayrollCheckEntries(" + Company + "," + HeadNum + ")", {
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
   Summary: Call UpdateExt to delete PayrollCheckEntry item
   Description: Call UpdateExt to delete PayrollCheckEntry item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PayrollCheckEntry
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PayrollCheckEntries_Company_HeadNum(Company:string, HeadNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/PayrollCheckEntries(" + Company + "," + HeadNum + ")", {
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
   Description: Get PRCheckTGLCs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PRCheckTGLCs1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PRCheckTGLCRow
   */  
export function get_PayrollCheckEntries_Company_HeadNum_PRCheckTGLCs(Company:string, HeadNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PRCheckTGLCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/PayrollCheckEntries(" + Company + "," + HeadNum + ")/PRCheckTGLCs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PRCheckTGLCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PRCheckTGLC item
   Description: Calls GetByID to retrieve the PRCheckTGLC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PRCheckTGLC1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param TGLCTranNum Desc: TGLCTranNum   Required: True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PRCheckTGLCRow
   */  
export function get_PayrollCheckEntries_Company_HeadNum_PRCheckTGLCs_Company_HeadNum_TGLCTranNum_Key2(Company:string, HeadNum:string, TGLCTranNum:string, Key2:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PRCheckTGLCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/PayrollCheckEntries(" + Company + "," + HeadNum + ")/PRCheckTGLCs(" + Company + "," + HeadNum + "," + TGLCTranNum + "," + Key2 + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PRCheckTGLCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get PRChkDeds items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PRChkDeds1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PRChkDedRow
   */  
export function get_PayrollCheckEntries_Company_HeadNum_PRChkDeds(Company:string, HeadNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PRChkDedRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/PayrollCheckEntries(" + Company + "," + HeadNum + ")/PRChkDeds", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PRChkDedRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PRChkDed item
   Description: Calls GetByID to retrieve the PRChkDed item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PRChkDed1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param DeductionID Desc: DeductionID   Required: True   Allow empty value : True
      @param DeductionNum Desc: DeductionNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PRChkDedRow
   */  
export function get_PayrollCheckEntries_Company_HeadNum_PRChkDeds_Company_HeadNum_DeductionID_DeductionNum(Company:string, HeadNum:string, DeductionID:string, DeductionNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PRChkDedRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/PayrollCheckEntries(" + Company + "," + HeadNum + ")/PRChkDeds(" + Company + "," + HeadNum + "," + DeductionID + "," + DeductionNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PRChkDedRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get PRChkDtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PRChkDtls1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PRChkDtlRow
   */  
export function get_PayrollCheckEntries_Company_HeadNum_PRChkDtls(Company:string, HeadNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PRChkDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/PayrollCheckEntries(" + Company + "," + HeadNum + ")/PRChkDtls", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PRChkDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PRChkDtl item
   Description: Calls GetByID to retrieve the PRChkDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PRChkDtl1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param LineNum Desc: LineNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PRChkDtlRow
   */  
export function get_PayrollCheckEntries_Company_HeadNum_PRChkDtls_Company_HeadNum_LineNum(Company:string, HeadNum:string, LineNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PRChkDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/PayrollCheckEntries(" + Company + "," + HeadNum + ")/PRChkDtls(" + Company + "," + HeadNum + "," + LineNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PRChkDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get PRChkTaxes items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PRChkTaxes1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PRChkTaxRow
   */  
export function get_PayrollCheckEntries_Company_HeadNum_PRChkTaxes(Company:string, HeadNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PRChkTaxRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/PayrollCheckEntries(" + Company + "," + HeadNum + ")/PRChkTaxes", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PRChkTaxRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PRChkTax item
   Description: Calls GetByID to retrieve the PRChkTax item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PRChkTax1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param TaxTblID Desc: TaxTblID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PRChkTaxRow
   */  
export function get_PayrollCheckEntries_Company_HeadNum_PRChkTaxes_Company_HeadNum_TaxTblID(Company:string, HeadNum:string, TaxTblID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PRChkTaxRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/PayrollCheckEntries(" + Company + "," + HeadNum + ")/PRChkTaxes(" + Company + "," + HeadNum + "," + TaxTblID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PRChkTaxRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get PRCheckTGLCs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PRCheckTGLCs
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PRCheckTGLCRow
   */  
export function get_PRCheckTGLCs(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PRCheckTGLCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/PRCheckTGLCs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PRCheckTGLCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PRCheckTGLCs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PRCheckTGLCRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PRCheckTGLCRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PRCheckTGLCs(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/PRCheckTGLCs", {
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
   Summary: Calls GetByID to retrieve the PRCheckTGLC item
   Description: Calls GetByID to retrieve the PRCheckTGLC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PRCheckTGLC
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param TGLCTranNum Desc: TGLCTranNum   Required: True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PRCheckTGLCRow
   */  
export function get_PRCheckTGLCs_Company_HeadNum_TGLCTranNum_Key2(Company:string, HeadNum:string, TGLCTranNum:string, Key2:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PRCheckTGLCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/PRCheckTGLCs(" + Company + "," + HeadNum + "," + TGLCTranNum + "," + Key2 + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PRCheckTGLCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PRCheckTGLC for the service
   Description: Calls UpdateExt to update PRCheckTGLC. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PRCheckTGLC
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param TGLCTranNum Desc: TGLCTranNum   Required: True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PRCheckTGLCRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PRCheckTGLCs_Company_HeadNum_TGLCTranNum_Key2(Company:string, HeadNum:string, TGLCTranNum:string, Key2:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/PRCheckTGLCs(" + Company + "," + HeadNum + "," + TGLCTranNum + "," + Key2 + ")", {
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
   Summary: Call UpdateExt to delete PRCheckTGLC item
   Description: Call UpdateExt to delete PRCheckTGLC item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PRCheckTGLC
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param TGLCTranNum Desc: TGLCTranNum   Required: True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PRCheckTGLCs_Company_HeadNum_TGLCTranNum_Key2(Company:string, HeadNum:string, TGLCTranNum:string, Key2:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/PRCheckTGLCs(" + Company + "," + HeadNum + "," + TGLCTranNum + "," + Key2 + ")", {
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
   Description: Get PRChkDeds items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PRChkDeds
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PRChkDedRow
   */  
export function get_PRChkDeds(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PRChkDedRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/PRChkDeds", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PRChkDedRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PRChkDeds
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PRChkDedRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PRChkDedRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PRChkDeds(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/PRChkDeds", {
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
   Summary: Calls GetByID to retrieve the PRChkDed item
   Description: Calls GetByID to retrieve the PRChkDed item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PRChkDed
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param DeductionID Desc: DeductionID   Required: True   Allow empty value : True
      @param DeductionNum Desc: DeductionNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PRChkDedRow
   */  
export function get_PRChkDeds_Company_HeadNum_DeductionID_DeductionNum(Company:string, HeadNum:string, DeductionID:string, DeductionNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PRChkDedRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/PRChkDeds(" + Company + "," + HeadNum + "," + DeductionID + "," + DeductionNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PRChkDedRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PRChkDed for the service
   Description: Calls UpdateExt to update PRChkDed. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PRChkDed
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param DeductionID Desc: DeductionID   Required: True   Allow empty value : True
      @param DeductionNum Desc: DeductionNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PRChkDedRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PRChkDeds_Company_HeadNum_DeductionID_DeductionNum(Company:string, HeadNum:string, DeductionID:string, DeductionNum:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/PRChkDeds(" + Company + "," + HeadNum + "," + DeductionID + "," + DeductionNum + ")", {
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
   Summary: Call UpdateExt to delete PRChkDed item
   Description: Call UpdateExt to delete PRChkDed item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PRChkDed
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param DeductionID Desc: DeductionID   Required: True   Allow empty value : True
      @param DeductionNum Desc: DeductionNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PRChkDeds_Company_HeadNum_DeductionID_DeductionNum(Company:string, HeadNum:string, DeductionID:string, DeductionNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/PRChkDeds(" + Company + "," + HeadNum + "," + DeductionID + "," + DeductionNum + ")", {
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
   Description: Get PRChkDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PRChkDtls
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PRChkDtlRow
   */  
export function get_PRChkDtls(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PRChkDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/PRChkDtls", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PRChkDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PRChkDtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PRChkDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PRChkDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PRChkDtls(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/PRChkDtls", {
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
   Summary: Calls GetByID to retrieve the PRChkDtl item
   Description: Calls GetByID to retrieve the PRChkDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PRChkDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param LineNum Desc: LineNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PRChkDtlRow
   */  
export function get_PRChkDtls_Company_HeadNum_LineNum(Company:string, HeadNum:string, LineNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PRChkDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/PRChkDtls(" + Company + "," + HeadNum + "," + LineNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PRChkDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PRChkDtl for the service
   Description: Calls UpdateExt to update PRChkDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PRChkDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param LineNum Desc: LineNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PRChkDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PRChkDtls_Company_HeadNum_LineNum(Company:string, HeadNum:string, LineNum:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/PRChkDtls(" + Company + "," + HeadNum + "," + LineNum + ")", {
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
   Summary: Call UpdateExt to delete PRChkDtl item
   Description: Call UpdateExt to delete PRChkDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PRChkDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param LineNum Desc: LineNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PRChkDtls_Company_HeadNum_LineNum(Company:string, HeadNum:string, LineNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/PRChkDtls(" + Company + "," + HeadNum + "," + LineNum + ")", {
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
   Description: Get PRChkTaxes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PRChkTaxes
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PRChkTaxRow
   */  
export function get_PRChkTaxes(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PRChkTaxRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/PRChkTaxes", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PRChkTaxRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PRChkTaxes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PRChkTaxRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PRChkTaxRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PRChkTaxes(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/PRChkTaxes", {
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
   Summary: Calls GetByID to retrieve the PRChkTax item
   Description: Calls GetByID to retrieve the PRChkTax item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PRChkTax
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param TaxTblID Desc: TaxTblID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PRChkTaxRow
   */  
export function get_PRChkTaxes_Company_HeadNum_TaxTblID(Company:string, HeadNum:string, TaxTblID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PRChkTaxRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/PRChkTaxes(" + Company + "," + HeadNum + "," + TaxTblID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PRChkTaxRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PRChkTax for the service
   Description: Calls UpdateExt to update PRChkTax. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PRChkTax
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param TaxTblID Desc: TaxTblID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PRChkTaxRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PRChkTaxes_Company_HeadNum_TaxTblID(Company:string, HeadNum:string, TaxTblID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/PRChkTaxes(" + Company + "," + HeadNum + "," + TaxTblID + ")", {
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
   Summary: Call UpdateExt to delete PRChkTax item
   Description: Call UpdateExt to delete PRChkTax item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PRChkTax
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param TaxTblID Desc: TaxTblID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PRChkTaxes_Company_HeadNum_TaxTblID(Company:string, HeadNum:string, TaxTblID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/PRChkTaxes(" + Company + "," + HeadNum + "," + TaxTblID + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PRCheckListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PRCheckListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PRCheckListRow)
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
   Required: True   Allow empty value : True
   Required: True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClausePRCheck:string, whereClausePRChkDed:string, whereClausePRChkDtl:string, whereClausePRChkTax:string, whereClausePRCheckTGLC:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClausePRCheck!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePRCheck=" + whereClausePRCheck
   }
   if(typeof whereClausePRChkDed!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePRChkDed=" + whereClausePRChkDed
   }
   if(typeof whereClausePRChkDtl!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePRChkDtl=" + whereClausePRChkDtl
   }
   if(typeof whereClausePRChkTax!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePRChkTax=" + whereClausePRChkTax
   }
   if(typeof whereClausePRCheckTGLC!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePRCheckTGLC=" + whereClausePRCheckTGLC
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/GetRows" + params, {
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
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(headNum:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof headNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "headNum=" + headNum
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/GetList" + params, {
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
   Summary: Invoke method GetCodeDescList
   OperationID: GetCodeDescList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCodeDescList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCodeDescList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCodeDescList(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/GetCodeDescList", {
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
   Summary: Invoke method getClientFileName
   OperationID: getClientFileName
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/getClientFileName_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/getClientFileName_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_getClientFileName(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/getClientFileName", {
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
   Summary: Invoke method CalculateDeductsAndTaxes
   Description: Method to call to calculate deductions and taxes.
   OperationID: CalculateDeductsAndTaxes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CalculateDeductsAndTaxes_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CalculateDeductsAndTaxes_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CalculateDeductsAndTaxes(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/CalculateDeductsAndTaxes", {
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
   Summary: Invoke method CalculateOvertime
   Description: Method to call to calculate overtime.
   OperationID: CalculateOvertime
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CalculateOvertime_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CalculateOvertime_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CalculateOvertime(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/CalculateOvertime", {
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
   Summary: Invoke method CalculateOvertimeVerification
   Description: Method to call prior to calling CalculateOvertime.  This method will
return text of a verification message to ask the user to verify the
process should run.  The question is yes-no.  If the answer is yes, proceed
with the calculation of overtime.  If the answer is no, cancel the
calculation of overtime.
   OperationID: CalculateOvertimeVerification
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/CalculateOvertimeVerification_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CalculateOvertimeVerification(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/CalculateOvertimeVerification", {
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
   Summary: Invoke method ChangePRCheckEmpID
   Description: Method to call to when the Employee ID changes.  This method will set
employee fields in PRCheck based on the new employee id.
   OperationID: ChangePRCheckEmpID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePRCheckEmpID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePRCheckEmpID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangePRCheckEmpID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/ChangePRCheckEmpID", {
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
   Summary: Invoke method ChangePRChkDtlAmountType
   Description: Method to call to when the Check Detail Amount Type changes.  This method
will reset values for the new amount type.
   OperationID: ChangePRChkDtlAmountType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePRChkDtlAmountType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePRChkDtlAmountType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangePRChkDtlAmountType(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/ChangePRChkDtlAmountType", {
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
   Summary: Invoke method ChangePRChkDtlBaseHours
   Description: Method to call to when the Check Detail Base Hours changes.  This method
will recalculate detail values based on the new hours.
   OperationID: ChangePRChkDtlBaseHours
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePRChkDtlBaseHours_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePRChkDtlBaseHours_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangePRChkDtlBaseHours(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/ChangePRChkDtlBaseHours", {
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
   Summary: Invoke method RecalcPayRate
   Description: Method to recalculate the pay rate for salaried employees so the base pay will be the same regardless.
   OperationID: RecalcPayRate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RecalcPayRate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RecalcPayRate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RecalcPayRate(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/RecalcPayRate", {
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
   Summary: Invoke method ChangePRChkDtlBasePay
   Description: Method to call to when the Check Detail Base Pay changes.  This method
will recalculate detail values based on the new base pay amount.
   OperationID: ChangePRChkDtlBasePay
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePRChkDtlBasePay_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePRChkDtlBasePay_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangePRChkDtlBasePay(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/ChangePRChkDtlBasePay", {
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
   Summary: Invoke method ChangePRChkDtlPayRate
   Description: Method to call to when the Check Detail Pay Rate changes.  This method
will recalculate detail values based on the new pay rate.
   OperationID: ChangePRChkDtlPayRate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePRChkDtlPayRate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePRChkDtlPayRate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangePRChkDtlPayRate(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/ChangePRChkDtlPayRate", {
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
   Summary: Invoke method ChangePRChkDtlPayrollDate
   Description: Method to call to when the Check Detail Payroll Date changes.  This method
will recalculate detail values if the amount type is calculated.
   OperationID: ChangePRChkDtlPayrollDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePRChkDtlPayrollDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePRChkDtlPayrollDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangePRChkDtlPayrollDate(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/ChangePRChkDtlPayrollDate", {
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
   Summary: Invoke method ChangePRChkDtlPayTypeID
   Description: Method to call to when the Check Detail Pay Type changes.  This method
will recalculate detail values based on the new pay type.
   OperationID: ChangePRChkDtlPayTypeID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePRChkDtlPayTypeID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePRChkDtlPayTypeID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangePRChkDtlPayTypeID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/ChangePRChkDtlPayTypeID", {
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
   Summary: Invoke method ChangePRChkDtlPremiumHours
   Description: Method to call to when the Check Detail Premium Hours changes.  This method
will recalculate detail values based on the new hours.
   OperationID: ChangePRChkDtlPremiumHours
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePRChkDtlPremiumHours_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePRChkDtlPremiumHours_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangePRChkDtlPremiumHours(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/ChangePRChkDtlPremiumHours", {
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
   Summary: Invoke method ChangePRChkDtlPremiumPayType
   Description: Method to call to when the Check Detail Premium Pay Type changes.  This method
will recalculate detail values based on the new pay type.
   OperationID: ChangePRChkDtlPremiumPayType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePRChkDtlPremiumPayType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePRChkDtlPremiumPayType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangePRChkDtlPremiumPayType(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/ChangePRChkDtlPremiumPayType", {
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
   Summary: Invoke method ChangePRChkDtlShift
   Description: Method to call to when the Check Detail Shift changes.  This method
will reassign values based on the new shift.
   OperationID: ChangePRChkDtlShift
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePRChkDtlShift_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePRChkDtlShift_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangePRChkDtlShift(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/ChangePRChkDtlShift", {
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
   Summary: Invoke method CheckDocumentIsLocked
   Description: Method to call when it is necessary to check if document is lock, before doing smth.
   OperationID: CheckDocumentIsLocked
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckDocumentIsLocked_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckDocumentIsLocked_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckDocumentIsLocked(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/CheckDocumentIsLocked", {
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
   Summary: Invoke method CheckPrinted
   Description: Method to call to retrieve the text of the question to ask the user when
checks have been printed.  This question is asked when the user attempts to
add hours, update hours, delete hours, update deductions, or update taxes to
a check.
   OperationID: CheckPrinted
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckPrinted_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckPrinted_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckPrinted(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/CheckPrinted", {
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
   Summary: Invoke method ElecFileDownloaded
   Description: Method to call to retrieve the text of the question to ask the user when
electronic deposit files have been generated.  This question is asked when the user attempts to
add hours, update hours, delete hours, update deductions, or update taxes to
a check.
   OperationID: ElecFileDownloaded
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ElecFileDownloaded_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ElecFileDownloaded_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ElecFileDownloaded(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/ElecFileDownloaded", {
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
   Summary: Invoke method GeneratePayChecks
   Description: Method to call to generate paychecks.
   OperationID: GeneratePayChecks
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GeneratePayChecks_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GeneratePayChecks_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GeneratePayChecks(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/GeneratePayChecks", {
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
   Summary: Invoke method GeneratePayChecksVerification
   Description: Method to call prior to calling GeneratePaychecks.  This method will
return text of a verification message to ask the user to verify the
process should run.  The question is yes-no.  If the answer is yes, proceed
with the check generation.  If the answer is no, cancel the check generation.
   OperationID: GeneratePayChecksVerification
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GeneratePayChecksVerification_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GeneratePayChecksVerification_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GeneratePayChecksVerification(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/GeneratePayChecksVerification", {
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
   Summary: Invoke method GetGLEntries
   Description: Retrieves the GL transactions for each check.
   OperationID: GetGLEntries
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetGLEntries_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetGLEntries_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetGLEntries(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/GetGLEntries", {
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
   Summary: Invoke method GetNewPRCheckForGroup
   Description: Method to call to get a new PRCheck record..
   OperationID: GetNewPRCheckForGroup
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPRCheckForGroup_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPRCheckForGroup_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPRCheckForGroup(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/GetNewPRCheckForGroup", {
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
   Summary: Invoke method GetRowsByEmpID
   Description: Validates the FromOpCode field and poplutes the From OpCode description.  Is called when
the From Op Code changes.  If the code is not valid, an exception will be thrown.
   OperationID: GetRowsByEmpID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsByEmpID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsByEmpID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRowsByEmpID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/GetRowsByEmpID", {
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
   Summary: Invoke method GetRowsFromAutoBankRec
   Description: Called from Automated Bank Reconciliation
   OperationID: GetRowsFromAutoBankRec
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsFromAutoBankRec_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsFromAutoBankRec_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRowsFromAutoBankRec(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/GetRowsFromAutoBankRec", {
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
   Summary: Invoke method UpdatePRChkDed
   Description: Method to call to update a PRChkDed record.  This method should be called
in place of the standard Update method when updating a PRChkDed record.
   OperationID: UpdatePRChkDed
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdatePRChkDed_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdatePRChkDed_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdatePRChkDed(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/UpdatePRChkDed", {
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
   Summary: Invoke method UpdatePRChkTax
   Description: Method to call to update a PRChkTax record.  This method should be called
in place of the standard Update method when updating a PRChkTax record.
   OperationID: UpdatePRChkTax
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdatePRChkTax_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdatePRChkTax_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdatePRChkTax(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/UpdatePRChkTax", {
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
   Summary: Invoke method GetNewPRCheck
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPRCheck
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPRCheck_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPRCheck_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPRCheck(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/GetNewPRCheck", {
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
   Summary: Invoke method GetNewPRChkDed
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPRChkDed
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPRChkDed_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPRChkDed_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPRChkDed(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/GetNewPRChkDed", {
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
   Summary: Invoke method GetNewPRChkDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPRChkDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPRChkDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPRChkDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPRChkDtl(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/GetNewPRChkDtl", {
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
   Summary: Invoke method GetNewPRChkTax
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPRChkTax
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPRChkTax_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPRChkTax_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPRChkTax(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/GetNewPRChkTax", {
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
   Summary: Invoke method GetNewPRCheckTGLC
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPRCheckTGLC
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPRCheckTGLC_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPRCheckTGLC_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPRCheckTGLC(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/GetNewPRCheckTGLC", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PRCheckListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PRCheckListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PRCheckRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PRCheckRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PRCheckTGLCRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PRCheckTGLCRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PRChkDedRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PRChkDedRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PRChkDtlRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PRChkDtlRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PRChkTaxRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PRChkTaxRow[],
}

export interface Erp_Tablesets_PRCheckListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  An internal flag which indicates if this check has been Posted.  If "NO" then it is  considered as still being in the data entry mode. In which case it is still accessible by the check entry programs.  It is set to "Yes" by the posting process.  */  
   "Posted":boolean,
      /**  The data entry "Group" that the check belongs to.  All checks belong to a "Group."  It is assigned to the record during creation using the "current group" that the user is signed into.  It cannot be changed.  The GroupID is used to selectively print and post.  */  
   "GroupID":string,
      /**  An integer automatically assigned by the system using the database sequence called "PRCheckSeq".  HeadNum + Company creates a unique key for the record. This is for internal control only the user never needs to reference.  */  
   "HeadNum":number,
      /**  Encoded value which identifies the employee.  */  
   "EmpLink":string,
      /**  BankAcctId of the BankAcct master that this check was drawn  against. This field is updated during the check printing process for system printed checks or entered by the user for manually printed checks. It must be entered and valid for manual checks. It is invalid if not found or BankAcct.Active = No.  */  
   "BankAcctID":string,
      /**  Check number is assigned during the check printing process for checks that are printed by the system or entered by the user for hand written checks. NOTE:  Posting of the group is not allowed if any CheckHed record exits with a zero check.  */  
   "CheckNum":number,
      /**  Check Date is assigned during the printing process for system printed checks or entered by the user for hand written checks.  */  
   "CheckDate":string,
      /**  Pay period start date for this check.  This is updated as part of the payroll posting process for system generated checks.  It is entered by the user for manual checks.  */  
   "PSDate":string,
      /**  Pay period end date for this check.  This is updated as part of the payroll posting process for system generated checks.  It is entered by the user for manual checks.  */  
   "PEDate":string,
      /**  Fiscal Year that the check is posted to.  Updated during the check printing process for system printed checks or updated based on the CheckDate for hand written checks.  */  
   "FiscalYear":number,
      /**  G/L fiscal period that this check is posted to.  Updated by the check printing process for system printed checks.  For hand written checks it updated by check entry program based on the check date.  */  
   "FiscalPeriod":number,
      /**  Voided flag  */  
   "Voided":boolean,
      /**  Total Base Pay for this check. Not user maintainable.  It summarizes all PRChkDtl for the check.  Updated via PRChkDtl write/delete triggers. The triggers update this with  (BasePay + PremiumPay + PremiumBasePay + ShiftPay)  */  
   "TotalBasePay":number,
      /**  Total Premium Pay for this check.  Not user maintainable.  It summarizes all PRChkDtl.PremiumPay for the check.  Updated via PRChkDtl write/delete triggers.  */  
   "TotalPremiumPay":number,
      /**  Total Shift Pay for this check.  Not user maintainable.  It summarizes all PRChkDtl.ShiftPay for the check.  Updated via PRChkDtl write/delete triggers.  */  
   "TotalShiftPay":number,
      /**  Total of all Tax amounts for the check.  Not user maintainable.  It summarizes all PRChkTax.TaxAmt for the check.  Updated via PRChkTax write/delete triggers.  */  
   "TotalTaxes":number,
      /**  Total of all deduction amounts for the check.  Not user maintainable.  It summarizes all PRChkDed.DeductionAmt for the check.  Updated via PRChkDed write/delete triggers.  */  
   "TotalDeductions":number,
      /**  Total Base Hours on this check. Not directly maintainable by user. A summary of PRChkDtl.BaseHours updated via the PRChkDtl write/delete triggers  */  
   "TotalBaseHours":number,
      /**  Total Premium Hours on this check. Not directly maintainable by user. A summary of PRChkDtl.PremiumHours updated via the PRChkDtl write/delete triggers  */  
   "TotalPremiumHours":number,
      /**  Net Check Amount.  Not directly user maintainable.  Updated as (PRCheck.TotalBasePay + TotalPremiumPay + ShiftPay + NonTaxAmt) - (TotalTaxes + TotalDeductions).  Updated via write trigger on PRCheck.  */  
   "CheckAmt":number,
      /**  Indicates that the check was created using the YTD Startup routines.  This is not a real check.  */  
   "StartupCheck":boolean,
      /**  UserID that created the Check. Assign by the system using the current UserID at the time the record was created.  */  
   "EntryPerson":string,
      /**  The WorkCompCode relates this check to the proper WorkComp master.  Used in the Worker's Comp report.  It is duplicated from the PREmpMas.WorkCompCode during the posting process.  */  
   "WorkCompCode":string,
      /**  Payroll class ID that employee is currently assigned to. A mirror image of PREmpMas. It is kept in sync by the PREmpMas write trigger.  */  
   "ClassID":string,
      /**  A short note which is printed on the check.  */  
   "Note":string,
      /**  Copied from PREmpMas at the time the PRCheck record is created.  */  
   "PayFrequency":string,
      /**  Indicates the check's cleared status.  When the Bank Statement is posted all Pending Transactions and Checks are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  */  
   "ClearedCheck":boolean,
      /**  Indicates that the check is in the process of being cleared.  When the Bank Statement is posted all Pending Transactions and Checks are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  */  
   "ClearedPending":boolean,
      /**  Amount that the bank cleared the check for.  */  
   "ClearedAmt":number,
      /**  Person who cleared the check (System Set).  */  
   "ClearedPerson":string,
      /**  Date that the check was cleared in the system (System Set).  */  
   "ClearedDate":string,
      /**  Time that the check was cleared in the system - in HH:MM:SS format (System Set).  */  
   "ClearedTime":string,
      /**  End Date of the Statement that the check was cleared on.  */  
   "ClearedStmtEndDate":string,
      /**  The identifier of the Bankslip document (bank statement) on which this transaction was cleared by the bank. This is updated via the bank reconciliation process.  This is also written to the related GLJrnDtl records.  */  
   "BankSlip":string,
      /**  This field identifies a bankslip.  */  
   "CashBookNum":number,
      /**  This field identifies a line of a bankslip.  */  
   "CashbookLine":number,
      /**  Fiscal year suffix.  */  
   "FiscalYearSuffix":string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   "FiscalCalendarID":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  MXRecDate  */  
   "MXRecDate":string,
      /**  VoidedDate  */  
   "VoidedDate":string,
   "SocSecNum":string,
   "EmpID":string,
   "AddressList":string,
   "EmpFirstName":string,
   "EmpMiddleInit":string,
   "EmpLastName":string,
   "PhotoFile":string,
   "ImageFile":string,
      /**  Used in VoidPRCheck - User response to a question when GL is not interfaced.  */  
   "PRInterfacedContinue":boolean,
   "EmpLinkFirstName":string,
   "EmpLinkLastName":string,
   "EmpLinkName":string,
      /**  shows is this invoice is blocked in RvLock.  */  
   "IsLcked":boolean,
      /**  Review Journal UID  */  
   "RvnJrnUID":number,
      /**  locked means can not be posted: an invoice is already in review journal or in posting process.  */  
   "LockStatus":string,
      /**  Full description of the bank account.  */  
   "BankAcctIDDescription":string,
      /**  The Bank's full name.  */  
   "BankAcctIDBankName":string,
      /**  Full description of the payroll class.  */  
   "ClassIDDescription":string,
      /**  Description of the workers' compensation code.  */  
   "WorkCompCodeDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PRCheckRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  An internal flag which indicates if this check has been Posted.  If "NO" then it is  considered as still being in the data entry mode. In which case it is still accessible by the check entry programs.  It is set to "Yes" by the posting process.  */  
   "Posted":boolean,
      /**  The data entry "Group" that the check belongs to.  All checks belong to a "Group."  It is assigned to the record during creation using the "current group" that the user is signed into.  It cannot be changed.  The GroupID is used to selectively print and post.  */  
   "GroupID":string,
      /**  An integer automatically assigned by the system using the database sequence called "PRCheckSeq".  HeadNum + Company creates a unique key for the record. This is for internal control only the user never needs to reference.  */  
   "HeadNum":number,
      /**  Encoded value which identifies the employee.  */  
   "EmpLink":string,
      /**  BankAcctId of the BankAcct master that this check was drawn  against. This field is updated during the check printing process for system printed checks or entered by the user for manually printed checks. It must be entered and valid for manual checks. It is invalid if not found or BankAcct.Active = No.  */  
   "BankAcctID":string,
      /**  Check number is assigned during the check printing process for checks that are printed by the system or entered by the user for hand written checks. NOTE:  Posting of the group is not allowed if any CheckHed record exits with a zero check.  */  
   "CheckNum":number,
      /**  Check Date is assigned during the printing process for system printed checks or entered by the user for hand written checks.  */  
   "CheckDate":string,
      /**  Pay period start date for this check.  This is updated as part of the payroll posting process for system generated checks.  It is entered by the user for manual checks.  */  
   "PSDate":string,
      /**  Pay period end date for this check.  This is updated as part of the payroll posting process for system generated checks.  It is entered by the user for manual checks.  */  
   "PEDate":string,
      /**  Fiscal Year that the check is posted to.  Updated during the check printing process for system printed checks or updated based on the CheckDate for hand written checks.  */  
   "FiscalYear":number,
      /**  G/L fiscal period that this check is posted to.  Updated by the check printing process for system printed checks.  For hand written checks it updated by check entry program based on the check date.  */  
   "FiscalPeriod":number,
      /**  Voided flag  */  
   "Voided":boolean,
      /**  Total Base Pay for this check. Not user maintainable.  It summarizes all PRChkDtl for the check.  Updated via PRChkDtl write/delete triggers. The triggers update this with  (BasePay + PremiumPay + PremiumBasePay + ShiftPay)  */  
   "TotalBasePay":number,
      /**  Total Premium Pay for this check.  Not user maintainable.  It summarizes all PRChkDtl.PremiumPay for the check.  Updated via PRChkDtl write/delete triggers.  */  
   "TotalPremiumPay":number,
      /**  Total Shift Pay for this check.  Not user maintainable.  It summarizes all PRChkDtl.ShiftPay for the check.  Updated via PRChkDtl write/delete triggers.  */  
   "TotalShiftPay":number,
      /**  Total of all Tax amounts for the check.  Not user maintainable.  It summarizes all PRChkTax.TaxAmt for the check.  Updated via PRChkTax write/delete triggers.  */  
   "TotalTaxes":number,
      /**  Total of all deduction amounts for the check.  Not user maintainable.  It summarizes all PRChkDed.DeductionAmt for the check.  Updated via PRChkDed write/delete triggers.  */  
   "TotalDeductions":number,
      /**  Total Base Hours on this check. Not directly maintainable by user. A summary of PRChkDtl.BaseHours updated via the PRChkDtl write/delete triggers  */  
   "TotalBaseHours":number,
      /**  Total Premium Hours on this check. Not directly maintainable by user. A summary of PRChkDtl.PremiumHours updated via the PRChkDtl write/delete triggers  */  
   "TotalPremiumHours":number,
      /**  Net Check Amount.  Not directly user maintainable.  Updated as (PRCheck.TotalBasePay + TotalPremiumPay + ShiftPay + NonTaxAmt) - (TotalTaxes + TotalDeductions).  Updated via write trigger on PRCheck.  */  
   "CheckAmt":number,
      /**  Indicates that the check was created using the YTD Startup routines.  This is not a real check.  */  
   "StartupCheck":boolean,
      /**  UserID that created the Check. Assign by the system using the current UserID at the time the record was created.  */  
   "EntryPerson":string,
      /**  The WorkCompCode relates this check to the proper WorkComp master.  Used in the Worker's Comp report.  It is duplicated from the PREmpMas.WorkCompCode during the posting process.  */  
   "WorkCompCode":string,
      /**  Payroll class ID that employee is currently assigned to. A mirror image of PREmpMas. It is kept in sync by the PREmpMas write trigger.  */  
   "ClassID":string,
      /**  A short note which is printed on the check.  */  
   "Note":string,
      /**  Copied from PREmpMas at the time the PRCheck record is created.  */  
   "PayFrequency":string,
      /**  Indicates the check's cleared status.  When the Bank Statement is posted all Pending Transactions and Checks are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  */  
   "ClearedCheck":boolean,
      /**  Indicates that the check is in the process of being cleared.  When the Bank Statement is posted all Pending Transactions and Checks are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  */  
   "ClearedPending":boolean,
      /**  Amount that the bank cleared the check for.  */  
   "ClearedAmt":number,
      /**  Person who cleared the check (System Set).  */  
   "ClearedPerson":string,
      /**  Date that the check was cleared in the system (System Set).  */  
   "ClearedDate":string,
      /**  Time that the check was cleared in the system - in HH:MM:SS format (System Set).  */  
   "ClearedTime":string,
      /**  End Date of the Statement that the check was cleared on.  */  
   "ClearedStmtEndDate":string,
      /**  The identifier of the Bankslip document (bank statement) on which this transaction was cleared by the bank. This is updated via the bank reconciliation process.  This is also written to the related GLJrnDtl records.  */  
   "BankSlip":string,
      /**  This field identifies a bankslip.  */  
   "CashBookNum":number,
      /**  This field identifies a line of a bankslip.  */  
   "CashbookLine":number,
      /**  Fiscal year suffix.  */  
   "FiscalYearSuffix":string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   "FiscalCalendarID":string,
      /**  PaymentNumber  */  
   "PaymentNumber":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  ActiveToPrint  */  
   "ActiveToPrint":boolean,
      /**  MXRecDate  */  
   "MXRecDate":string,
      /**  VoidedDate  */  
   "VoidedDate":string,
   "EmpFirstName":string,
   "EmpID":string,
   "EmpLastName":string,
   "EmpLinkFirstName":string,
   "EmpLinkLastName":string,
   "EmpLinkName":string,
   "EmpMiddleInit":string,
   "ImageFile":string,
      /**  shows is this invoice is blocked in RvLock.  */  
   "IsLcked":boolean,
      /**  locked means can not be posted: an invoice is already in review journal or in posting process.  */  
   "LockStatus":string,
   "PhotoFile":string,
      /**  Used in VoidPRCheck - User response to a question when GL is not interfaced.  */  
   "PRInterfacedContinue":boolean,
      /**  Review Journal UID  */  
   "RvnJrnUID":number,
   "SocSecNum":string,
   "AddressList":string,
      /**  The columns is the formatted by new line separator version of the AddressList column  */  
   "AddressListFormatted":string,
      /**  Display CheckAmt for kinetic  */  
   "DspCheckAmt":number,
      /**  Display CheckDate for kinetic  */  
   "DspCheckDate":string,
      /**  Display CheckNum for kinetic  */  
   "DspCheckNum":number,
   "BitFlag":number,
   "BankAcctIDBankName":string,
   "BankAcctIDDescription":string,
   "ClassIDDescription":string,
   "WorkCompCodeDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PRCheckTGLCRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**   Identifies the master file to which the GL Control is related to.  This field is used to properly isolate controls to the masters they are related to.
For example; Customer, PartClass identifies controls that are related to Customers and Part Classes  */  
   "RelatedToFile":string,
      /**  Major component of the foreign key of the related master record. For example: For a "PORel" control this field would contain the related PO Number.  */  
   "Key1":string,
      /**   2nd component of the foreign key to the related master record.   For example: For a "PORel" control this field would contain the related PO Line Number.
The usage of this field is dependent on the type of record.  */  
   "Key2":string,
      /**  3rd component of the foreign key to the related master record.  For example: For a "PORel" control this field would contain the related PO Release Number.  The usage of this field is dependent record type.  */  
   "Key3":string,
      /**   4th component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
   "Key4":string,
      /**   5th component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
   "Key5":string,
      /**   6th component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
   "Key6":string,
      /**  Internal identifier used to keep records unique for the related record.  The system generates this number by finding the last TranGLC record for the RelatedToFile-Key1-Key2 etc. and adding 1 to it.  */  
   "TGLCTranNum":number,
      /**  String identifier of the account context.  */  
   "GLAcctContext":string,
      /**  Reference to an accounting book.  If not blank must be a valid entry in the GLBook table.  */  
   "BookID":string,
      /**  The chart of account code used by the book.  Will contain the Master COA when BookID is blank.  Reference only.  Used for integrity checking when updating/deleting a GL account.  */  
   "COACode":string,
      /**  Full account containing the non-dynamic segment values up to 200 characters.  Unique identifier for the GL Account.  */  
   "GLAccount":string,
      /**  Indicates if the user can update or delete this record.  */  
   "UserCanModify":boolean,
      /**  Segement Value 1 of the account for this context.  */  
   "SegValue1":string,
      /**  Segement Value 2 of the account for this context.  */  
   "SegValue2":string,
      /**  Segement Value 3 of the account for this context.  */  
   "SegValue3":string,
      /**  Segement Value 4 of the account for this context.  */  
   "SegValue4":string,
      /**  Segement Value 5 of the account for this context.  */  
   "SegValue5":string,
      /**  Segement Value 6 of the account for this context.  */  
   "SegValue6":string,
      /**  Segement Value 7 of the account for this context.  */  
   "SegValue7":string,
      /**  Segement Value 8 of the account for this context.  */  
   "SegValue8":string,
      /**  Segement Value 9 of the account for this context.  */  
   "SegValue9":string,
      /**  Segement Value 10 of the account for this context.  */  
   "SegValue10":string,
      /**  Segement Value 11 of the account for this context.  */  
   "SegValue11":string,
      /**  Segement Value 12 of the account for this context.  */  
   "SegValue12":string,
      /**  Segement Value 13 of the account for this context.  */  
   "SegValue13":string,
      /**  Segement Value 14 of the account for this context.  */  
   "SegValue14":string,
      /**  Segement Value 15 of the account for this context.  */  
   "SegValue15":string,
      /**  Segement Value 16 of the account for this context.  */  
   "SegValue16":string,
      /**  Segement Value 17 of the account for this context.  */  
   "SegValue17":string,
      /**  Segement Value 18 of the account for this context.  */  
   "SegValue18":string,
      /**  Segement Value 19 of the account for this context.  */  
   "SegValue19":string,
      /**  Segement Value 20 of the account for this context.  */  
   "SegValue20":string,
      /**  Unique Identifier of the system GL Control Type.  */  
   "SysGLControlType":string,
      /**  System generated GL Control Identifier.  */  
   "SysGLControlCode":string,
      /**  Global Company identifier.  Used in Multi-Company Journal.  */  
   "ExtCompanyID":string,
      /**  Flag to indicate the account in this record is for an external company.  */  
   "IsExternalCompany":boolean,
      /**  Fiscal year of the related GLJrnDtl.  */  
   "FiscalYear":number,
      /**  JournalCode of the related GLJrnDtl.  */  
   "JournalCode":string,
      /**  Journal number of the related GLJrnDtl.  */  
   "JournalNum":number,
      /**  JournalLine of the related GLJrnDtl.  */  
   "JournalLine":number,
      /**  Transaction date of the transaction.  This is used in order to display the transactions in date order.  */  
   "TranDate":string,
      /**   An internal code to identify the table of  the source transaction.
P = PartTran
L = LaborDtl
I = InvcHead
Note: The system does not combine TranSource when creating GLJrnDtl. That is, a specific GLJrnDtl record can only be related to one source.  */  
   "TranSource":string,
      /**  LaborHedSeq of the related LaborDtl.  Pertains only to source from LaborDtl (TranSource = "L")  */  
   "LaborHedSeq":number,
      /**  LaborDtlSeq of the related LaborDtl. Pertains only to source from LaborDtl (TranSource = "L")  */  
   "LaborDtlSeq":number,
      /**  System date of the related PartTran record.  Pertains only to source from PartTran (TranSource = "P")  */  
   "SysDate":string,
      /**  System time of the related PartTran record.  Pertains only to source from PartTran (TranSource = "P")  */  
   "SysTime":number,
      /**  TranNum of the related PartTran record.  Pertains only to source from PartTran (TranSource = "P")  */  
   "TranNum":number,
      /**  InvoiceNum of the related InvcHead record.  Pertains only to source from PartTran (TranSource = "I")  */  
   "ARInvoiceNum":number,
      /**  Transaction amount that this transaction posted to the related GlJrnDtl.  */  
   "TransAmt":number,
      /**  Invoice Line Number associated with this GL Journal  */  
   "InvoiceLine":number,
      /**  The sequence number associated with this GL journal  */  
   "SeqNum":number,
      /**  The Internal VendorNum that ties back to the Vendor master file.  This field is not directly maintainable.  */  
   "VendorNum":number,
      /**  Vendor's invoice number.  */  
   "APInvoiceNum":string,
      /**  Date record was created  */  
   "CreateDate":string,
      /**  Fiscal year suffix.  */  
   "FiscalYearSuffix":string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   "FiscalCalendarID":string,
      /**  Credit Amount.  */  
   "CreditAmount":number,
      /**  Debit Amount.  */  
   "DebitAmount":number,
      /**  BookCreditAmount  */  
   "BookCreditAmount":number,
      /**  Book Debit Amount  */  
   "BookDebitAmount":number,
      /**  A unique code that identifies the document currency.  */  
   "CurrencyCode":string,
      /**   Indicates if this record contains account data only or reference data such as journal number, amounts, etc.  Valid  values are:
A - account data only
R - reference data  */  
   "RecordType":string,
      /**  When a posting rule creates a pair of journal details balancing each other, each detail in the pair should reference the other one. This allows to show correspondence of accounts in reports. Support of reports that allow this being visible is not in the scope of this change.  */  
   "CorrAccUID":number,
      /**  this field equals ABTUID which was created during posting  */  
   "ABTUID":string,
      /**  Technical identifier.  */  
   "RuleUID":number,
      /**   Identifies if statistical information may be entered for the natural (chart) account.
Accounts can be used only for monetary amounts, both monetary and statistical amounts or only for statistical amounts.
0 = Only used for monetary amounts.
1 = Used for both monetary and statistical amounts.
2 = Only used for statistical amounts.  */  
   "Statistical":number,
      /**  Statistical UOM code.  */  
   "StatUOMCode":string,
      /**  This field shows Debit statistical amount.  */  
   "DebitStatAmt":number,
      /**  This field shows Credit statistical amount.  */  
   "CreditStatAmt":number,
      /**  IsModifiedByUser  */  
   "IsModifiedByUser":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  MovementNum  */  
   "MovementNum":number,
      /**  MovementType  */  
   "MovementType":string,
      /**  Plant  */  
   "Plant":string,
   "HeadNum":number,
   "BitFlag":number,
   "COADescription":string,
   "GLAccountGLAcctDisp":string,
   "GLAccountAccountDesc":string,
   "GLAccountGLShortAcct":string,
   "GLBookDescription":string,
   "GLBookCurrencyCode":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PRChkDedRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Duplicated from related PRCheck.  */  
   "HeadNum":number,
      /**  The deduction Id that this check deduction record is related to.  */  
   "DeductionID":string,
      /**  DeductionNum of the related PREmpDed.  */  
   "DeductionNum":number,
      /**  Deduction Amount scheduled to be taken.  Calculated based on the values stored in PREmpDed. This amount includes any CarryOverAmt.  */  
   "ScheduledAmt":number,
      /**  Indicates if the Deduction Amount is manually calculated.  The system will not calculate the DeductionAmount when ManualCalc = Yes.  */  
   "ManualCalc":boolean,
      /**  An internally assigned integer which controls the order in which deductions are processed. It is created/used by the payroll calculation process. It is not the same thing as the PRDeduct.Priority ! Basically it is a sequential # which was generated by processing the deductions in priority order. An exception is for negative deductions, they are set to zero (highest priority). The CalcOrder comes into play when there are insufficient funds to take all the deductions. When this occurs the deductions are decreased in a descending CalcOrder sequence until the check becomes positive.  */  
   "CalcOrder":number,
      /**  Deduction Amount taken. Normally this is the same a ScheduledAmt, except in the case where there was insufficient pay to take the deduction. In which case this value could be lower.  */  
   "DeductionAmt":number,
      /**  Payroll class ID that employee is currently assigned to.  A mirror image of PREmpMas. It is kept in sync by the PREmpMas write trigger.  */  
   "ClassID":string,
      /**  Mirror image of PRCheck.Posted.  */  
   "Posted":boolean,
      /**  Encoded value which identifies the employee. Mirror image of PRCheck.EmpLink.  */  
   "EmpLink":string,
      /**  mirror image of PRCheck.CheckDate  */  
   "CheckDate":string,
      /**  Deduction Year to date amount taken.  */  
   "PriorDedYTD":number,
      /**   An internal flag indicating if this is a Void payment transaction.
This is set by the P/R void check program.  */  
   "Voided":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  PrintHeadNum  */  
   "PrintHeadNum":number,
   "EmpID":string,
      /**  First name of employee.  */  
   "FirstName":string,
   "GroupID":string,
      /**  Last name of employee  */  
   "LastName":string,
      /**  This is the employees full name. This is not directly maintainable. It is a concatenation of the FirstName + MiddleInitial + LastName fields. It exists so that it can be used in browses or where ever the complete name in a first, middle, last fashion is required.  */  
   "Name":string,
   "Reference":string,
   "BitFlag":number,
   "ClassIDDescription":string,
   "DeductionIDDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PRChkDtlRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Duplicated from the related PRCheck.  */  
   "HeadNum":number,
      /**  Integer assigned by the system which is used as one of the fields to uniquely identify the PRChkDtl record.  */  
   "LineNum":number,
      /**  Date that the employee worked or earned the pay.  */  
   "PayrollDate":string,
      /**   Identifies the Pay type of this payment record.  A foreign key to the PayType master table.  This must be a valid PayType where PayType.PremiumFactor <= 1.00.
Ex:( Regular, Holiday, Sick, Vacation . . .)  */  
   "PayTypeID":string,
      /**  The employee's base hourly pay rate.  This rate does not include premium or shift differential factors.  It is defaulted from the PREmpMas.PayRate field.  */  
   "PayRate":number,
      /**   Hours for non premium time.  Maintainable only if PayTypeID is not blank.
Stored as Hours.Hundreths. For example 3 1/2 hours is stored as 3.5  */  
   "BaseHours":number,
      /**  Base pay is the pay amount calculated non-premium hours employees base pay rate.  (see PremiumPay, ShiftPay).  It is calculated as  (BaseHours * PayRate) or set = to the employee salary amount.  It can be overridden in hours entry for salaried employees.  */  
   "BasePay":number,
      /**  Identifies the premium Paytype of this payment record (Ex: OT, etc.).  A foreign key to the PayType master table.  This must be a valid PayType where PayType.PremiumFactor > 1.00.  */  
   "PremiumPayType":string,
      /**   Hours to be paid at the premium rate.  This is stored as Hours.Hundreths. For example 3 1/2 hours is stored as 3.5
This is disabled and zero if PremiumPaytype = blank.  */  
   "PremiumHours":number,
      /**   The amount paid for premium hours not including the premium amount.  Not directly maintainable. (PremiumPayHours* Payrate )
Ex: rate = $10.00,  hours = 3, PremiumBasePay = 30.00. 
The Base Pay portion of the total premium pay amount  is kept separate from the Premium Pay portion for users who wish to track the premium portion of overtime expenses separately in general ledger.  */  
   "PremiumBasePay":number,
      /**   Premium pay is the additional amount above the base pay that is being paid as a premium for this pay type. It is not directly maintainable.
For example PayHours = 8, PayRate = 10.00 and PremiumFactor = 1.5,  BasePay would be 80.00 and PremiumPay would be 40.00.
The Base Pay is kept separate from the Premium Pay for users who wish to track the premium portion of the pay separately in general ledger.
PremiumPayHours * (Payrate * (PremiumFactor - 1.00)).  */  
   "PremiumPay":number,
      /**   Defaults from the EmpBasic.Shift when entered through payroll hours entry, or was from LaborHed.Shift is the case the record was created from labor transfer process.
Note:  When shift is changed in check entry the pay amounts may need to be recalculated if shift pay is active.  */  
   "Shift":number,
      /**   Shift pay is the amount paid due to shift differential.
(BaseHours * ShiftDifferential)  + 
PremiumHours * (ShiftDifferential * PremiumFactor).
PremiumFactor  is used only if PayType.IncludeShift = Yes. 
Note: Shift differential is either an additional percentage of payrate or an additional flat amount.  
For example PayHours = 8, PayRate = 10.00 and Shift differential is an extra 1.00 per hour. ShiftPay would be $8.00.
This is refreshed when changes are made to Shift, PayRate, or PayHours or PremiumHours or PayType.  */  
   "ShiftPay":number,
      /**  Payroll class ID that employee is currently assigned to. A mirror image of PREmpMas. It is kept in sync by the PREmpMas write trigger.  */  
   "ClassID":string,
      /**  Mirror image of PRCheck.Posted.  */  
   "Posted":boolean,
      /**  Encoded value which identifies the employee. Mirror image of PRCheck.EmpLink.  */  
   "EmpLink":string,
      /**  mirror image of PRCheck.CheckDate.  This is not updated until the checks are posted.  */  
   "CheckDate":string,
      /**  A internally used flag which indicates that this record was generated from a LaborHed record.  */  
   "FromLabor":boolean,
      /**   An internal flag indicating if this is a Void payment transaction.
This is set by the P/R void check program.  */  
   "Voided":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  PrintHeadNum  */  
   "PrintHeadNum":number,
      /**  IsOutdatedLabor  */  
   "IsOutdatedLabor":boolean,
   "DiffMethod":string,
   "DiffMethodDesc":string,
   "DiffQualifier":string,
   "DiffQualifierDesc":string,
   "DiffRate":number,
   "EmpID":string,
      /**  First name of employee.  */  
   "FirstName":string,
   "GroupID":string,
      /**  Last name of employee  */  
   "LastName":string,
      /**  This is the employees full name. This is not directly maintainable. It is a concatenation of the FirstName + MiddleInitial + LastName fields. It exists so that it can be used in browses or where ever the complete name in a first, middle, last fashion is required.  */  
   "Name":string,
   "ShiftTimesDesc":string,
   "TotalHours":number,
   "TotalPay":number,
      /**  Used in VoidPRCheck - Date the check was voided.  */  
   "VoidedDate":string,
   "AmountType":string,
      /**   DateRange specifies the range between record is created depending of payroll frequency, the possible values are:
"Outdated", labor processed before period begins
"In Pay Range", labor processed between perido begin and period ending
"Outrunning". labor processed after period ending  */  
   "DateRange":string,
   "BitFlag":number,
   "ClassIDDescription":string,
   "PayTypeIDDescription":string,
   "PremiumPayTypeIDDescription":string,
   "ShiftDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PRChkTaxRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Duplicated from related PRCheck.  */  
   "HeadNum":number,
      /**  Tax Table ID  */  
   "TaxTblID":string,
      /**  Identifies the type of tax table.  Valid values are "FIT" - Federal, "SIT" - State, "FUTA" - Federal Unemployment, "SUTA" - State Unemployment,  "SS" - Social Security, "MED" - Medicare, "CITY" - Local, "CNTY" - County, "OTHR" - Other.  */  
   "TaxType":string,
      /**  Payroll class ID that employee is currently assigned to. A mirror image of PREmpMas. It is kept in sync by the PREmpMas write trigger.  */  
   "ClassID":string,
      /**  Mirror image of PRCheck.Posted.  */  
   "Posted":boolean,
      /**  Encoded value which identifies the employee. Mirror image of PRCheck.EmpLink.  */  
   "EmpLink":string,
      /**  mirror image of PRCheck.CheckDate  */  
   "CheckDate":string,
      /**  Amount withheld on this check for a specific tax.  */  
   "TaxAmt":number,
      /**  The Year to Date tax withheld  prior to this check. Current YTD is PriorTaxYTD + TaxAmt.  */  
   "PriorTaxYTD":number,
      /**  Taxable hours on this check for the tax jurisdiction.  This is the BaseHours and PremiumHours if the PayType is not exempt from the tax jurisdiction.  */  
   "TaxableHours":number,
      /**  The taxable amount of supplemental pay for this check  for the tax jurisdiction.  */  
   "SupTaxableAmt":number,
      /**  The hours accumulated from supplemental pay records.  This is used in tax calc when tax basis is % of hours.  */  
   "SupTaxableHours":number,
      /**  Pay check amount that is considered as taxable for this tax jurisdiction. This is calculated by the system as part of the payroll calculate routine.  */  
   "TaxableAmt":number,
      /**  The Year to Date taxable amount prior to this check. Current YTD is PriorTaxableYTD + TaxableAmt.  */  
   "PriorTaxableYTD":number,
      /**  Indicates if this tax record for the check is taxable as of the check date. Of course, if a tax was first taken it would have been taxable. This flag is used so that if after the check is posted it is discovered that it was taken in error the user can set this to NO which would reduce the year to date taxable amount from this date forward. This situation should not be a common occurrence; however it's more likely when employees' have multiple taxes that are deactivated/activated during the same year. It does not change the Tax withheld only taxable.  This flag is needed so that the "Recalculate" taxable amounts would work correctly.  */  
   "Active":boolean,
      /**  Indicates if the Tax Amount is manually calculated.  The system will not calculate the TaxAmount when ManualCalc = Yes.  */  
   "ManualCalc":boolean,
      /**   An internal flag indicating if this is a Void payment transaction.
This is set by the P/R void check program.  */  
   "Voided":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  PrintHeadNum  */  
   "PrintHeadNum":number,
   "CreditAmount":number,
   "EmpID":string,
   "FilingStatus":string,
      /**  First name of employee.  */  
   "FirstName":string,
   "GroupID":string,
      /**  Last name of employee  */  
   "LastName":string,
      /**  This is the employees full name. This is not directly maintainable. It is a concatenation of the FirstName + MiddleInitial + LastName fields. It exists so that it can be used in browses or where ever the complete name in a first, middle, last fashion is required.  */  
   "Name":string,
   "TaxDesc":string,
   "BitFlag":number,
   "ClassIDDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param GroupID
      @param HeadNum
      @param ds
   */  
export interface CalculateDeductsAndTaxes_input{
      /**  The group id to calculate deductions and taxes for  */  
   GroupID:string,
      /**  The current PRCheck.HeadNum record.  Is used to
            rebuild the dataset so the data is current  */  
   HeadNum:number,
   ds:Erp_Tablesets_PayrollCheckEntryTableset[],
}

export interface CalculateDeductsAndTaxes_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PayrollCheckEntryTableset[],
}
}

export interface CalculateOvertimeVerification_output{
parameters : {
      /**  output parameters  */  
   VerificationMsg:string,
}
}

   /** Required : 
      @param GroupID
      @param HeadNum
      @param ds
   */  
export interface CalculateOvertime_input{
      /**  The group id to calculate overtime for  */  
   GroupID:string,
      /**  The current PRCheck.HeadNum record.  Is used to
            rebuild the dataset so the data is current  */  
   HeadNum:number,
   ds:Erp_Tablesets_PayrollCheckEntryTableset[],
}

export interface CalculateOvertime_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PayrollCheckEntryTableset[],
}
}

   /** Required : 
      @param ProposedEmpID
      @param ds
   */  
export interface ChangePRCheckEmpID_input{
      /**  The proposed employee id  */  
   ProposedEmpID:string,
   ds:Erp_Tablesets_PayrollCheckEntryTableset[],
}

export interface ChangePRCheckEmpID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PayrollCheckEntryTableset[],
}
}

   /** Required : 
      @param PRChkDtlKey
      @param ProposedAmountType
      @param ds
   */  
export interface ChangePRChkDtlAmountType_input{
      /**  PRChkDtl Key of row to update ProposedBaseHours Company/HeadNum/LineNum  */  
   PRChkDtlKey:string,
      /**  The proposed amount type  */  
   ProposedAmountType:string,
   ds:Erp_Tablesets_PayrollCheckEntryTableset[],
}

export interface ChangePRChkDtlAmountType_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PayrollCheckEntryTableset[],
}
}

   /** Required : 
      @param PRChkDtlKey
      @param ProposedBaseHours
      @param ds
   */  
export interface ChangePRChkDtlBaseHours_input{
      /**  PRChkDtl Key of row to update ProposedBaseHours Company/HeadNum/LineNum  */  
   PRChkDtlKey:string,
      /**  The proposed base hours  */  
   ProposedBaseHours:number,
   ds:Erp_Tablesets_PayrollCheckEntryTableset[],
}

export interface ChangePRChkDtlBaseHours_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PayrollCheckEntryTableset[],
}
}

   /** Required : 
      @param ProposedBasePay
      @param ds
   */  
export interface ChangePRChkDtlBasePay_input{
      /**  The proposed base pay amount  */  
   ProposedBasePay:number,
   ds:Erp_Tablesets_PayrollCheckEntryTableset[],
}

export interface ChangePRChkDtlBasePay_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PayrollCheckEntryTableset[],
}
}

   /** Required : 
      @param PRChkDtlKey
      @param ProposedPayRate
      @param ds
   */  
export interface ChangePRChkDtlPayRate_input{
      /**  PRChkDtl Key of row to update ProposedBaseHours Company/HeadNum/LineNum  */  
   PRChkDtlKey:string,
      /**  The proposed pay rate  */  
   ProposedPayRate:number,
   ds:Erp_Tablesets_PayrollCheckEntryTableset[],
}

export interface ChangePRChkDtlPayRate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PayrollCheckEntryTableset[],
}
}

   /** Required : 
      @param PRChkDtlKey
      @param ProposedPayTypeID
      @param ds
   */  
export interface ChangePRChkDtlPayTypeID_input{
      /**  PRChkDtl Key of row to update ProposedBaseHours Company/HeadNum/LineNum  */  
   PRChkDtlKey:string,
      /**  The proposed pay type id  */  
   ProposedPayTypeID:string,
   ds:Erp_Tablesets_PayrollCheckEntryTableset[],
}

export interface ChangePRChkDtlPayTypeID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PayrollCheckEntryTableset[],
}
}

   /** Required : 
      @param ProposedPayrollDate
      @param ds
   */  
export interface ChangePRChkDtlPayrollDate_input{
      /**  The proposed payroll date  */  
   ProposedPayrollDate:string,
   ds:Erp_Tablesets_PayrollCheckEntryTableset[],
}

export interface ChangePRChkDtlPayrollDate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PayrollCheckEntryTableset[],
}
}

   /** Required : 
      @param PRChkDtlKey
      @param ProposedPremiumHours
      @param ds
   */  
export interface ChangePRChkDtlPremiumHours_input{
      /**  PRChkDtl Key of row to update ProposedBaseHours Company/HeadNum/LineNum  */  
   PRChkDtlKey:string,
      /**  The proposed premium hours  */  
   ProposedPremiumHours:number,
   ds:Erp_Tablesets_PayrollCheckEntryTableset[],
}

export interface ChangePRChkDtlPremiumHours_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PayrollCheckEntryTableset[],
}
}

   /** Required : 
      @param PRChkDtlKey
      @param ProposedPremiumPayType
      @param ds
   */  
export interface ChangePRChkDtlPremiumPayType_input{
      /**  PRChkDtl Key of row to update ProposedBaseHours Company/HeadNum/LineNum  */  
   PRChkDtlKey:string,
      /**  The proposed premium pay type id  */  
   ProposedPremiumPayType:string,
   ds:Erp_Tablesets_PayrollCheckEntryTableset[],
}

export interface ChangePRChkDtlPremiumPayType_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PayrollCheckEntryTableset[],
}
}

   /** Required : 
      @param PRChkDtlKey
      @param ProposedShift
      @param ds
   */  
export interface ChangePRChkDtlShift_input{
      /**  PRChkDtl Key of row to update ProposedBaseHours Company/HeadNum/LineNum  */  
   PRChkDtlKey:string,
      /**  The proposed shift  */  
   ProposedShift:number,
   ds:Erp_Tablesets_PayrollCheckEntryTableset[],
}

export interface ChangePRChkDtlShift_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PayrollCheckEntryTableset[],
}
}

   /** Required : 
      @param keyValue
   */  
export interface CheckDocumentIsLocked_input{
      /**  HeadNum  */  
   keyValue:string,
}

export interface CheckDocumentIsLocked_output{
}

   /** Required : 
      @param GroupID
   */  
export interface CheckPrinted_input{
      /**  The group id the check is assigned to  */  
   GroupID:string,
}

export interface CheckPrinted_output{
parameters : {
      /**  output parameters  */  
   QuestionText:string,
}
}

   /** Required : 
      @param headNum
   */  
export interface DeleteByID_input{
   headNum:number,
}

export interface DeleteByID_output{
}

   /** Required : 
      @param GroupID
   */  
export interface ElecFileDownloaded_input{
      /**  The group id the check is assigned to  */  
   GroupID:string,
}

export interface ElecFileDownloaded_output{
parameters : {
      /**  output parameters  */  
   QuestionText:string,
}
}

export interface Erp_Tablesets_PRCheckListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  An internal flag which indicates if this check has been Posted.  If "NO" then it is  considered as still being in the data entry mode. In which case it is still accessible by the check entry programs.  It is set to "Yes" by the posting process.  */  
   Posted:boolean,
      /**  The data entry "Group" that the check belongs to.  All checks belong to a "Group."  It is assigned to the record during creation using the "current group" that the user is signed into.  It cannot be changed.  The GroupID is used to selectively print and post.  */  
   GroupID:string,
      /**  An integer automatically assigned by the system using the database sequence called "PRCheckSeq".  HeadNum + Company creates a unique key for the record. This is for internal control only the user never needs to reference.  */  
   HeadNum:number,
      /**  Encoded value which identifies the employee.  */  
   EmpLink:string,
      /**  BankAcctId of the BankAcct master that this check was drawn  against. This field is updated during the check printing process for system printed checks or entered by the user for manually printed checks. It must be entered and valid for manual checks. It is invalid if not found or BankAcct.Active = No.  */  
   BankAcctID:string,
      /**  Check number is assigned during the check printing process for checks that are printed by the system or entered by the user for hand written checks. NOTE:  Posting of the group is not allowed if any CheckHed record exits with a zero check.  */  
   CheckNum:number,
      /**  Check Date is assigned during the printing process for system printed checks or entered by the user for hand written checks.  */  
   CheckDate:string,
      /**  Pay period start date for this check.  This is updated as part of the payroll posting process for system generated checks.  It is entered by the user for manual checks.  */  
   PSDate:string,
      /**  Pay period end date for this check.  This is updated as part of the payroll posting process for system generated checks.  It is entered by the user for manual checks.  */  
   PEDate:string,
      /**  Fiscal Year that the check is posted to.  Updated during the check printing process for system printed checks or updated based on the CheckDate for hand written checks.  */  
   FiscalYear:number,
      /**  G/L fiscal period that this check is posted to.  Updated by the check printing process for system printed checks.  For hand written checks it updated by check entry program based on the check date.  */  
   FiscalPeriod:number,
      /**  Voided flag  */  
   Voided:boolean,
      /**  Total Base Pay for this check. Not user maintainable.  It summarizes all PRChkDtl for the check.  Updated via PRChkDtl write/delete triggers. The triggers update this with  (BasePay + PremiumPay + PremiumBasePay + ShiftPay)  */  
   TotalBasePay:number,
      /**  Total Premium Pay for this check.  Not user maintainable.  It summarizes all PRChkDtl.PremiumPay for the check.  Updated via PRChkDtl write/delete triggers.  */  
   TotalPremiumPay:number,
      /**  Total Shift Pay for this check.  Not user maintainable.  It summarizes all PRChkDtl.ShiftPay for the check.  Updated via PRChkDtl write/delete triggers.  */  
   TotalShiftPay:number,
      /**  Total of all Tax amounts for the check.  Not user maintainable.  It summarizes all PRChkTax.TaxAmt for the check.  Updated via PRChkTax write/delete triggers.  */  
   TotalTaxes:number,
      /**  Total of all deduction amounts for the check.  Not user maintainable.  It summarizes all PRChkDed.DeductionAmt for the check.  Updated via PRChkDed write/delete triggers.  */  
   TotalDeductions:number,
      /**  Total Base Hours on this check. Not directly maintainable by user. A summary of PRChkDtl.BaseHours updated via the PRChkDtl write/delete triggers  */  
   TotalBaseHours:number,
      /**  Total Premium Hours on this check. Not directly maintainable by user. A summary of PRChkDtl.PremiumHours updated via the PRChkDtl write/delete triggers  */  
   TotalPremiumHours:number,
      /**  Net Check Amount.  Not directly user maintainable.  Updated as (PRCheck.TotalBasePay + TotalPremiumPay + ShiftPay + NonTaxAmt) - (TotalTaxes + TotalDeductions).  Updated via write trigger on PRCheck.  */  
   CheckAmt:number,
      /**  Indicates that the check was created using the YTD Startup routines.  This is not a real check.  */  
   StartupCheck:boolean,
      /**  UserID that created the Check. Assign by the system using the current UserID at the time the record was created.  */  
   EntryPerson:string,
      /**  The WorkCompCode relates this check to the proper WorkComp master.  Used in the Worker's Comp report.  It is duplicated from the PREmpMas.WorkCompCode during the posting process.  */  
   WorkCompCode:string,
      /**  Payroll class ID that employee is currently assigned to. A mirror image of PREmpMas. It is kept in sync by the PREmpMas write trigger.  */  
   ClassID:string,
      /**  A short note which is printed on the check.  */  
   Note:string,
      /**  Copied from PREmpMas at the time the PRCheck record is created.  */  
   PayFrequency:string,
      /**  Indicates the check's cleared status.  When the Bank Statement is posted all Pending Transactions and Checks are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  */  
   ClearedCheck:boolean,
      /**  Indicates that the check is in the process of being cleared.  When the Bank Statement is posted all Pending Transactions and Checks are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  */  
   ClearedPending:boolean,
      /**  Amount that the bank cleared the check for.  */  
   ClearedAmt:number,
      /**  Person who cleared the check (System Set).  */  
   ClearedPerson:string,
      /**  Date that the check was cleared in the system (System Set).  */  
   ClearedDate:string,
      /**  Time that the check was cleared in the system - in HH:MM:SS format (System Set).  */  
   ClearedTime:string,
      /**  End Date of the Statement that the check was cleared on.  */  
   ClearedStmtEndDate:string,
      /**  The identifier of the Bankslip document (bank statement) on which this transaction was cleared by the bank. This is updated via the bank reconciliation process.  This is also written to the related GLJrnDtl records.  */  
   BankSlip:string,
      /**  This field identifies a bankslip.  */  
   CashBookNum:number,
      /**  This field identifies a line of a bankslip.  */  
   CashbookLine:number,
      /**  Fiscal year suffix.  */  
   FiscalYearSuffix:string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   FiscalCalendarID:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  MXRecDate  */  
   MXRecDate:string,
      /**  VoidedDate  */  
   VoidedDate:string,
   SocSecNum:string,
   EmpID:string,
   AddressList:string,
   EmpFirstName:string,
   EmpMiddleInit:string,
   EmpLastName:string,
   PhotoFile:string,
   ImageFile:string,
      /**  Used in VoidPRCheck - User response to a question when GL is not interfaced.  */  
   PRInterfacedContinue:boolean,
   EmpLinkFirstName:string,
   EmpLinkLastName:string,
   EmpLinkName:string,
      /**  shows is this invoice is blocked in RvLock.  */  
   IsLcked:boolean,
      /**  Review Journal UID  */  
   RvnJrnUID:number,
      /**  locked means can not be posted: an invoice is already in review journal or in posting process.  */  
   LockStatus:string,
      /**  Full description of the bank account.  */  
   BankAcctIDDescription:string,
      /**  The Bank's full name.  */  
   BankAcctIDBankName:string,
      /**  Full description of the payroll class.  */  
   ClassIDDescription:string,
      /**  Description of the workers' compensation code.  */  
   WorkCompCodeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PRCheckListTableset{
   PRCheckList:Erp_Tablesets_PRCheckListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_PRCheckRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  An internal flag which indicates if this check has been Posted.  If "NO" then it is  considered as still being in the data entry mode. In which case it is still accessible by the check entry programs.  It is set to "Yes" by the posting process.  */  
   Posted:boolean,
      /**  The data entry "Group" that the check belongs to.  All checks belong to a "Group."  It is assigned to the record during creation using the "current group" that the user is signed into.  It cannot be changed.  The GroupID is used to selectively print and post.  */  
   GroupID:string,
      /**  An integer automatically assigned by the system using the database sequence called "PRCheckSeq".  HeadNum + Company creates a unique key for the record. This is for internal control only the user never needs to reference.  */  
   HeadNum:number,
      /**  Encoded value which identifies the employee.  */  
   EmpLink:string,
      /**  BankAcctId of the BankAcct master that this check was drawn  against. This field is updated during the check printing process for system printed checks or entered by the user for manually printed checks. It must be entered and valid for manual checks. It is invalid if not found or BankAcct.Active = No.  */  
   BankAcctID:string,
      /**  Check number is assigned during the check printing process for checks that are printed by the system or entered by the user for hand written checks. NOTE:  Posting of the group is not allowed if any CheckHed record exits with a zero check.  */  
   CheckNum:number,
      /**  Check Date is assigned during the printing process for system printed checks or entered by the user for hand written checks.  */  
   CheckDate:string,
      /**  Pay period start date for this check.  This is updated as part of the payroll posting process for system generated checks.  It is entered by the user for manual checks.  */  
   PSDate:string,
      /**  Pay period end date for this check.  This is updated as part of the payroll posting process for system generated checks.  It is entered by the user for manual checks.  */  
   PEDate:string,
      /**  Fiscal Year that the check is posted to.  Updated during the check printing process for system printed checks or updated based on the CheckDate for hand written checks.  */  
   FiscalYear:number,
      /**  G/L fiscal period that this check is posted to.  Updated by the check printing process for system printed checks.  For hand written checks it updated by check entry program based on the check date.  */  
   FiscalPeriod:number,
      /**  Voided flag  */  
   Voided:boolean,
      /**  Total Base Pay for this check. Not user maintainable.  It summarizes all PRChkDtl for the check.  Updated via PRChkDtl write/delete triggers. The triggers update this with  (BasePay + PremiumPay + PremiumBasePay + ShiftPay)  */  
   TotalBasePay:number,
      /**  Total Premium Pay for this check.  Not user maintainable.  It summarizes all PRChkDtl.PremiumPay for the check.  Updated via PRChkDtl write/delete triggers.  */  
   TotalPremiumPay:number,
      /**  Total Shift Pay for this check.  Not user maintainable.  It summarizes all PRChkDtl.ShiftPay for the check.  Updated via PRChkDtl write/delete triggers.  */  
   TotalShiftPay:number,
      /**  Total of all Tax amounts for the check.  Not user maintainable.  It summarizes all PRChkTax.TaxAmt for the check.  Updated via PRChkTax write/delete triggers.  */  
   TotalTaxes:number,
      /**  Total of all deduction amounts for the check.  Not user maintainable.  It summarizes all PRChkDed.DeductionAmt for the check.  Updated via PRChkDed write/delete triggers.  */  
   TotalDeductions:number,
      /**  Total Base Hours on this check. Not directly maintainable by user. A summary of PRChkDtl.BaseHours updated via the PRChkDtl write/delete triggers  */  
   TotalBaseHours:number,
      /**  Total Premium Hours on this check. Not directly maintainable by user. A summary of PRChkDtl.PremiumHours updated via the PRChkDtl write/delete triggers  */  
   TotalPremiumHours:number,
      /**  Net Check Amount.  Not directly user maintainable.  Updated as (PRCheck.TotalBasePay + TotalPremiumPay + ShiftPay + NonTaxAmt) - (TotalTaxes + TotalDeductions).  Updated via write trigger on PRCheck.  */  
   CheckAmt:number,
      /**  Indicates that the check was created using the YTD Startup routines.  This is not a real check.  */  
   StartupCheck:boolean,
      /**  UserID that created the Check. Assign by the system using the current UserID at the time the record was created.  */  
   EntryPerson:string,
      /**  The WorkCompCode relates this check to the proper WorkComp master.  Used in the Worker's Comp report.  It is duplicated from the PREmpMas.WorkCompCode during the posting process.  */  
   WorkCompCode:string,
      /**  Payroll class ID that employee is currently assigned to. A mirror image of PREmpMas. It is kept in sync by the PREmpMas write trigger.  */  
   ClassID:string,
      /**  A short note which is printed on the check.  */  
   Note:string,
      /**  Copied from PREmpMas at the time the PRCheck record is created.  */  
   PayFrequency:string,
      /**  Indicates the check's cleared status.  When the Bank Statement is posted all Pending Transactions and Checks are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  */  
   ClearedCheck:boolean,
      /**  Indicates that the check is in the process of being cleared.  When the Bank Statement is posted all Pending Transactions and Checks are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  */  
   ClearedPending:boolean,
      /**  Amount that the bank cleared the check for.  */  
   ClearedAmt:number,
      /**  Person who cleared the check (System Set).  */  
   ClearedPerson:string,
      /**  Date that the check was cleared in the system (System Set).  */  
   ClearedDate:string,
      /**  Time that the check was cleared in the system - in HH:MM:SS format (System Set).  */  
   ClearedTime:string,
      /**  End Date of the Statement that the check was cleared on.  */  
   ClearedStmtEndDate:string,
      /**  The identifier of the Bankslip document (bank statement) on which this transaction was cleared by the bank. This is updated via the bank reconciliation process.  This is also written to the related GLJrnDtl records.  */  
   BankSlip:string,
      /**  This field identifies a bankslip.  */  
   CashBookNum:number,
      /**  This field identifies a line of a bankslip.  */  
   CashbookLine:number,
      /**  Fiscal year suffix.  */  
   FiscalYearSuffix:string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   FiscalCalendarID:string,
      /**  PaymentNumber  */  
   PaymentNumber:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  ActiveToPrint  */  
   ActiveToPrint:boolean,
      /**  MXRecDate  */  
   MXRecDate:string,
      /**  VoidedDate  */  
   VoidedDate:string,
   EmpFirstName:string,
   EmpID:string,
   EmpLastName:string,
   EmpLinkFirstName:string,
   EmpLinkLastName:string,
   EmpLinkName:string,
   EmpMiddleInit:string,
   ImageFile:string,
      /**  shows is this invoice is blocked in RvLock.  */  
   IsLcked:boolean,
      /**  locked means can not be posted: an invoice is already in review journal or in posting process.  */  
   LockStatus:string,
   PhotoFile:string,
      /**  Used in VoidPRCheck - User response to a question when GL is not interfaced.  */  
   PRInterfacedContinue:boolean,
      /**  Review Journal UID  */  
   RvnJrnUID:number,
   SocSecNum:string,
   AddressList:string,
      /**  The columns is the formatted by new line separator version of the AddressList column  */  
   AddressListFormatted:string,
      /**  Display CheckAmt for kinetic  */  
   DspCheckAmt:number,
      /**  Display CheckDate for kinetic  */  
   DspCheckDate:string,
      /**  Display CheckNum for kinetic  */  
   DspCheckNum:number,
   BitFlag:number,
   BankAcctIDBankName:string,
   BankAcctIDDescription:string,
   ClassIDDescription:string,
   WorkCompCodeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PRCheckTGLCRow{
      /**  Company Identifier.  */  
   Company:string,
      /**   Identifies the master file to which the GL Control is related to.  This field is used to properly isolate controls to the masters they are related to.
For example; Customer, PartClass identifies controls that are related to Customers and Part Classes  */  
   RelatedToFile:string,
      /**  Major component of the foreign key of the related master record. For example: For a "PORel" control this field would contain the related PO Number.  */  
   Key1:string,
      /**   2nd component of the foreign key to the related master record.   For example: For a "PORel" control this field would contain the related PO Line Number.
The usage of this field is dependent on the type of record.  */  
   Key2:string,
      /**  3rd component of the foreign key to the related master record.  For example: For a "PORel" control this field would contain the related PO Release Number.  The usage of this field is dependent record type.  */  
   Key3:string,
      /**   4th component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
   Key4:string,
      /**   5th component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
   Key5:string,
      /**   6th component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
   Key6:string,
      /**  Internal identifier used to keep records unique for the related record.  The system generates this number by finding the last TranGLC record for the RelatedToFile-Key1-Key2 etc. and adding 1 to it.  */  
   TGLCTranNum:number,
      /**  String identifier of the account context.  */  
   GLAcctContext:string,
      /**  Reference to an accounting book.  If not blank must be a valid entry in the GLBook table.  */  
   BookID:string,
      /**  The chart of account code used by the book.  Will contain the Master COA when BookID is blank.  Reference only.  Used for integrity checking when updating/deleting a GL account.  */  
   COACode:string,
      /**  Full account containing the non-dynamic segment values up to 200 characters.  Unique identifier for the GL Account.  */  
   GLAccount:string,
      /**  Indicates if the user can update or delete this record.  */  
   UserCanModify:boolean,
      /**  Segement Value 1 of the account for this context.  */  
   SegValue1:string,
      /**  Segement Value 2 of the account for this context.  */  
   SegValue2:string,
      /**  Segement Value 3 of the account for this context.  */  
   SegValue3:string,
      /**  Segement Value 4 of the account for this context.  */  
   SegValue4:string,
      /**  Segement Value 5 of the account for this context.  */  
   SegValue5:string,
      /**  Segement Value 6 of the account for this context.  */  
   SegValue6:string,
      /**  Segement Value 7 of the account for this context.  */  
   SegValue7:string,
      /**  Segement Value 8 of the account for this context.  */  
   SegValue8:string,
      /**  Segement Value 9 of the account for this context.  */  
   SegValue9:string,
      /**  Segement Value 10 of the account for this context.  */  
   SegValue10:string,
      /**  Segement Value 11 of the account for this context.  */  
   SegValue11:string,
      /**  Segement Value 12 of the account for this context.  */  
   SegValue12:string,
      /**  Segement Value 13 of the account for this context.  */  
   SegValue13:string,
      /**  Segement Value 14 of the account for this context.  */  
   SegValue14:string,
      /**  Segement Value 15 of the account for this context.  */  
   SegValue15:string,
      /**  Segement Value 16 of the account for this context.  */  
   SegValue16:string,
      /**  Segement Value 17 of the account for this context.  */  
   SegValue17:string,
      /**  Segement Value 18 of the account for this context.  */  
   SegValue18:string,
      /**  Segement Value 19 of the account for this context.  */  
   SegValue19:string,
      /**  Segement Value 20 of the account for this context.  */  
   SegValue20:string,
      /**  Unique Identifier of the system GL Control Type.  */  
   SysGLControlType:string,
      /**  System generated GL Control Identifier.  */  
   SysGLControlCode:string,
      /**  Global Company identifier.  Used in Multi-Company Journal.  */  
   ExtCompanyID:string,
      /**  Flag to indicate the account in this record is for an external company.  */  
   IsExternalCompany:boolean,
      /**  Fiscal year of the related GLJrnDtl.  */  
   FiscalYear:number,
      /**  JournalCode of the related GLJrnDtl.  */  
   JournalCode:string,
      /**  Journal number of the related GLJrnDtl.  */  
   JournalNum:number,
      /**  JournalLine of the related GLJrnDtl.  */  
   JournalLine:number,
      /**  Transaction date of the transaction.  This is used in order to display the transactions in date order.  */  
   TranDate:string,
      /**   An internal code to identify the table of  the source transaction.
P = PartTran
L = LaborDtl
I = InvcHead
Note: The system does not combine TranSource when creating GLJrnDtl. That is, a specific GLJrnDtl record can only be related to one source.  */  
   TranSource:string,
      /**  LaborHedSeq of the related LaborDtl.  Pertains only to source from LaborDtl (TranSource = "L")  */  
   LaborHedSeq:number,
      /**  LaborDtlSeq of the related LaborDtl. Pertains only to source from LaborDtl (TranSource = "L")  */  
   LaborDtlSeq:number,
      /**  System date of the related PartTran record.  Pertains only to source from PartTran (TranSource = "P")  */  
   SysDate:string,
      /**  System time of the related PartTran record.  Pertains only to source from PartTran (TranSource = "P")  */  
   SysTime:number,
      /**  TranNum of the related PartTran record.  Pertains only to source from PartTran (TranSource = "P")  */  
   TranNum:number,
      /**  InvoiceNum of the related InvcHead record.  Pertains only to source from PartTran (TranSource = "I")  */  
   ARInvoiceNum:number,
      /**  Transaction amount that this transaction posted to the related GlJrnDtl.  */  
   TransAmt:number,
      /**  Invoice Line Number associated with this GL Journal  */  
   InvoiceLine:number,
      /**  The sequence number associated with this GL journal  */  
   SeqNum:number,
      /**  The Internal VendorNum that ties back to the Vendor master file.  This field is not directly maintainable.  */  
   VendorNum:number,
      /**  Vendor's invoice number.  */  
   APInvoiceNum:string,
      /**  Date record was created  */  
   CreateDate:string,
      /**  Fiscal year suffix.  */  
   FiscalYearSuffix:string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   FiscalCalendarID:string,
      /**  Credit Amount.  */  
   CreditAmount:number,
      /**  Debit Amount.  */  
   DebitAmount:number,
      /**  BookCreditAmount  */  
   BookCreditAmount:number,
      /**  Book Debit Amount  */  
   BookDebitAmount:number,
      /**  A unique code that identifies the document currency.  */  
   CurrencyCode:string,
      /**   Indicates if this record contains account data only or reference data such as journal number, amounts, etc.  Valid  values are:
A - account data only
R - reference data  */  
   RecordType:string,
      /**  When a posting rule creates a pair of journal details balancing each other, each detail in the pair should reference the other one. This allows to show correspondence of accounts in reports. Support of reports that allow this being visible is not in the scope of this change.  */  
   CorrAccUID:number,
      /**  this field equals ABTUID which was created during posting  */  
   ABTUID:string,
      /**  Technical identifier.  */  
   RuleUID:number,
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
      /**  IsModifiedByUser  */  
   IsModifiedByUser:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  MovementNum  */  
   MovementNum:number,
      /**  MovementType  */  
   MovementType:string,
      /**  Plant  */  
   Plant:string,
   HeadNum:number,
   BitFlag:number,
   COADescription:string,
   GLAccountGLAcctDisp:string,
   GLAccountAccountDesc:string,
   GLAccountGLShortAcct:string,
   GLBookDescription:string,
   GLBookCurrencyCode:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PRChkDedRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Duplicated from related PRCheck.  */  
   HeadNum:number,
      /**  The deduction Id that this check deduction record is related to.  */  
   DeductionID:string,
      /**  DeductionNum of the related PREmpDed.  */  
   DeductionNum:number,
      /**  Deduction Amount scheduled to be taken.  Calculated based on the values stored in PREmpDed. This amount includes any CarryOverAmt.  */  
   ScheduledAmt:number,
      /**  Indicates if the Deduction Amount is manually calculated.  The system will not calculate the DeductionAmount when ManualCalc = Yes.  */  
   ManualCalc:boolean,
      /**  An internally assigned integer which controls the order in which deductions are processed. It is created/used by the payroll calculation process. It is not the same thing as the PRDeduct.Priority ! Basically it is a sequential # which was generated by processing the deductions in priority order. An exception is for negative deductions, they are set to zero (highest priority). The CalcOrder comes into play when there are insufficient funds to take all the deductions. When this occurs the deductions are decreased in a descending CalcOrder sequence until the check becomes positive.  */  
   CalcOrder:number,
      /**  Deduction Amount taken. Normally this is the same a ScheduledAmt, except in the case where there was insufficient pay to take the deduction. In which case this value could be lower.  */  
   DeductionAmt:number,
      /**  Payroll class ID that employee is currently assigned to.  A mirror image of PREmpMas. It is kept in sync by the PREmpMas write trigger.  */  
   ClassID:string,
      /**  Mirror image of PRCheck.Posted.  */  
   Posted:boolean,
      /**  Encoded value which identifies the employee. Mirror image of PRCheck.EmpLink.  */  
   EmpLink:string,
      /**  mirror image of PRCheck.CheckDate  */  
   CheckDate:string,
      /**  Deduction Year to date amount taken.  */  
   PriorDedYTD:number,
      /**   An internal flag indicating if this is a Void payment transaction.
This is set by the P/R void check program.  */  
   Voided:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  PrintHeadNum  */  
   PrintHeadNum:number,
   EmpID:string,
      /**  First name of employee.  */  
   FirstName:string,
   GroupID:string,
      /**  Last name of employee  */  
   LastName:string,
      /**  This is the employees full name. This is not directly maintainable. It is a concatenation of the FirstName + MiddleInitial + LastName fields. It exists so that it can be used in browses or where ever the complete name in a first, middle, last fashion is required.  */  
   Name:string,
   Reference:string,
   BitFlag:number,
   ClassIDDescription:string,
   DeductionIDDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PRChkDtlRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Duplicated from the related PRCheck.  */  
   HeadNum:number,
      /**  Integer assigned by the system which is used as one of the fields to uniquely identify the PRChkDtl record.  */  
   LineNum:number,
      /**  Date that the employee worked or earned the pay.  */  
   PayrollDate:string,
      /**   Identifies the Pay type of this payment record.  A foreign key to the PayType master table.  This must be a valid PayType where PayType.PremiumFactor <= 1.00.
Ex:( Regular, Holiday, Sick, Vacation . . .)  */  
   PayTypeID:string,
      /**  The employee's base hourly pay rate.  This rate does not include premium or shift differential factors.  It is defaulted from the PREmpMas.PayRate field.  */  
   PayRate:number,
      /**   Hours for non premium time.  Maintainable only if PayTypeID is not blank.
Stored as Hours.Hundreths. For example 3 1/2 hours is stored as 3.5  */  
   BaseHours:number,
      /**  Base pay is the pay amount calculated non-premium hours employees base pay rate.  (see PremiumPay, ShiftPay).  It is calculated as  (BaseHours * PayRate) or set = to the employee salary amount.  It can be overridden in hours entry for salaried employees.  */  
   BasePay:number,
      /**  Identifies the premium Paytype of this payment record (Ex: OT, etc.).  A foreign key to the PayType master table.  This must be a valid PayType where PayType.PremiumFactor > 1.00.  */  
   PremiumPayType:string,
      /**   Hours to be paid at the premium rate.  This is stored as Hours.Hundreths. For example 3 1/2 hours is stored as 3.5
This is disabled and zero if PremiumPaytype = blank.  */  
   PremiumHours:number,
      /**   The amount paid for premium hours not including the premium amount.  Not directly maintainable. (PremiumPayHours* Payrate )
Ex: rate = $10.00,  hours = 3, PremiumBasePay = 30.00. 
The Base Pay portion of the total premium pay amount  is kept separate from the Premium Pay portion for users who wish to track the premium portion of overtime expenses separately in general ledger.  */  
   PremiumBasePay:number,
      /**   Premium pay is the additional amount above the base pay that is being paid as a premium for this pay type. It is not directly maintainable.
For example PayHours = 8, PayRate = 10.00 and PremiumFactor = 1.5,  BasePay would be 80.00 and PremiumPay would be 40.00.
The Base Pay is kept separate from the Premium Pay for users who wish to track the premium portion of the pay separately in general ledger.
PremiumPayHours * (Payrate * (PremiumFactor - 1.00)).  */  
   PremiumPay:number,
      /**   Defaults from the EmpBasic.Shift when entered through payroll hours entry, or was from LaborHed.Shift is the case the record was created from labor transfer process.
Note:  When shift is changed in check entry the pay amounts may need to be recalculated if shift pay is active.  */  
   Shift:number,
      /**   Shift pay is the amount paid due to shift differential.
(BaseHours * ShiftDifferential)  + 
PremiumHours * (ShiftDifferential * PremiumFactor).
PremiumFactor  is used only if PayType.IncludeShift = Yes. 
Note: Shift differential is either an additional percentage of payrate or an additional flat amount.  
For example PayHours = 8, PayRate = 10.00 and Shift differential is an extra 1.00 per hour. ShiftPay would be $8.00.
This is refreshed when changes are made to Shift, PayRate, or PayHours or PremiumHours or PayType.  */  
   ShiftPay:number,
      /**  Payroll class ID that employee is currently assigned to. A mirror image of PREmpMas. It is kept in sync by the PREmpMas write trigger.  */  
   ClassID:string,
      /**  Mirror image of PRCheck.Posted.  */  
   Posted:boolean,
      /**  Encoded value which identifies the employee. Mirror image of PRCheck.EmpLink.  */  
   EmpLink:string,
      /**  mirror image of PRCheck.CheckDate.  This is not updated until the checks are posted.  */  
   CheckDate:string,
      /**  A internally used flag which indicates that this record was generated from a LaborHed record.  */  
   FromLabor:boolean,
      /**   An internal flag indicating if this is a Void payment transaction.
This is set by the P/R void check program.  */  
   Voided:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  PrintHeadNum  */  
   PrintHeadNum:number,
      /**  IsOutdatedLabor  */  
   IsOutdatedLabor:boolean,
   DiffMethod:string,
   DiffMethodDesc:string,
   DiffQualifier:string,
   DiffQualifierDesc:string,
   DiffRate:number,
   EmpID:string,
      /**  First name of employee.  */  
   FirstName:string,
   GroupID:string,
      /**  Last name of employee  */  
   LastName:string,
      /**  This is the employees full name. This is not directly maintainable. It is a concatenation of the FirstName + MiddleInitial + LastName fields. It exists so that it can be used in browses or where ever the complete name in a first, middle, last fashion is required.  */  
   Name:string,
   ShiftTimesDesc:string,
   TotalHours:number,
   TotalPay:number,
      /**  Used in VoidPRCheck - Date the check was voided.  */  
   VoidedDate:string,
   AmountType:string,
      /**   DateRange specifies the range between record is created depending of payroll frequency, the possible values are:
"Outdated", labor processed before period begins
"In Pay Range", labor processed between perido begin and period ending
"Outrunning". labor processed after period ending  */  
   DateRange:string,
   BitFlag:number,
   ClassIDDescription:string,
   PayTypeIDDescription:string,
   PremiumPayTypeIDDescription:string,
   ShiftDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PRChkTaxRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Duplicated from related PRCheck.  */  
   HeadNum:number,
      /**  Tax Table ID  */  
   TaxTblID:string,
      /**  Identifies the type of tax table.  Valid values are "FIT" - Federal, "SIT" - State, "FUTA" - Federal Unemployment, "SUTA" - State Unemployment,  "SS" - Social Security, "MED" - Medicare, "CITY" - Local, "CNTY" - County, "OTHR" - Other.  */  
   TaxType:string,
      /**  Payroll class ID that employee is currently assigned to. A mirror image of PREmpMas. It is kept in sync by the PREmpMas write trigger.  */  
   ClassID:string,
      /**  Mirror image of PRCheck.Posted.  */  
   Posted:boolean,
      /**  Encoded value which identifies the employee. Mirror image of PRCheck.EmpLink.  */  
   EmpLink:string,
      /**  mirror image of PRCheck.CheckDate  */  
   CheckDate:string,
      /**  Amount withheld on this check for a specific tax.  */  
   TaxAmt:number,
      /**  The Year to Date tax withheld  prior to this check. Current YTD is PriorTaxYTD + TaxAmt.  */  
   PriorTaxYTD:number,
      /**  Taxable hours on this check for the tax jurisdiction.  This is the BaseHours and PremiumHours if the PayType is not exempt from the tax jurisdiction.  */  
   TaxableHours:number,
      /**  The taxable amount of supplemental pay for this check  for the tax jurisdiction.  */  
   SupTaxableAmt:number,
      /**  The hours accumulated from supplemental pay records.  This is used in tax calc when tax basis is % of hours.  */  
   SupTaxableHours:number,
      /**  Pay check amount that is considered as taxable for this tax jurisdiction. This is calculated by the system as part of the payroll calculate routine.  */  
   TaxableAmt:number,
      /**  The Year to Date taxable amount prior to this check. Current YTD is PriorTaxableYTD + TaxableAmt.  */  
   PriorTaxableYTD:number,
      /**  Indicates if this tax record for the check is taxable as of the check date. Of course, if a tax was first taken it would have been taxable. This flag is used so that if after the check is posted it is discovered that it was taken in error the user can set this to NO which would reduce the year to date taxable amount from this date forward. This situation should not be a common occurrence; however it's more likely when employees' have multiple taxes that are deactivated/activated during the same year. It does not change the Tax withheld only taxable.  This flag is needed so that the "Recalculate" taxable amounts would work correctly.  */  
   Active:boolean,
      /**  Indicates if the Tax Amount is manually calculated.  The system will not calculate the TaxAmount when ManualCalc = Yes.  */  
   ManualCalc:boolean,
      /**   An internal flag indicating if this is a Void payment transaction.
This is set by the P/R void check program.  */  
   Voided:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  PrintHeadNum  */  
   PrintHeadNum:number,
   CreditAmount:number,
   EmpID:string,
   FilingStatus:string,
      /**  First name of employee.  */  
   FirstName:string,
   GroupID:string,
      /**  Last name of employee  */  
   LastName:string,
      /**  This is the employees full name. This is not directly maintainable. It is a concatenation of the FirstName + MiddleInitial + LastName fields. It exists so that it can be used in browses or where ever the complete name in a first, middle, last fashion is required.  */  
   Name:string,
   TaxDesc:string,
   BitFlag:number,
   ClassIDDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PayrollCheckEntryTableset{
   PRCheck:Erp_Tablesets_PRCheckRow[],
   PRChkDed:Erp_Tablesets_PRChkDedRow[],
   PRChkDtl:Erp_Tablesets_PRChkDtlRow[],
   PRChkTax:Erp_Tablesets_PRChkTaxRow[],
   PRCheckTGLC:Erp_Tablesets_PRCheckTGLCRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtPayrollCheckEntryTableset{
   PRCheck:Erp_Tablesets_PRCheckRow[],
   PRChkDed:Erp_Tablesets_PRChkDedRow[],
   PRChkDtl:Erp_Tablesets_PRChkDtlRow[],
   PRChkTax:Erp_Tablesets_PRChkTaxRow[],
   PRCheckTGLC:Erp_Tablesets_PRCheckTGLCRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param groupID
   */  
export interface GeneratePayChecksVerification_input{
      /**  The group id to get the configuration options  */  
   groupID:string,
}

export interface GeneratePayChecksVerification_output{
parameters : {
      /**  output parameters  */  
   VerificationMsg:string,
}
}

   /** Required : 
      @param GroupID
      @param HeadNum
      @param ds
   */  
export interface GeneratePayChecks_input{
      /**  The group id to generate paychecks for  */  
   GroupID:string,
      /**  The current PRCheck.HeadNum record.  Is used to
            rebuild the dataset so the data is current. Not required.  If the value
            is 0, a refreshed dataset won't be passed back.  */  
   HeadNum:number,
   ds:Erp_Tablesets_PayrollCheckEntryTableset[],
}

export interface GeneratePayChecks_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PayrollCheckEntryTableset[],
   OutNoCheckMessage:string,
   OutNotApprovedLaborMessage:string,
}
}

   /** Required : 
      @param headNum
   */  
export interface GetByID_input{
   headNum:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_PayrollCheckEntryTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_PayrollCheckEntryTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_PayrollCheckEntryTableset[],
}

   /** Required : 
      @param tableName
      @param fieldName
   */  
export interface GetCodeDescList_input{
   tableName:string,
   fieldName:string,
}

export interface GetCodeDescList_output{
   returnObj:string,
}

   /** Required : 
      @param EmpID
      @param CheckNum
   */  
export interface GetGLEntries_input{
      /**  Employee ID  */  
   EmpID:string,
      /**  Check Number  */  
   CheckNum:number,
}

export interface GetGLEntries_output{
   returnObj:Erp_Tablesets_PayrollCheckEntryTableset[],
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
   returnObj:Erp_Tablesets_PRCheckListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param GroupID
      @param ds
   */  
export interface GetNewPRCheckForGroup_input{
      /**  The group id to add the payroll check to  */  
   GroupID:string,
   ds:Erp_Tablesets_PayrollCheckEntryTableset[],
}

export interface GetNewPRCheckForGroup_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PayrollCheckEntryTableset[],
}
}

   /** Required : 
      @param ds
      @param headNum
      @param tgLCTranNum
   */  
export interface GetNewPRCheckTGLC_input{
   ds:Erp_Tablesets_PayrollCheckEntryTableset[],
   headNum:number,
   tgLCTranNum:number,
}

export interface GetNewPRCheckTGLC_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PayrollCheckEntryTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewPRCheck_input{
   ds:Erp_Tablesets_PayrollCheckEntryTableset[],
}

export interface GetNewPRCheck_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PayrollCheckEntryTableset[],
}
}

   /** Required : 
      @param ds
      @param headNum
      @param deductionID
   */  
export interface GetNewPRChkDed_input{
   ds:Erp_Tablesets_PayrollCheckEntryTableset[],
   headNum:number,
   deductionID:string,
}

export interface GetNewPRChkDed_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PayrollCheckEntryTableset[],
}
}

   /** Required : 
      @param ds
      @param headNum
   */  
export interface GetNewPRChkDtl_input{
   ds:Erp_Tablesets_PayrollCheckEntryTableset[],
   headNum:number,
}

export interface GetNewPRChkDtl_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PayrollCheckEntryTableset[],
}
}

   /** Required : 
      @param ds
      @param headNum
   */  
export interface GetNewPRChkTax_input{
   ds:Erp_Tablesets_PayrollCheckEntryTableset[],
   headNum:number,
}

export interface GetNewPRChkTax_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PayrollCheckEntryTableset[],
}
}

   /** Required : 
      @param empID
      @param whereClausePRCheck
      @param whereClausePRChkDtl
      @param whereClausePRChkDed
      @param whereClausePRChkTax
      @param whereClausePRCheckTGLC
      @param pageSize
      @param absolutePage
   */  
export interface GetRowsByEmpID_input{
      /**  Employee ID  */  
   empID:string,
      /**  WhereClause Payroll Check  */  
   whereClausePRCheck:string,
      /**  WhereClause Payroll Check Details  */  
   whereClausePRChkDtl:string,
      /**  WhereClause Payroll Check Deductions  */  
   whereClausePRChkDed:string,
      /**  WhereClause Payroll Check Tax  */  
   whereClausePRChkTax:string,
      /**  WhereClause Payroll Check TranGLC  */  
   whereClausePRCheckTGLC:string,
      /**  PageSize  */  
   pageSize:number,
      /**  Absolute Page  */  
   absolutePage:number,
}

export interface GetRowsByEmpID_output{
   returnObj:Erp_Tablesets_PayrollCheckEntryTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ipHeadNum
      @param ipWhereClausePRCheck
      @param ipWhereClausePRChkDtl
      @param ipWhereClausePRChkDed
      @param ipWhereClausePRChkTax
      @param ipWhereClausePRCheckTGLC
      @param ipPageSize
      @param ipAbsolutePage
   */  
export interface GetRowsFromAutoBankRec_input{
      /**  Head No  */  
   ipHeadNum:string,
      /**  WhereClause Payroll Check  */  
   ipWhereClausePRCheck:string,
      /**  WhereClause Payroll Check Details  */  
   ipWhereClausePRChkDtl:string,
      /**  WhereClause Payroll Check Deductions  */  
   ipWhereClausePRChkDed:string,
      /**  WhereClause Payroll Check Tax  */  
   ipWhereClausePRChkTax:string,
      /**  WhereClause Payroll Check TranGLC  */  
   ipWhereClausePRCheckTGLC:string,
      /**  PageSize  */  
   ipPageSize:number,
      /**  Absolute Page  */  
   ipAbsolutePage:number,
}

export interface GetRowsFromAutoBankRec_output{
   returnObj:Erp_Tablesets_PayrollCheckEntryTableset[],
parameters : {
      /**  output parameters  */  
   opMorePages:boolean,
}
}

   /** Required : 
      @param whereClausePRCheck
      @param whereClausePRChkDed
      @param whereClausePRChkDtl
      @param whereClausePRChkTax
      @param whereClausePRCheckTGLC
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClausePRCheck:string,
   whereClausePRChkDed:string,
   whereClausePRChkDtl:string,
   whereClausePRChkTax:string,
   whereClausePRCheckTGLC:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_PayrollCheckEntryTableset[],
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
      @param ds
   */  
export interface RecalcPayRate_input{
   ds:Erp_Tablesets_PayrollCheckEntryTableset[],
}

export interface RecalcPayRate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PayrollCheckEntryTableset[],
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtPayrollCheckEntryTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtPayrollCheckEntryTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface UpdatePRChkDed_input{
   ds:Erp_Tablesets_PayrollCheckEntryTableset[],
}

export interface UpdatePRChkDed_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PayrollCheckEntryTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface UpdatePRChkTax_input{
   ds:Erp_Tablesets_PayrollCheckEntryTableset[],
}

export interface UpdatePRChkTax_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PayrollCheckEntryTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_PayrollCheckEntryTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PayrollCheckEntryTableset[],
}
}

   /** Required : 
      @param IP_ServerFileName
   */  
export interface getClientFileName_input{
   IP_ServerFileName:string,
}

export interface getClientFileName_output{
   returnObj:string,
}

