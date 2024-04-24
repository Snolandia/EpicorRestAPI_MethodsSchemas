import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.PkgControlIDSvc
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDSvc/$metadata", {
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
   Description: Get PkgControlIDs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PkgControlIDs
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PkgControlHeaderRow
   */  
export function get_PkgControlIDs(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PkgControlHeaderRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDSvc/PkgControlIDs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PkgControlHeaderRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PkgControlIDs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PkgControlHeaderRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PkgControlHeaderRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PkgControlIDs(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDSvc/PkgControlIDs", {
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
   Summary: Calls GetByID to retrieve the PkgControlID item
   Description: Calls GetByID to retrieve the PkgControlID item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PkgControlID
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PCID Desc: PCID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PkgControlHeaderRow
   */  
export function get_PkgControlIDs_Company_PCID(Company:string, PCID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PkgControlHeaderRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDSvc/PkgControlIDs(" + Company + "," + PCID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PkgControlHeaderRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PkgControlID for the service
   Description: Calls UpdateExt to update PkgControlID. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PkgControlID
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PCID Desc: PCID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PkgControlHeaderRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PkgControlIDs_Company_PCID(Company:string, PCID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDSvc/PkgControlIDs(" + Company + "," + PCID + ")", {
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
   Summary: Call UpdateExt to delete PkgControlID item
   Description: Call UpdateExt to delete PkgControlID item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PkgControlID
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PCID Desc: PCID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PkgControlIDs_Company_PCID(Company:string, PCID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDSvc/PkgControlIDs(" + Company + "," + PCID + ")", {
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
   Description: Get PkgControlCustPartNums items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PkgControlCustPartNums1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PCID Desc: PCID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PkgControlCustPartNumRow
   */  
export function get_PkgControlIDs_Company_PCID_PkgControlCustPartNums(Company:string, PCID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PkgControlCustPartNumRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDSvc/PkgControlIDs(" + Company + "," + PCID + ")/PkgControlCustPartNums", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PkgControlCustPartNumRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PkgControlCustPartNum item
   Description: Calls GetByID to retrieve the PkgControlCustPartNum item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PkgControlCustPartNum1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PCID Desc: PCID   Required: True   Allow empty value : True
      @param PCIDCustPartSeq Desc: PCIDCustPartSeq   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PkgControlCustPartNumRow
   */  
export function get_PkgControlIDs_Company_PCID_PkgControlCustPartNums_Company_PCID_PCIDCustPartSeq(Company:string, PCID:string, PCIDCustPartSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PkgControlCustPartNumRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDSvc/PkgControlIDs(" + Company + "," + PCID + ")/PkgControlCustPartNums(" + Company + "," + PCID + "," + PCIDCustPartSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PkgControlCustPartNumRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get PCLabelValues items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PCLabelValues1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PCID Desc: PCID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PCLabelValuesRow
   */  
export function get_PkgControlIDs_Company_PCID_PCLabelValues(Company:string, PCID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PCLabelValuesRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDSvc/PkgControlIDs(" + Company + "," + PCID + ")/PCLabelValues", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PCLabelValuesRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PCLabelValue item
   Description: Calls GetByID to retrieve the PCLabelValue item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PCLabelValue1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PCID Desc: PCID   Required: True   Allow empty value : True
      @param LabelSeq Desc: LabelSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PCLabelValuesRow
   */  
export function get_PkgControlIDs_Company_PCID_PCLabelValues_Company_PCID_LabelSeq(Company:string, PCID:string, LabelSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PCLabelValuesRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDSvc/PkgControlIDs(" + Company + "," + PCID + ")/PCLabelValues(" + Company + "," + PCID + "," + LabelSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PCLabelValuesRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get PkgControlItems items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PkgControlItems1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PCID Desc: PCID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PkgControlItemRow
   */  
export function get_PkgControlIDs_Company_PCID_PkgControlItems(Company:string, PCID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PkgControlItemRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDSvc/PkgControlIDs(" + Company + "," + PCID + ")/PkgControlItems", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PkgControlItemRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PkgControlItem item
   Description: Calls GetByID to retrieve the PkgControlItem item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PkgControlItem1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PCID Desc: PCID   Required: True   Allow empty value : True
      @param PCIDItemSeq Desc: PCIDItemSeq   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PkgControlItemRow
   */  
export function get_PkgControlIDs_Company_PCID_PkgControlItems_Company_PCID_PCIDItemSeq(Company:string, PCID:string, PCIDItemSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PkgControlItemRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDSvc/PkgControlIDs(" + Company + "," + PCID + ")/PkgControlItems(" + Company + "," + PCID + "," + PCIDItemSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PkgControlItemRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get PkgControlCustPartNums items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PkgControlCustPartNums
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PkgControlCustPartNumRow
   */  
export function get_PkgControlCustPartNums(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PkgControlCustPartNumRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDSvc/PkgControlCustPartNums", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PkgControlCustPartNumRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PkgControlCustPartNums
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PkgControlCustPartNumRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PkgControlCustPartNumRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PkgControlCustPartNums(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDSvc/PkgControlCustPartNums", {
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
   Summary: Calls GetByID to retrieve the PkgControlCustPartNum item
   Description: Calls GetByID to retrieve the PkgControlCustPartNum item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PkgControlCustPartNum
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PCID Desc: PCID   Required: True   Allow empty value : True
      @param PCIDCustPartSeq Desc: PCIDCustPartSeq   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PkgControlCustPartNumRow
   */  
export function get_PkgControlCustPartNums_Company_PCID_PCIDCustPartSeq(Company:string, PCID:string, PCIDCustPartSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PkgControlCustPartNumRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDSvc/PkgControlCustPartNums(" + Company + "," + PCID + "," + PCIDCustPartSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PkgControlCustPartNumRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PkgControlCustPartNum for the service
   Description: Calls UpdateExt to update PkgControlCustPartNum. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PkgControlCustPartNum
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PCID Desc: PCID   Required: True   Allow empty value : True
      @param PCIDCustPartSeq Desc: PCIDCustPartSeq   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PkgControlCustPartNumRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PkgControlCustPartNums_Company_PCID_PCIDCustPartSeq(Company:string, PCID:string, PCIDCustPartSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDSvc/PkgControlCustPartNums(" + Company + "," + PCID + "," + PCIDCustPartSeq + ")", {
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
   Summary: Call UpdateExt to delete PkgControlCustPartNum item
   Description: Call UpdateExt to delete PkgControlCustPartNum item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PkgControlCustPartNum
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PCID Desc: PCID   Required: True   Allow empty value : True
      @param PCIDCustPartSeq Desc: PCIDCustPartSeq   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PkgControlCustPartNums_Company_PCID_PCIDCustPartSeq(Company:string, PCID:string, PCIDCustPartSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDSvc/PkgControlCustPartNums(" + Company + "," + PCID + "," + PCIDCustPartSeq + ")", {
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
   Description: Get PCLabelValues items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PCLabelValues
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PCLabelValuesRow
   */  
export function get_PCLabelValues(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PCLabelValuesRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDSvc/PCLabelValues", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PCLabelValuesRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PCLabelValues
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PCLabelValuesRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PCLabelValuesRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PCLabelValues(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDSvc/PCLabelValues", {
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
   Summary: Calls GetByID to retrieve the PCLabelValue item
   Description: Calls GetByID to retrieve the PCLabelValue item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PCLabelValue
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PCID Desc: PCID   Required: True   Allow empty value : True
      @param LabelSeq Desc: LabelSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PCLabelValuesRow
   */  
export function get_PCLabelValues_Company_PCID_LabelSeq(Company:string, PCID:string, LabelSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PCLabelValuesRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDSvc/PCLabelValues(" + Company + "," + PCID + "," + LabelSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PCLabelValuesRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PCLabelValue for the service
   Description: Calls UpdateExt to update PCLabelValue. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PCLabelValue
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PCID Desc: PCID   Required: True   Allow empty value : True
      @param LabelSeq Desc: LabelSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PCLabelValuesRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PCLabelValues_Company_PCID_LabelSeq(Company:string, PCID:string, LabelSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDSvc/PCLabelValues(" + Company + "," + PCID + "," + LabelSeq + ")", {
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
   Summary: Call UpdateExt to delete PCLabelValue item
   Description: Call UpdateExt to delete PCLabelValue item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PCLabelValue
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PCID Desc: PCID   Required: True   Allow empty value : True
      @param LabelSeq Desc: LabelSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PCLabelValues_Company_PCID_LabelSeq(Company:string, PCID:string, LabelSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDSvc/PCLabelValues(" + Company + "," + PCID + "," + LabelSeq + ")", {
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
   Description: Get PkgControlItems items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PkgControlItems
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PkgControlItemRow
   */  
export function get_PkgControlItems(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PkgControlItemRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDSvc/PkgControlItems", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PkgControlItemRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PkgControlItems
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PkgControlItemRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PkgControlItemRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PkgControlItems(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDSvc/PkgControlItems", {
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
   Summary: Calls GetByID to retrieve the PkgControlItem item
   Description: Calls GetByID to retrieve the PkgControlItem item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PkgControlItem
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PCID Desc: PCID   Required: True   Allow empty value : True
      @param PCIDItemSeq Desc: PCIDItemSeq   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PkgControlItemRow
   */  
export function get_PkgControlItems_Company_PCID_PCIDItemSeq(Company:string, PCID:string, PCIDItemSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PkgControlItemRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDSvc/PkgControlItems(" + Company + "," + PCID + "," + PCIDItemSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PkgControlItemRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PkgControlItem for the service
   Description: Calls UpdateExt to update PkgControlItem. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PkgControlItem
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PCID Desc: PCID   Required: True   Allow empty value : True
      @param PCIDItemSeq Desc: PCIDItemSeq   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PkgControlItemRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PkgControlItems_Company_PCID_PCIDItemSeq(Company:string, PCID:string, PCIDItemSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDSvc/PkgControlItems(" + Company + "," + PCID + "," + PCIDItemSeq + ")", {
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
   Summary: Call UpdateExt to delete PkgControlItem item
   Description: Call UpdateExt to delete PkgControlItem item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PkgControlItem
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PCID Desc: PCID   Required: True   Allow empty value : True
      @param PCIDItemSeq Desc: PCIDItemSeq   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PkgControlItems_Company_PCID_PCIDItemSeq(Company:string, PCID:string, PCIDItemSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDSvc/PkgControlItems(" + Company + "," + PCID + "," + PCIDItemSeq + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PkgControlHeaderListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PkgControlHeaderListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PkgControlHeaderListRow)
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
export function get_GetRows(whereClausePkgControlHeader:string, whereClausePkgControlCustPartNum:string, whereClausePCLabelValues:string, whereClausePkgControlItem:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClausePkgControlHeader!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePkgControlHeader=" + whereClausePkgControlHeader
   }
   if(typeof whereClausePkgControlCustPartNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePkgControlCustPartNum=" + whereClausePkgControlCustPartNum
   }
   if(typeof whereClausePCLabelValues!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePCLabelValues=" + whereClausePCLabelValues
   }
   if(typeof whereClausePkgControlItem!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePkgControlItem=" + whereClausePkgControlItem
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDSvc/GetRows" + params, {
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
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(pcID:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof pcID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "pcID=" + pcID
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDSvc/GetList" + params, {
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
   Summary: Invoke method GetListCoreStageHX
   Description: Get list of PCIDs from Core, Stage and History tables.
   OperationID: GetListCoreStageHX
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListCoreStageHX_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListCoreStageHX_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetListCoreStageHX(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDSvc/GetListCoreStageHX", {
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
   Summary: Invoke method GetPCIDList
   Description: Purpose:  To find PCID's that are shipped on a given shipment
   OperationID: GetPCIDList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPCIDList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPCIDList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPCIDList(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDSvc/GetPCIDList", {
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
   Summary: Invoke method PCIDExists
   Description: Purpose:  Test if a given PCID already exists in the PkgControlHeader table.
   OperationID: PCIDExists
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PCIDExists_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PCIDExists_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PCIDExists(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDSvc/PCIDExists", {
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
   Summary: Invoke method WarehseEnforcePkgControlRulesExists
   Description: This method is udes to verify if a Warehouse with EnforcePkgControlRules exists
   OperationID: WarehseEnforcePkgControlRulesExists
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/WarehseEnforcePkgControlRulesExists_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/WarehseEnforcePkgControlRulesExists_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_WarehseEnforcePkgControlRulesExists(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDSvc/WarehseEnforcePkgControlRulesExists", {
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
   Summary: Invoke method WhseBinExists
   Description: This method is udes to verify if a WhseBin exists
   OperationID: WhseBinExists
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/WhseBinExists_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/WhseBinExists_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_WhseBinExists(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDSvc/WhseBinExists", {
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
   Summary: Invoke method OnChangePCID
   Description: Call this method when the value of Epicor.Mfg.BO.PkgControlIDDataSet.PCID changes.
   OperationID: OnChangePCID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangePCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangePCID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDSvc/OnChangePCID", {
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
   Summary: Invoke method CommitPCIDTransfer
   Description: This method will commit the inventory transfer.
   OperationID: CommitPCIDTransfer
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CommitPCIDTransfer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CommitPCIDTransfer_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CommitPCIDTransfer(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDSvc/CommitPCIDTransfer", {
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
   Summary: Invoke method PasswordConfigured
   Description: this method returns if the supervisor password is configured
   OperationID: PasswordConfigured
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/PasswordConfigured_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PasswordConfigured(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDSvc/PasswordConfigured", {
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
   Summary: Invoke method ConfirmSupervisorPassword
   Description: This method is used to confirm if the User/Supervisor Password provided is correct.
This is called from PackageControlLib.
   OperationID: ConfirmSupervisorPassword
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ConfirmSupervisorPassword_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ConfirmSupervisorPassword_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ConfirmSupervisorPassword(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDSvc/ConfirmSupervisorPassword", {
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
   Summary: Invoke method GetNewPkgControlHeader
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPkgControlHeader
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPkgControlHeader_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPkgControlHeader_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPkgControlHeader(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDSvc/GetNewPkgControlHeader", {
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
   Summary: Invoke method GetNewPkgControlCustPartNum
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPkgControlCustPartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPkgControlCustPartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPkgControlCustPartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPkgControlCustPartNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDSvc/GetNewPkgControlCustPartNum", {
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
   Summary: Invoke method GetNewPkgControlItem
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPkgControlItem
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPkgControlItem_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPkgControlItem_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPkgControlItem(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDSvc/GetNewPkgControlItem", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PCLabelValuesRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PCLabelValuesRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PkgControlCustPartNumRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PkgControlCustPartNumRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PkgControlHeaderListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PkgControlHeaderListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PkgControlHeaderRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PkgControlHeaderRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PkgControlItemRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PkgControlItemRow[],
}

export interface Erp_Tablesets_PCLabelValuesRow{
   "Company":string,
   "LabelSeq":number,
   "LabelValues":string,
   "PCID":string,
   "ValueField":string,
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PkgControlCustPartNumRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Package Control Identification Number.  */  
   "PCID":string,
      /**  PCID Customer Part Sequence.  */  
   "PCIDCustPartSeq":number,
      /**  Used for MixedMaster parent PCIDs.  Customer Part Number associated to the MixedMaster parent PCID.  */  
   "CustPartNum":string,
      /**  Used for MixedMaster parent PCIDs. Number of parts per parent PCID for the Customer Part Number associated to the MixedMaster parent PCID.  */  
   "CustQtyPerContainer":number,
      /**  Used for MixedMaster parent PCIDs.  Number of PCIDs for the Customer Part Number associated to the MixedMaster parent PCID.  */  
   "CustNumContainers":number,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PkgControlHeaderListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Package Control Identification Number  */  
   "PCID":string,
      /**  Site where the PCID is currently located.  */  
   "Plant":string,
      /**  Warehouse where the PCID is currently located.  */  
   "WarehouseCode":string,
      /**  Warehouse Bin where the PCID is currently located.  */  
   "BinNum":string,
      /**  Warehouse where the PCID return stock needs to be returned to.  */  
   "ReturnToWarehouseCode":string,
      /**  Warehouse Bin where the PCID return stock needs to be returned to.  */  
   "ReturnToBinNum":string,
      /**  PCID current status.  */  
   "PkgControlStatus":string,
      /**  PCID prior status.  */  
   "PkgControlPriorStatus":string,
      /**  Label Print Control status.  */  
   "LabelPrintControlStatus":string,
      /**  Label Print Control prior status.  */  
   "LabelPrintControlPriorStatus":string,
      /**  If false then PCID is a single-level PCID that cannot be associated with a Parent.  */  
   "AllowParentPCID":boolean,
      /**  If false then PCID must contain only one PartNum.  */  
   "AllowMixedParts":boolean,
      /**  If false then PCID must contain only one LotNum for each Part on the PCID.  */  
   "AllowMixedLots":boolean,
      /**  If false then PCID must contain only one UOM per Part on the PCID.  */  
   "AllowMixedUOMs":boolean,
      /**  If false then PCID is restricted to containing single-level child PCIDs only and those child PCIDs must contain the same PartNum, Part UOM, or Part Quantity per child PCID.  This is referred to as a Master PCID, otherwise it would be referred to as a MixedMaster PCID.  */  
   "AllowMixedChildPCIDs":boolean,
      /**  If false then PCID must contain only one Serial Number per PCID.  */  
   "AllowMultipleSerialNumPerPCID":boolean,
      /**  If false then the standard PCID printing logic is used. If true then the Label Print Control logic and rules will apply and be enforced.  */  
   "LabelPrintControlled":boolean,
      /**  If false then the number of PCID label prints will not be tracked.  */  
   "LabelPrintCounter":boolean,
      /**  If false then PkgControlHeader and PkgControlItem cannot be voided or deleted.  */  
   "AllowVoids":boolean,
      /**  If false then PkgControlHeader and PkgControlItem cannot be deleted.  */  
   "AllowDeletes":boolean,
      /**  If true then PkgControlHeader and PkgControlItem will be written to history tables and removed from the maintenance tables on void, delete or close/collapse.  */  
   "ArchivePCIDHistory":boolean,
      /**  Unique packaging code assigned by the user.  */  
   "PkgCode":string,
      /**  User defined code which uniquely identifies the UOM for length, width, and height.  */  
   "LWHDimensionUOM":string,
      /**  Length dimension.  */  
   "Length":number,
      /**  Width dimension.  */  
   "Width":number,
      /**  Height dimension.  */  
   "Height":number,
      /**  User defined code which uniquely identifies the UOM for volume.  */  
   "VolumeUOM":string,
      /**  Volume.  */  
   "Volume":number,
      /**  User defined code which uniquely identifies the UOM for weight.  */  
   "WeightUOM":string,
      /**  Maximum Weight.  */  
   "MaximumWeight":number,
      /**  Calculated Weight.  */  
   "CalculatedWeight":number,
      /**  The total weight of the parts and the container combined.  */  
   "TotalWeight":number,
      /**  Maximum number of PCIDs allowed if vertically stacked.  */  
   "MaximumStack":number,
      /**  Position Sequence within a parent PCID.  */  
   "PositionSeq":number,
      /**  Trailer ID.  */  
   "TrailerID":string,
      /**  Bond or Security Seal ID.  */  
   "SecuritySealID":string,
      /**  Raw PCID as scanned or generated.  */  
   "RawPCIDLicensePlate":string,
      /**  GS1-128 as generated by the Legal Number process.  GS1-128 supersedes the former UCC/EAN128 standards.  */  
   "GS1128":string,
      /**  For a static PCID, each time the PCID is collapsed this counter is incremented, and the collapse counter is stamped on any PartTran records generated throughout the life of the PCID.  */  
   "PkgControlCollapseCounter":number,
      /**  System date and time when the row was created.  */  
   "CreatedDate":string,
      /**  The user ID that created this row.  */  
   "CreatedBy":string,
      /**  System date and time when the row was last updated.  */  
   "UpdatedDate":string,
      /**  The user ID that last updated this row.  */  
   "UpdatedBy":string,
      /**  Last PCID Scanned.  */  
   "LastPCIDScanned":string,
      /**  Number of next level down child PCIDs associated to this PCID.  */  
   "NumberOfPCIDs":number,
      /**  Flag used to fire the auto print rule that will print the labels.  */  
   "AutoPrint":boolean,
      /**  System date and time when the row was created.  */  
   "LPCCreatedDate":string,
      /**  The user ID that created this record.  */  
   "LPCCreatedBy":string,
      /**  Printer ID that printed the label.  */  
   "LPCPrinterID":string,
      /**  User that printed the label.  */  
   "LPCPrintedBy":string,
      /**  Label feature. Displays what transaction the label was printed from.  */  
   "LPCPrintedFromTx":string,
      /**  Ad Hoc feature. Displays what transaction type the label was printed from.  */  
   "LPCPrintedFromTxType":string,
      /**  The job for which the label was printed.  */  
   "LPCJobNum":string,
      /**  The operation sequence for which the label was printed.  */  
   "LPCOprSeq":number,
      /**  The assembly sequence for which the label was printed.  */  
   "LPCAssemblySeq":number,
      /**  Shift that the label was created on or shift entered in Ad Hoc print program.  */  
   "LPCShift":number,
      /**  Operator who created the label if printed from MES, Labor Reporting employee if printed from Ad Hoc Manufacturing Backup, or blank otherwise.  */  
   "LPCOperatorEmpID":string,
      /**  Original Source PCID for repack. This field will be populated with the source container PCID when assigning a repack label.  */  
   "OriginalSourcePCID":string,
      /**  This field will be populated with the new PCID that replaced this PCID when using the overlay feature.  */  
   "OverlaidByPCID":string,
      /**  Set to True when PCID has been overlaid using the overlay feature.  */  
   "Overlaid":boolean,
      /**  Partial Container – set to true when the container is created from the Ad Hoc – Partial program.  */  
   "ContainerPartial":boolean,
      /**  If true the container was repacked.  */  
   "ContainerRepacked":boolean,
      /**  If true the container used is a returnable container.  */  
   "ContainerReturnable":boolean,
      /**  Our Vendor ID for the Customer being Shipped To.  */  
   "OurSupplierCode":string,
      /**  Site Name.  */  
   "PlantName":string,
      /**  Site Address line 1.  */  
   "PlantAddress1":string,
      /**  Site Address line 2.  */  
   "PlantAddress2":string,
      /**  Site Address line 3.  */  
   "PlantAddress3":string,
      /**  Site City.  */  
   "PlantCity":string,
      /**  Site State.  */  
   "PlantState":string,
      /**  Site Zip.  */  
   "PlantZip":string,
      /**  Site Country Number.  */  
   "PlantCountryNum":number,
      /**  Site Country Description.  */  
   "PlantCountryDesc":string,
      /**  Site Phone.  */  
   "PlantPhone":string,
      /**  Pack Number if applicable.  */  
   "PackNum":number,
      /**  Ship To Customer Container Part Number.  */  
   "CustContainerPartNum":string,
      /**  EDI Ship To Number populated with the final destination if shipping to an Intermediate Consignee, otherwise an actual ShipToNum.  */  
   "EDIShipToNum":string,
      /**  Ship To Number.  */  
   "ShipToNum":string,
      /**  Name of the Ship To that the PCID is going to.  */  
   "ShipToName":string,
      /**  Address line 1 of the Ship To that the PCID is going to.  */  
   "ShipToAddress1":string,
      /**  Address line 2 of the Ship To that the PCID is going to.  */  
   "ShipToAddress2":string,
      /**  Address line 3 of the Ship To that the PCID is going to.  */  
   "ShipToAddress3":string,
      /**  City of the Ship To that the PCID is going to.  */  
   "ShipToCity":string,
      /**  State of the Ship To that the PCID is going to.  */  
   "ShipToState":string,
      /**  Zip of the Ship To that the PCID is going to.  */  
   "ShipToZip":string,
      /**  Country number of the Ship To that the PCID is going to.  */  
   "ShipToCountryNum":number,
      /**  Country of the Ship To that the PCID is going to.  */  
   "ShipToCountryDesc":string,
      /**  The dock that the parts should be shipped to.  */  
   "ShipToDock":string,
      /**  The Internal PartNum for the Package Code.  */  
   "PkgCodePartNum":string,
      /**  Vendor Number.  */  
   "VendorNum":number,
      /**  Vendor ID.  */  
   "VendorID":string,
      /**  Vendor Purchase Point.  */  
   "VendorPurPoint":string,
      /**  Vendor Address line 1.  */  
   "VendorAddress1":string,
      /**  Vendor Address line 2.  */  
   "VendorAddress2":string,
      /**  Vendor Address line 3.  */  
   "VendorAddress3":string,
      /**  Vendor City.  */  
   "VendorCity":string,
      /**  Vendor State.  */  
   "VendorState":string,
      /**  Vendor Zip.  */  
   "VendorZip":string,
      /**  Vendor Country Number.  */  
   "VendorCountryNum":number,
      /**  Vendor Country Description.  */  
   "VendorCountryDesc":string,
      /**  Our Dock ID.  */  
   "OurDock":string,
      /**  Value to display on package control label.  */  
   "LabelValue01":string,
      /**  Value to display on package control label.  */  
   "LabelValue02":string,
      /**  Value to display on package control label.  */  
   "LabelValue03":string,
      /**  Value to display on package control label.  */  
   "LabelValue04":string,
      /**  Value to display on package control label.  */  
   "LabelValue05":string,
      /**  Value to display on package control label.  */  
   "LabelValue06":string,
      /**  Value to display on package control label.  */  
   "LabelValue07":string,
      /**  Value to display on package control label.  */  
   "LabelValue08":string,
      /**  Value to display on package control label.  */  
   "LabelValue09":string,
      /**  Value to display on package control label.  */  
   "LabelValue10":string,
      /**  Value to display on package control label.  */  
   "LabelValue11":string,
      /**  Value to display on package control label.  */  
   "LabelValue12":string,
      /**  Value to display on package control label.  */  
   "LabelValue13":string,
      /**  Value to display on package control label.  */  
   "LabelValue14":string,
      /**  Value to display on package control label.  */  
   "LabelValue15":string,
      /**  Value to display on package control label.  */  
   "LabelValue16":string,
      /**  Value to display on package control label.  */  
   "LabelValue17":string,
      /**  Value to display on package control label.  */  
   "LabelValue18":string,
      /**  Value to display on package control label.  */  
   "LabelValue19":string,
      /**  Value to display on package control label.  */  
   "LabelValue20":string,
      /**  Value to display on package control label.  */  
   "LabelValue21":string,
      /**  Value to display on package control label.  */  
   "LabelValue22":string,
      /**  Value to display on package control label.  */  
   "LabelValue23":string,
      /**  Value to display on package control label.  */  
   "LabelValue24":string,
      /**  Value to display on package control label.  */  
   "LabelValue25":string,
      /**  Value to display on package control label.  */  
   "LabelValue26":string,
      /**  Value to display on package control label.  */  
   "LabelValue27":string,
      /**  Value to display on package control label.  */  
   "LabelValue28":string,
      /**  Value to display on package control label.  */  
   "LabelValue29":string,
      /**  Value to display on package control label.  */  
   "LabelValue30":string,
      /**  Reserved for development use.  */  
   "PkgControlCharacter01":string,
      /**  Reserved for development use.  */  
   "PkgControlCharacter02":string,
      /**  Reserved for development use.  */  
   "PkgControlCharacter03":string,
      /**  Reserved for development use.  */  
   "PkgControlCharacter04":string,
      /**  Reserved for development use.  */  
   "PkgControlCharacter05":string,
      /**  Reserved for development use.  */  
   "PkgControlDate01":string,
      /**  Reserved for development use.  */  
   "PkgControlDate02":string,
      /**  Reserved for development use.  */  
   "PkgControlBoolean01":boolean,
      /**  Reserved for development use.  */  
   "PkgControlBoolean02":boolean,
      /**  Reserved for development use.  */  
   "PkgControlInteger01":number,
      /**  Reserved for development use.  */  
   "PkgControlInteger02":number,
      /**  Reserved for development use.  */  
   "PkgControlDecimal01":number,
      /**  Reserved for development use.  */  
   "PkgControlDecimal02":number,
      /**  Package Control Type.  Valid values are “Static” or “Dynamic”.  */  
   "PkgControlType":string,
      /**  Package Control ID Code.  */  
   "PkgControlIDCode":string,
      /**  External Length dimension.  */  
   "ExternalLength":number,
      /**  External Width dimension.  */  
   "ExternalWidth":number,
      /**  External Height dimension.  */  
   "ExternalHeight":number,
      /**  External Volume.  */  
   "ExternalVolume":number,
      /**  Tare Weight.  */  
   "TareWeight":number,
      /**  Incremental tally of number of times PCID label has been printed.  */  
   "LabelPrintCount":number,
      /**  Indicates if the expendable PCID will be tracked.  */  
   "TrackExpendable":boolean,
      /**  Indicates if the returnable PCID will be tracked.  */  
   "TrackReturnable":boolean,
      /**  Label Type.  */  
   "LabelType":string,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
      /**  Ship To Customer Number.  */  
   "CustNum":number,
      /**  Indicates if the PCID is expendable.  */  
   "ContainerExpendable":boolean,
      /**  Ship To Customer ID.  */  
   "CustID":string,
      /**  Ship To Customer Name.  */  
   "CustName":string,
      /**  Vendor Name.  */  
   "VendorName":string,
      /**  Vendor Purchase Point Name.  */  
   "VendorPPName":string,
      /**  True if the inventory referenced during Adhoc PCID had not yet been received and the PCID needed to be staged.  */  
   "AdhocStagedInventory":boolean,
      /**  UpdatedByEmpID  */  
   "UpdatedByEmpID":string,
      /**  Raw Barcode Scan prior to execution of any extract logic.  */  
   "RawBarcodeScan":string,
      /**  OutboundContainer  */  
   "OutboundContainer":boolean,
      /**  PkgControlStatus value prior to being added to a pack.  */  
   "BeforePackPkgControlStatus":string,
      /**  LabelPrintControlStatus value prior to being added to a pack.  */  
   "BeforePackLabelPrintControlStatus":string,
      /**  To indicate the source process when a PCID was added to a pack.  */  
   "PackedFromSource":string,
      /**  Date last counted.  Updated during the cycle count Posting Process.  */  
   "LastCountedDate":string,
      /**  TFPackNum  */  
   "TFPackNum":number,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PkgControlHeaderRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Package Control Identification Number  */  
   "PCID":string,
      /**  Site where the PCID is currently located.  */  
   "Plant":string,
      /**  Warehouse where the PCID is currently located.  */  
   "WarehouseCode":string,
      /**  Warehouse Bin where the PCID is currently located.  */  
   "BinNum":string,
      /**  Warehouse where the PCID return stock needs to be returned to.  */  
   "ReturnToWarehouseCode":string,
      /**  Warehouse Bin where the PCID return stock needs to be returned to.  */  
   "ReturnToBinNum":string,
      /**  PCID current status.  */  
   "PkgControlStatus":string,
      /**  PCID prior status.  */  
   "PkgControlPriorStatus":string,
      /**  Label Print Control status.  */  
   "LabelPrintControlStatus":string,
      /**  Label Print Control prior status.  */  
   "LabelPrintControlPriorStatus":string,
      /**  If false then PCID is a single-level PCID that cannot be associated with a Parent.  */  
   "AllowParentPCID":boolean,
      /**  If false then PCID must contain only one PartNum.  */  
   "AllowMixedParts":boolean,
      /**  If false then PCID must contain only one LotNum for each Part on the PCID.  */  
   "AllowMixedLots":boolean,
      /**  If false then PCID must contain only one UOM per Part on the PCID.  */  
   "AllowMixedUOMs":boolean,
      /**  If false then PCID is restricted to containing single-level child PCIDs only and those child PCIDs must contain the same PartNum, Part UOM, or Part Quantity per child PCID.  This is referred to as a Master PCID, otherwise it would be referred to as a MixedMaster PCID.  */  
   "AllowMixedChildPCIDs":boolean,
      /**  If false then PCID must contain only one Serial Number per PCID.  */  
   "AllowMultipleSerialNumPerPCID":boolean,
      /**  If false then the standard PCID printing logic is used. If true then the Label Print Control logic and rules will apply and be enforced.  */  
   "LabelPrintControlled":boolean,
      /**  If false then the number of PCID label prints will not be tracked.  */  
   "LabelPrintCounter":boolean,
      /**  If false then PkgControlHeader and PkgControlItem cannot be voided or deleted.  */  
   "AllowVoids":boolean,
      /**  If false then PkgControlHeader and PkgControlItem cannot be deleted.  */  
   "AllowDeletes":boolean,
      /**  If true then PkgControlHeader and PkgControlItem will be written to history tables and removed from the maintenance tables on void, delete or close/collapse.  */  
   "ArchivePCIDHistory":boolean,
      /**  Unique packaging code assigned by the user.  */  
   "PkgCode":string,
      /**  User defined code which uniquely identifies the UOM for length, width, and height.  */  
   "LWHDimensionUOM":string,
      /**  Length dimension.  */  
   "Length":number,
      /**  Width dimension.  */  
   "Width":number,
      /**  Height dimension.  */  
   "Height":number,
      /**  User defined code which uniquely identifies the UOM for volume.  */  
   "VolumeUOM":string,
      /**  Volume.  */  
   "Volume":number,
      /**  User defined code which uniquely identifies the UOM for weight.  */  
   "WeightUOM":string,
      /**  Maximum Weight.  */  
   "MaximumWeight":number,
      /**  Calculated Weight.  */  
   "CalculatedWeight":number,
      /**  The total weight of the parts and the container combined.  */  
   "TotalWeight":number,
      /**  Maximum number of PCIDs allowed if vertically stacked.  */  
   "MaximumStack":number,
      /**  Position Sequence within a parent PCID.  */  
   "PositionSeq":number,
      /**  Trailer ID.  */  
   "TrailerID":string,
      /**  Bond or Security Seal ID.  */  
   "SecuritySealID":string,
      /**  Raw PCID as scanned or generated.  */  
   "RawPCIDLicensePlate":string,
      /**  GS1-128 as generated by the Legal Number process.  GS1-128 supersedes the former UCC/EAN128 standards.  */  
   "GS1128":string,
      /**  For a static PCID, each time the PCID is collapsed this counter is incremented, and the collapse counter is stamped on any PartTran records generated throughout the life of the PCID.  */  
   "PkgControlCollapseCounter":number,
      /**  System date and time when the row was created.  */  
   "CreatedDate":string,
      /**  The user ID that created this row.  */  
   "CreatedBy":string,
      /**  System date and time when the row was last updated.  */  
   "UpdatedDate":string,
      /**  The user ID that last updated this row.  */  
   "UpdatedBy":string,
      /**  Last PCID Scanned.  */  
   "LastPCIDScanned":string,
      /**  Number of next level down child PCIDs associated to this PCID.  */  
   "NumberOfPCIDs":number,
      /**  Flag used to fire the auto print rule that will print the labels.  */  
   "AutoPrint":boolean,
      /**  System date and time when the row was created.  */  
   "LPCCreatedDate":string,
      /**  The user ID that created this record.  */  
   "LPCCreatedBy":string,
      /**  Printer ID that printed the label.  */  
   "LPCPrinterID":string,
      /**  User that printed the label.  */  
   "LPCPrintedBy":string,
      /**  Label feature. Displays what transaction the label was printed from.  */  
   "LPCPrintedFromTx":string,
      /**  Ad Hoc feature. Displays what transaction type the label was printed from.  */  
   "LPCPrintedFromTxType":string,
      /**  The job for which the label was printed.  */  
   "LPCJobNum":string,
      /**  The operation sequence for which the label was printed.  */  
   "LPCOprSeq":number,
      /**  The assembly sequence for which the label was printed.  */  
   "LPCAssemblySeq":number,
      /**  Shift that the label was created on or shift entered in Ad Hoc print program.  */  
   "LPCShift":number,
      /**  Operator who created the label if printed from MES, Labor Reporting employee if printed from Ad Hoc Manufacturing Backup, or blank otherwise.  */  
   "LPCOperatorEmpID":string,
      /**  Original Source PCID for repack. This field will be populated with the source container PCID when assigning a repack label.  */  
   "OriginalSourcePCID":string,
      /**  This field will be populated with the new PCID that replaced this PCID when using the overlay feature.  */  
   "OverlaidByPCID":string,
      /**  Set to True when PCID has been overlaid using the overlay feature.  */  
   "Overlaid":boolean,
      /**  Partial Container – set to true when the container is created from the Ad Hoc – Partial program.  */  
   "ContainerPartial":boolean,
      /**  If true the container was repacked.  */  
   "ContainerRepacked":boolean,
      /**  If true the container used is a returnable container.  */  
   "ContainerReturnable":boolean,
      /**  Our Vendor ID for the Customer being Shipped To.  */  
   "OurSupplierCode":string,
      /**  Site Name.  */  
   "PlantName":string,
      /**  Site Address line 1.  */  
   "PlantAddress1":string,
      /**  Site Address line 2.  */  
   "PlantAddress2":string,
      /**  Site Address line 3.  */  
   "PlantAddress3":string,
      /**  Site City.  */  
   "PlantCity":string,
      /**  Site State.  */  
   "PlantState":string,
      /**  Site Zip.  */  
   "PlantZip":string,
      /**  Site Country Number.  */  
   "PlantCountryNum":number,
      /**  Site Country Description.  */  
   "PlantCountryDesc":string,
      /**  Site Phone.  */  
   "PlantPhone":string,
      /**  Pack Number if applicable.  */  
   "PackNum":number,
      /**  Ship To Customer Container Part Number.  */  
   "CustContainerPartNum":string,
      /**  EDI Ship To Number populated with the final destination if shipping to an Intermediate Consignee, otherwise an actual ShipToNum.  */  
   "EDIShipToNum":string,
      /**  Ship To Number.  */  
   "ShipToNum":string,
      /**  Name of the Ship To that the PCID is going to.  */  
   "ShipToName":string,
      /**  Address line 1 of the Ship To that the PCID is going to.  */  
   "ShipToAddress1":string,
      /**  Address line 2 of the Ship To that the PCID is going to.  */  
   "ShipToAddress2":string,
      /**  Address line 3 of the Ship To that the PCID is going to.  */  
   "ShipToAddress3":string,
      /**  City of the Ship To that the PCID is going to.  */  
   "ShipToCity":string,
      /**  State of the Ship To that the PCID is going to.  */  
   "ShipToState":string,
      /**  Zip of the Ship To that the PCID is going to.  */  
   "ShipToZip":string,
      /**  Country number of the Ship To that the PCID is going to.  */  
   "ShipToCountryNum":number,
      /**  Country of the Ship To that the PCID is going to.  */  
   "ShipToCountryDesc":string,
      /**  The dock that the parts should be shipped to.  */  
   "ShipToDock":string,
      /**  The Internal PartNum for the Package Code.  */  
   "PkgCodePartNum":string,
      /**  Vendor Number.  */  
   "VendorNum":number,
      /**  Vendor ID.  */  
   "VendorID":string,
      /**  Vendor Purchase Point.  */  
   "VendorPurPoint":string,
      /**  Vendor Address line 1.  */  
   "VendorAddress1":string,
      /**  Vendor Address line 2.  */  
   "VendorAddress2":string,
      /**  Vendor Address line 3.  */  
   "VendorAddress3":string,
      /**  Vendor City.  */  
   "VendorCity":string,
      /**  Vendor State.  */  
   "VendorState":string,
      /**  Vendor Zip.  */  
   "VendorZip":string,
      /**  Vendor Country Number.  */  
   "VendorCountryNum":number,
      /**  Vendor Country Description.  */  
   "VendorCountryDesc":string,
      /**  Our Dock ID.  */  
   "OurDock":string,
      /**  Value to display on package control label.  */  
   "LabelValue01":string,
      /**  Value to display on package control label.  */  
   "LabelValue02":string,
      /**  Value to display on package control label.  */  
   "LabelValue03":string,
      /**  Value to display on package control label.  */  
   "LabelValue04":string,
      /**  Value to display on package control label.  */  
   "LabelValue05":string,
      /**  Value to display on package control label.  */  
   "LabelValue06":string,
      /**  Value to display on package control label.  */  
   "LabelValue07":string,
      /**  Value to display on package control label.  */  
   "LabelValue08":string,
      /**  Value to display on package control label.  */  
   "LabelValue09":string,
      /**  Value to display on package control label.  */  
   "LabelValue10":string,
      /**  Value to display on package control label.  */  
   "LabelValue11":string,
      /**  Value to display on package control label.  */  
   "LabelValue12":string,
      /**  Value to display on package control label.  */  
   "LabelValue13":string,
      /**  Value to display on package control label.  */  
   "LabelValue14":string,
      /**  Value to display on package control label.  */  
   "LabelValue15":string,
      /**  Value to display on package control label.  */  
   "LabelValue16":string,
      /**  Value to display on package control label.  */  
   "LabelValue17":string,
      /**  Value to display on package control label.  */  
   "LabelValue18":string,
      /**  Value to display on package control label.  */  
   "LabelValue19":string,
      /**  Value to display on package control label.  */  
   "LabelValue20":string,
      /**  Value to display on package control label.  */  
   "LabelValue21":string,
      /**  Value to display on package control label.  */  
   "LabelValue22":string,
      /**  Value to display on package control label.  */  
   "LabelValue23":string,
      /**  Value to display on package control label.  */  
   "LabelValue24":string,
      /**  Value to display on package control label.  */  
   "LabelValue25":string,
      /**  Value to display on package control label.  */  
   "LabelValue26":string,
      /**  Value to display on package control label.  */  
   "LabelValue27":string,
      /**  Value to display on package control label.  */  
   "LabelValue28":string,
      /**  Value to display on package control label.  */  
   "LabelValue29":string,
      /**  Value to display on package control label.  */  
   "LabelValue30":string,
      /**  Reserved for development use.  */  
   "PkgControlCharacter01":string,
      /**  Reserved for development use.  */  
   "PkgControlCharacter02":string,
      /**  Reserved for development use.  */  
   "PkgControlCharacter03":string,
      /**  Reserved for development use.  */  
   "PkgControlCharacter04":string,
      /**  Reserved for development use.  */  
   "PkgControlCharacter05":string,
      /**  Reserved for development use.  */  
   "PkgControlDate01":string,
      /**  Reserved for development use.  */  
   "PkgControlDate02":string,
      /**  Reserved for development use.  */  
   "PkgControlBoolean01":boolean,
      /**  Reserved for development use.  */  
   "PkgControlBoolean02":boolean,
      /**  Reserved for development use.  */  
   "PkgControlInteger01":number,
      /**  Reserved for development use.  */  
   "PkgControlInteger02":number,
      /**  Reserved for development use.  */  
   "PkgControlDecimal01":number,
      /**  Reserved for development use.  */  
   "PkgControlDecimal02":number,
      /**  Package Control Type.  Valid values are “Static” or “Dynamic”.  */  
   "PkgControlType":string,
      /**  Package Control ID Code.  */  
   "PkgControlIDCode":string,
      /**  External Length dimension.  */  
   "ExternalLength":number,
      /**  External Width dimension.  */  
   "ExternalWidth":number,
      /**  External Height dimension.  */  
   "ExternalHeight":number,
      /**  External Volume.  */  
   "ExternalVolume":number,
      /**  Tare Weight.  */  
   "TareWeight":number,
      /**  Incremental tally of number of times PCID label has been printed.  */  
   "LabelPrintCount":number,
      /**  Indicates if the expendable PCID will be tracked.  */  
   "TrackExpendable":boolean,
      /**  Indicates if the returnable PCID will be tracked.  */  
   "TrackReturnable":boolean,
      /**  Label Type.  */  
   "LabelType":string,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
      /**  Ship To Customer Number.  */  
   "CustNum":number,
      /**  Indicates if the PCID is expendable.  */  
   "ContainerExpendable":boolean,
      /**  Ship To Customer ID.  */  
   "CustID":string,
      /**  Ship To Customer Name.  */  
   "CustName":string,
      /**  Vendor Name.  */  
   "VendorName":string,
      /**  Vendor Purchase Point Name.  */  
   "VendorPPName":string,
      /**  True if the inventory referenced during Adhoc PCID had not yet been received and the PCID needed to be staged.  */  
   "AdhocStagedInventory":boolean,
      /**  UpdatedByEmpID  */  
   "UpdatedByEmpID":string,
      /**  Raw Barcode Scan prior to execution of any extract logic.  */  
   "RawBarcodeScan":string,
      /**  OutboundContainer  */  
   "OutboundContainer":boolean,
      /**  PkgControlStatus value prior to being added to a pack.  */  
   "BeforePackPkgControlStatus":string,
      /**  LabelPrintControlStatus value prior to being added to a pack.  */  
   "BeforePackLabelPrintControlStatus":string,
      /**  To indicate the source process when a PCID was added to a pack.  */  
   "PackedFromSource":string,
      /**  Date last counted.  Updated during the cycle count Posting Process.  */  
   "LastCountedDate":string,
      /**  TFPackNum  */  
   "TFPackNum":number,
      /**  Child PCID count  */  
   "ChildPCIDCount":number,
      /**  Indicates if EnableCboReasonCode control should be Enabled.  */  
   "EnableCboReasonCode":boolean,
      /**  if the PkgControlID is expendable  */  
   "Expendable":boolean,
   "ExtensionDigit":number,
      /**  Used for Handheld, this field will determine if the ASN (Advanced Ship Notice) has been sent/printed  */  
   "HHASN":boolean,
   "HHItemIUM":string,
   "HHItemPartNum":string,
      /**  Used for Handheld.  */  
   "HHItemQuantity":number,
   "HHItemRevisionNum":string,
      /**  Used for HandHeld, it can be either PkgControlHeader.LabelPrintControlStatus OR PkgControlHeader.PkgControlStatus  */  
   "HHLabelStatus":string,
      /**   Used for handHeld             
If PkgControlHeader.PkgControlType = Static then PkgControlHeader.PackNum
If PkgControlHeader.PkgControlType = Dynamic then PkgControlItem.PackNum  */  
   "HHPackSlip":number,
      /**  Used for HandHeld, It could contains a list of PackNum from the children  */  
   "HHPackSlipList":string,
   "LWHDimUOM":string,
      /**  Warehouse Bin where the Parent PCID is currently located.  */  
   "ParentBinNum":string,
      /**  System date and time when the row was created.  */  
   "ParentCreatedDate":string,
      /**  Ship To Customer Container Part Number.  */  
   "ParentCustContainerPartNum":string,
      /**  Parent Ship To Customer ID.  */  
   "ParentCustID":string,
      /**  If false then the standard PCID printing logic is used. If true then the Label Print Control logic and rules will apply and be enforced.  */  
   "ParentLabelPrintControlled":boolean,
      /**  Label Print Control status.  */  
   "ParentLabelPrintControlStatus":string,
      /**  Label Type.  */  
   "ParentLabelType":string,
      /**  Number of next level down child PCIDs associated to this PCID.  */  
   "ParentNumberOfPCIDs":number,
      /**  Pack Number if applicable.  */  
   "ParentPackNum":number,
      /**  Parent Package Control Identification Number  */  
   "ParentPCID":string,
      /**  Unique packaging code assigned by the user.  */  
   "ParentPkgCode":string,
      /**  The Internal PartNum for the Package Code.  */  
   "ParentPkgCodePartNum":string,
      /**  PCID current status.  */  
   "ParentPkgControlStatus":string,
      /**  Package Control Type.  Valid values are “Static” or “Dynamic”.  */  
   "ParentPkgControlType":string,
      /**  Site where the Parent PCID is currently located.  */  
   "ParentPlant":string,
      /**  Site Name.  */  
   "ParentPlantName":string,
      /**  Parent Ship To Number.  */  
   "ParentShipToNum":string,
      /**  Warehouse where the Parent PCID is currently located.  */  
   "ParentWarehouseCode":string,
   "ParentWhseDesc":string,
   "PartDesc":string,
   "PkgCodeDesc":string,
   "PkgType":string,
      /**  Reason Code  */  
   "ReasonCode":string,
   "ResCodeIn":string,
   "ResCodeOut":string,
   "RTWhseDesc":string,
      /**  Ship To Container Part ID  */  
   "ShipToContainerPartID":string,
      /**  Transaction document type  */  
   "TranDocTypeID":string,
   "WhseDesc":string,
      /**  Adjust Inventory  */  
   "AdjustInventory":boolean,
      /**  Container UOM  */  
   "ContainerUOM":string,
   "DisableReasonCode":boolean,
      /**  Indicates if BtnVoidPCIDInv control should be Enabled.  */  
   "EnableBtnVoidPCIDInv":boolean,
   "BitFlag":number,
   "BinDescription":string,
   "WarehouseDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PkgControlItemRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Package Control Identification Number  */  
   "PCID":string,
      /**  PCID Item Sequence  */  
   "PCIDItemSeq":number,
      /**  The PCID of the item in this PCID.  */  
   "ItemPCID":string,
      /**  The Part Number of the item in this PCID.  */  
   "ItemPartNum":string,
      /**  The Revision Number of the item in this PCID.  */  
   "ItemRevisionNum":string,
      /**  The Part Description of the item in this PCID.  */  
   "ItemPartDesc":string,
      /**  The Lot Number of the item in this PCID.  */  
   "ItemLotNum":string,
      /**  The Inventory UOM of the item in this PCID.  */  
   "ItemIUM":string,
      /**  The Quantity of the item in this PCID.  */  
   "ItemQuantity":number,
      /**  Site Identifier.  */  
   "Plant":string,
      /**  Demand Type.  */  
   "DemandType":string,
      /**  Order Number of the demand.  */  
   "OrderNum":number,
      /**  Order Line Number of the demand.  */  
   "OrderLine":number,
      /**  Order Release Number of the demand.  */  
   "OrderRelNum":number,
      /**  Job Number of the demand.  */  
   "JobNum":string,
      /**  Assembly Sequence Number of the demand.  */  
   "AssemblySeq":number,
      /**  Material Sequence Number of the demand.  */  
   "MtlSeq":number,
      /**  Transfer Order Number of the demand.  */  
   "TFOrdNum":string,
      /**  Transfer Order Line of the demand.  */  
   "TFOrdLine":number,
      /**  Pack Number if applicable.  */  
   "PackNum":number,
      /**  Pack Line Number if applicable.  */  
   "PackLine":number,
      /**  Ship To Customer Part Number.  */  
   "CustPartNum":string,
      /**  Ship To Customer Part Revision.  */  
   "CustPartRev":string,
      /**  The PO number that these parts were created against.  */  
   "CustPONum":string,
      /**  Engineering Alert to display on the label.  */  
   "CustShipToEngineerAlert":string,
      /**  Safety Indicator to display on the label.  */  
   "SafetyIndicator":boolean,
      /**  The Internal PartNum for the Package Code.  */  
   "PkgCodePartNum":string,
      /**  Purchase Order Type.  */  
   "VendorPOType":string,
      /**  Purchase Order Number.  */  
   "VendorPONum":number,
      /**  Purchase Order Line Number.  */  
   "VendorPOLine":number,
      /**  Purchase Order Release Number.  */  
   "VendorPORelNum":number,
      /**  Supplier Part Number.  */  
   "VendorPartNum":string,
      /**  Supplier Unit of Measure.  */  
   "VendorUOM":string,
      /**  Supplier Quantity.  */  
   "VendorQty":number,
      /**  Receipt Packing Slip.  */  
   "ReceiptPackSlip":string,
      /**  Receipt Type.  */  
   "ReceiptType":string,
      /**  Receipt Date.  */  
   "ReceiptDate":string,
      /**  Receipt UOM.  */  
   "ReceiptUOM":string,
      /**  Receipt Quantity.  */  
   "ReceiptQty":number,
      /**  RMA Number.  */  
   "RMANum":number,
      /**  RMA Line.  */  
   "RMALine":number,
      /**  Reserved for development use.  */  
   "PkgControlCharacter01":string,
      /**  Reserved for development use.  */  
   "PkgControlCharacter02":string,
      /**  Reserved for development use.  */  
   "PkgControlCharacter03":string,
      /**  Reserved for development use.  */  
   "PkgControlCharacter04":string,
      /**  Reserved for development use.  */  
   "PkgControlCharacter05":string,
      /**  Reserved for development use.  */  
   "PkgControlDate01":string,
      /**  Reserved for development use.  */  
   "PkgControlDate02":string,
      /**  Reserved for development  */  
   "PkgControlBoolean01":boolean,
      /**  Reserved for development use.  */  
   "PkgControlBoolean02":boolean,
      /**  Reserved for development use.  */  
   "PkgControlDecimal01":number,
      /**  Reserved for development use.  */  
   "PkgControlDecimal02":number,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
      /**  Set to INVOICED when invoice created, set to POSTED when invoice is posted.  */  
   "ShipmentInvoicedPosted":string,
      /**  The job number on which the quantity on this record were produced  */  
   "SupplyJobNum":string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "ItemAttributeSetID":number,
      /**  TFPackNum  */  
   "TFPackNum":number,
      /**  TFPackLine  */  
   "TFPackLine":number,
      /**  Set to true if this PkgControlItem record was created by processing a mtl queue picking record  */  
   "ItemPicked":boolean,
      /**  SysRowID of the PartWip to which this item relates. The value is a GUID.  If the item is not WIP, this column is blank.  This value should only ever be populated in a Staging or History PCID, never an Inventory PCID.  */  
   "ItemPartWipSysRowID":string,
      /**  Internal flag to distiguish between tracking of issued raw material, and the actual manufactured product.  "R" - Raw Material a part which was issued to the job.  "M" - Manufactured Part. The part that is being manufactured.  */  
   "TrackType":string,
      /**  Job operation sequence number that part is related to.  */  
   "OprSeq":number,
      /**  Indicates if the WIP has been sent to Non-Conformance.  */  
   "InNonConformance":boolean,
      /**  Indicates if the WIP has failed Non-Conformance and has been moved to DMR Processing.  */  
   "InDMRProcessing":boolean,
   "ChildPCIDOrPart":string,
   "CustID":string,
   "CustName":string,
      /**  Number of next level down child PCIDs associated to this PCID.  */  
   "NumberOfPCIDs":number,
   "PackageCode":string,
      /**  Site Name.  */  
   "PlantName":string,
      /**  Warehouse where the PCID is currently located.  */  
   "WarehouseCode":string,
   "WhseDesc":string,
      /**  Warehouse Bin where the PCID is currently located.  */  
   "BinNum":string,
      /**  The Full Description of the Attribute Set.  */  
   "ItemAttributeSetDescription":string,
      /**  The Short Description of the Attribute Set.  */  
   "ItemAttributeSetShortDescription":string,
   "ItemPartAttrClassID":string,
   "ItemType":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param toWhse
      @param toBin
      @param ds
   */  
export interface CommitPCIDTransfer_input{
   toWhse:string,
   toBin:string,
   ds:Erp_Tablesets_PkgControlIDTableset[],
}

export interface CommitPCIDTransfer_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PkgControlIDTableset[],
}
}

   /** Required : 
      @param ipCompany
      @param ipPlant
      @param ipPassword
   */  
export interface ConfirmSupervisorPassword_input{
   ipCompany:string,
   ipPlant:string,
   ipPassword:string,
}

export interface ConfirmSupervisorPassword_output{
   returnObj:boolean,
}

   /** Required : 
      @param pcID
   */  
export interface DeleteByID_input{
   pcID:string,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_PCLabelValuesRow{
   Company:string,
   LabelSeq:number,
   LabelValues:string,
   PCID:string,
   ValueField:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PkgControlCustPartNumRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Package Control Identification Number.  */  
   PCID:string,
      /**  PCID Customer Part Sequence.  */  
   PCIDCustPartSeq:number,
      /**  Used for MixedMaster parent PCIDs.  Customer Part Number associated to the MixedMaster parent PCID.  */  
   CustPartNum:string,
      /**  Used for MixedMaster parent PCIDs. Number of parts per parent PCID for the Customer Part Number associated to the MixedMaster parent PCID.  */  
   CustQtyPerContainer:number,
      /**  Used for MixedMaster parent PCIDs.  Number of PCIDs for the Customer Part Number associated to the MixedMaster parent PCID.  */  
   CustNumContainers:number,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PkgControlHeaderListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Package Control Identification Number  */  
   PCID:string,
      /**  Site where the PCID is currently located.  */  
   Plant:string,
      /**  Warehouse where the PCID is currently located.  */  
   WarehouseCode:string,
      /**  Warehouse Bin where the PCID is currently located.  */  
   BinNum:string,
      /**  Warehouse where the PCID return stock needs to be returned to.  */  
   ReturnToWarehouseCode:string,
      /**  Warehouse Bin where the PCID return stock needs to be returned to.  */  
   ReturnToBinNum:string,
      /**  PCID current status.  */  
   PkgControlStatus:string,
      /**  PCID prior status.  */  
   PkgControlPriorStatus:string,
      /**  Label Print Control status.  */  
   LabelPrintControlStatus:string,
      /**  Label Print Control prior status.  */  
   LabelPrintControlPriorStatus:string,
      /**  If false then PCID is a single-level PCID that cannot be associated with a Parent.  */  
   AllowParentPCID:boolean,
      /**  If false then PCID must contain only one PartNum.  */  
   AllowMixedParts:boolean,
      /**  If false then PCID must contain only one LotNum for each Part on the PCID.  */  
   AllowMixedLots:boolean,
      /**  If false then PCID must contain only one UOM per Part on the PCID.  */  
   AllowMixedUOMs:boolean,
      /**  If false then PCID is restricted to containing single-level child PCIDs only and those child PCIDs must contain the same PartNum, Part UOM, or Part Quantity per child PCID.  This is referred to as a Master PCID, otherwise it would be referred to as a MixedMaster PCID.  */  
   AllowMixedChildPCIDs:boolean,
      /**  If false then PCID must contain only one Serial Number per PCID.  */  
   AllowMultipleSerialNumPerPCID:boolean,
      /**  If false then the standard PCID printing logic is used. If true then the Label Print Control logic and rules will apply and be enforced.  */  
   LabelPrintControlled:boolean,
      /**  If false then the number of PCID label prints will not be tracked.  */  
   LabelPrintCounter:boolean,
      /**  If false then PkgControlHeader and PkgControlItem cannot be voided or deleted.  */  
   AllowVoids:boolean,
      /**  If false then PkgControlHeader and PkgControlItem cannot be deleted.  */  
   AllowDeletes:boolean,
      /**  If true then PkgControlHeader and PkgControlItem will be written to history tables and removed from the maintenance tables on void, delete or close/collapse.  */  
   ArchivePCIDHistory:boolean,
      /**  Unique packaging code assigned by the user.  */  
   PkgCode:string,
      /**  User defined code which uniquely identifies the UOM for length, width, and height.  */  
   LWHDimensionUOM:string,
      /**  Length dimension.  */  
   Length:number,
      /**  Width dimension.  */  
   Width:number,
      /**  Height dimension.  */  
   Height:number,
      /**  User defined code which uniquely identifies the UOM for volume.  */  
   VolumeUOM:string,
      /**  Volume.  */  
   Volume:number,
      /**  User defined code which uniquely identifies the UOM for weight.  */  
   WeightUOM:string,
      /**  Maximum Weight.  */  
   MaximumWeight:number,
      /**  Calculated Weight.  */  
   CalculatedWeight:number,
      /**  The total weight of the parts and the container combined.  */  
   TotalWeight:number,
      /**  Maximum number of PCIDs allowed if vertically stacked.  */  
   MaximumStack:number,
      /**  Position Sequence within a parent PCID.  */  
   PositionSeq:number,
      /**  Trailer ID.  */  
   TrailerID:string,
      /**  Bond or Security Seal ID.  */  
   SecuritySealID:string,
      /**  Raw PCID as scanned or generated.  */  
   RawPCIDLicensePlate:string,
      /**  GS1-128 as generated by the Legal Number process.  GS1-128 supersedes the former UCC/EAN128 standards.  */  
   GS1128:string,
      /**  For a static PCID, each time the PCID is collapsed this counter is incremented, and the collapse counter is stamped on any PartTran records generated throughout the life of the PCID.  */  
   PkgControlCollapseCounter:number,
      /**  System date and time when the row was created.  */  
   CreatedDate:string,
      /**  The user ID that created this row.  */  
   CreatedBy:string,
      /**  System date and time when the row was last updated.  */  
   UpdatedDate:string,
      /**  The user ID that last updated this row.  */  
   UpdatedBy:string,
      /**  Last PCID Scanned.  */  
   LastPCIDScanned:string,
      /**  Number of next level down child PCIDs associated to this PCID.  */  
   NumberOfPCIDs:number,
      /**  Flag used to fire the auto print rule that will print the labels.  */  
   AutoPrint:boolean,
      /**  System date and time when the row was created.  */  
   LPCCreatedDate:string,
      /**  The user ID that created this record.  */  
   LPCCreatedBy:string,
      /**  Printer ID that printed the label.  */  
   LPCPrinterID:string,
      /**  User that printed the label.  */  
   LPCPrintedBy:string,
      /**  Label feature. Displays what transaction the label was printed from.  */  
   LPCPrintedFromTx:string,
      /**  Ad Hoc feature. Displays what transaction type the label was printed from.  */  
   LPCPrintedFromTxType:string,
      /**  The job for which the label was printed.  */  
   LPCJobNum:string,
      /**  The operation sequence for which the label was printed.  */  
   LPCOprSeq:number,
      /**  The assembly sequence for which the label was printed.  */  
   LPCAssemblySeq:number,
      /**  Shift that the label was created on or shift entered in Ad Hoc print program.  */  
   LPCShift:number,
      /**  Operator who created the label if printed from MES, Labor Reporting employee if printed from Ad Hoc Manufacturing Backup, or blank otherwise.  */  
   LPCOperatorEmpID:string,
      /**  Original Source PCID for repack. This field will be populated with the source container PCID when assigning a repack label.  */  
   OriginalSourcePCID:string,
      /**  This field will be populated with the new PCID that replaced this PCID when using the overlay feature.  */  
   OverlaidByPCID:string,
      /**  Set to True when PCID has been overlaid using the overlay feature.  */  
   Overlaid:boolean,
      /**  Partial Container – set to true when the container is created from the Ad Hoc – Partial program.  */  
   ContainerPartial:boolean,
      /**  If true the container was repacked.  */  
   ContainerRepacked:boolean,
      /**  If true the container used is a returnable container.  */  
   ContainerReturnable:boolean,
      /**  Our Vendor ID for the Customer being Shipped To.  */  
   OurSupplierCode:string,
      /**  Site Name.  */  
   PlantName:string,
      /**  Site Address line 1.  */  
   PlantAddress1:string,
      /**  Site Address line 2.  */  
   PlantAddress2:string,
      /**  Site Address line 3.  */  
   PlantAddress3:string,
      /**  Site City.  */  
   PlantCity:string,
      /**  Site State.  */  
   PlantState:string,
      /**  Site Zip.  */  
   PlantZip:string,
      /**  Site Country Number.  */  
   PlantCountryNum:number,
      /**  Site Country Description.  */  
   PlantCountryDesc:string,
      /**  Site Phone.  */  
   PlantPhone:string,
      /**  Pack Number if applicable.  */  
   PackNum:number,
      /**  Ship To Customer Container Part Number.  */  
   CustContainerPartNum:string,
      /**  EDI Ship To Number populated with the final destination if shipping to an Intermediate Consignee, otherwise an actual ShipToNum.  */  
   EDIShipToNum:string,
      /**  Ship To Number.  */  
   ShipToNum:string,
      /**  Name of the Ship To that the PCID is going to.  */  
   ShipToName:string,
      /**  Address line 1 of the Ship To that the PCID is going to.  */  
   ShipToAddress1:string,
      /**  Address line 2 of the Ship To that the PCID is going to.  */  
   ShipToAddress2:string,
      /**  Address line 3 of the Ship To that the PCID is going to.  */  
   ShipToAddress3:string,
      /**  City of the Ship To that the PCID is going to.  */  
   ShipToCity:string,
      /**  State of the Ship To that the PCID is going to.  */  
   ShipToState:string,
      /**  Zip of the Ship To that the PCID is going to.  */  
   ShipToZip:string,
      /**  Country number of the Ship To that the PCID is going to.  */  
   ShipToCountryNum:number,
      /**  Country of the Ship To that the PCID is going to.  */  
   ShipToCountryDesc:string,
      /**  The dock that the parts should be shipped to.  */  
   ShipToDock:string,
      /**  The Internal PartNum for the Package Code.  */  
   PkgCodePartNum:string,
      /**  Vendor Number.  */  
   VendorNum:number,
      /**  Vendor ID.  */  
   VendorID:string,
      /**  Vendor Purchase Point.  */  
   VendorPurPoint:string,
      /**  Vendor Address line 1.  */  
   VendorAddress1:string,
      /**  Vendor Address line 2.  */  
   VendorAddress2:string,
      /**  Vendor Address line 3.  */  
   VendorAddress3:string,
      /**  Vendor City.  */  
   VendorCity:string,
      /**  Vendor State.  */  
   VendorState:string,
      /**  Vendor Zip.  */  
   VendorZip:string,
      /**  Vendor Country Number.  */  
   VendorCountryNum:number,
      /**  Vendor Country Description.  */  
   VendorCountryDesc:string,
      /**  Our Dock ID.  */  
   OurDock:string,
      /**  Value to display on package control label.  */  
   LabelValue01:string,
      /**  Value to display on package control label.  */  
   LabelValue02:string,
      /**  Value to display on package control label.  */  
   LabelValue03:string,
      /**  Value to display on package control label.  */  
   LabelValue04:string,
      /**  Value to display on package control label.  */  
   LabelValue05:string,
      /**  Value to display on package control label.  */  
   LabelValue06:string,
      /**  Value to display on package control label.  */  
   LabelValue07:string,
      /**  Value to display on package control label.  */  
   LabelValue08:string,
      /**  Value to display on package control label.  */  
   LabelValue09:string,
      /**  Value to display on package control label.  */  
   LabelValue10:string,
      /**  Value to display on package control label.  */  
   LabelValue11:string,
      /**  Value to display on package control label.  */  
   LabelValue12:string,
      /**  Value to display on package control label.  */  
   LabelValue13:string,
      /**  Value to display on package control label.  */  
   LabelValue14:string,
      /**  Value to display on package control label.  */  
   LabelValue15:string,
      /**  Value to display on package control label.  */  
   LabelValue16:string,
      /**  Value to display on package control label.  */  
   LabelValue17:string,
      /**  Value to display on package control label.  */  
   LabelValue18:string,
      /**  Value to display on package control label.  */  
   LabelValue19:string,
      /**  Value to display on package control label.  */  
   LabelValue20:string,
      /**  Value to display on package control label.  */  
   LabelValue21:string,
      /**  Value to display on package control label.  */  
   LabelValue22:string,
      /**  Value to display on package control label.  */  
   LabelValue23:string,
      /**  Value to display on package control label.  */  
   LabelValue24:string,
      /**  Value to display on package control label.  */  
   LabelValue25:string,
      /**  Value to display on package control label.  */  
   LabelValue26:string,
      /**  Value to display on package control label.  */  
   LabelValue27:string,
      /**  Value to display on package control label.  */  
   LabelValue28:string,
      /**  Value to display on package control label.  */  
   LabelValue29:string,
      /**  Value to display on package control label.  */  
   LabelValue30:string,
      /**  Reserved for development use.  */  
   PkgControlCharacter01:string,
      /**  Reserved for development use.  */  
   PkgControlCharacter02:string,
      /**  Reserved for development use.  */  
   PkgControlCharacter03:string,
      /**  Reserved for development use.  */  
   PkgControlCharacter04:string,
      /**  Reserved for development use.  */  
   PkgControlCharacter05:string,
      /**  Reserved for development use.  */  
   PkgControlDate01:string,
      /**  Reserved for development use.  */  
   PkgControlDate02:string,
      /**  Reserved for development use.  */  
   PkgControlBoolean01:boolean,
      /**  Reserved for development use.  */  
   PkgControlBoolean02:boolean,
      /**  Reserved for development use.  */  
   PkgControlInteger01:number,
      /**  Reserved for development use.  */  
   PkgControlInteger02:number,
      /**  Reserved for development use.  */  
   PkgControlDecimal01:number,
      /**  Reserved for development use.  */  
   PkgControlDecimal02:number,
      /**  Package Control Type.  Valid values are “Static” or “Dynamic”.  */  
   PkgControlType:string,
      /**  Package Control ID Code.  */  
   PkgControlIDCode:string,
      /**  External Length dimension.  */  
   ExternalLength:number,
      /**  External Width dimension.  */  
   ExternalWidth:number,
      /**  External Height dimension.  */  
   ExternalHeight:number,
      /**  External Volume.  */  
   ExternalVolume:number,
      /**  Tare Weight.  */  
   TareWeight:number,
      /**  Incremental tally of number of times PCID label has been printed.  */  
   LabelPrintCount:number,
      /**  Indicates if the expendable PCID will be tracked.  */  
   TrackExpendable:boolean,
      /**  Indicates if the returnable PCID will be tracked.  */  
   TrackReturnable:boolean,
      /**  Label Type.  */  
   LabelType:string,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  Ship To Customer Number.  */  
   CustNum:number,
      /**  Indicates if the PCID is expendable.  */  
   ContainerExpendable:boolean,
      /**  Ship To Customer ID.  */  
   CustID:string,
      /**  Ship To Customer Name.  */  
   CustName:string,
      /**  Vendor Name.  */  
   VendorName:string,
      /**  Vendor Purchase Point Name.  */  
   VendorPPName:string,
      /**  True if the inventory referenced during Adhoc PCID had not yet been received and the PCID needed to be staged.  */  
   AdhocStagedInventory:boolean,
      /**  UpdatedByEmpID  */  
   UpdatedByEmpID:string,
      /**  Raw Barcode Scan prior to execution of any extract logic.  */  
   RawBarcodeScan:string,
      /**  OutboundContainer  */  
   OutboundContainer:boolean,
      /**  PkgControlStatus value prior to being added to a pack.  */  
   BeforePackPkgControlStatus:string,
      /**  LabelPrintControlStatus value prior to being added to a pack.  */  
   BeforePackLabelPrintControlStatus:string,
      /**  To indicate the source process when a PCID was added to a pack.  */  
   PackedFromSource:string,
      /**  Date last counted.  Updated during the cycle count Posting Process.  */  
   LastCountedDate:string,
      /**  TFPackNum  */  
   TFPackNum:number,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PkgControlHeaderRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Package Control Identification Number  */  
   PCID:string,
      /**  Site where the PCID is currently located.  */  
   Plant:string,
      /**  Warehouse where the PCID is currently located.  */  
   WarehouseCode:string,
      /**  Warehouse Bin where the PCID is currently located.  */  
   BinNum:string,
      /**  Warehouse where the PCID return stock needs to be returned to.  */  
   ReturnToWarehouseCode:string,
      /**  Warehouse Bin where the PCID return stock needs to be returned to.  */  
   ReturnToBinNum:string,
      /**  PCID current status.  */  
   PkgControlStatus:string,
      /**  PCID prior status.  */  
   PkgControlPriorStatus:string,
      /**  Label Print Control status.  */  
   LabelPrintControlStatus:string,
      /**  Label Print Control prior status.  */  
   LabelPrintControlPriorStatus:string,
      /**  If false then PCID is a single-level PCID that cannot be associated with a Parent.  */  
   AllowParentPCID:boolean,
      /**  If false then PCID must contain only one PartNum.  */  
   AllowMixedParts:boolean,
      /**  If false then PCID must contain only one LotNum for each Part on the PCID.  */  
   AllowMixedLots:boolean,
      /**  If false then PCID must contain only one UOM per Part on the PCID.  */  
   AllowMixedUOMs:boolean,
      /**  If false then PCID is restricted to containing single-level child PCIDs only and those child PCIDs must contain the same PartNum, Part UOM, or Part Quantity per child PCID.  This is referred to as a Master PCID, otherwise it would be referred to as a MixedMaster PCID.  */  
   AllowMixedChildPCIDs:boolean,
      /**  If false then PCID must contain only one Serial Number per PCID.  */  
   AllowMultipleSerialNumPerPCID:boolean,
      /**  If false then the standard PCID printing logic is used. If true then the Label Print Control logic and rules will apply and be enforced.  */  
   LabelPrintControlled:boolean,
      /**  If false then the number of PCID label prints will not be tracked.  */  
   LabelPrintCounter:boolean,
      /**  If false then PkgControlHeader and PkgControlItem cannot be voided or deleted.  */  
   AllowVoids:boolean,
      /**  If false then PkgControlHeader and PkgControlItem cannot be deleted.  */  
   AllowDeletes:boolean,
      /**  If true then PkgControlHeader and PkgControlItem will be written to history tables and removed from the maintenance tables on void, delete or close/collapse.  */  
   ArchivePCIDHistory:boolean,
      /**  Unique packaging code assigned by the user.  */  
   PkgCode:string,
      /**  User defined code which uniquely identifies the UOM for length, width, and height.  */  
   LWHDimensionUOM:string,
      /**  Length dimension.  */  
   Length:number,
      /**  Width dimension.  */  
   Width:number,
      /**  Height dimension.  */  
   Height:number,
      /**  User defined code which uniquely identifies the UOM for volume.  */  
   VolumeUOM:string,
      /**  Volume.  */  
   Volume:number,
      /**  User defined code which uniquely identifies the UOM for weight.  */  
   WeightUOM:string,
      /**  Maximum Weight.  */  
   MaximumWeight:number,
      /**  Calculated Weight.  */  
   CalculatedWeight:number,
      /**  The total weight of the parts and the container combined.  */  
   TotalWeight:number,
      /**  Maximum number of PCIDs allowed if vertically stacked.  */  
   MaximumStack:number,
      /**  Position Sequence within a parent PCID.  */  
   PositionSeq:number,
      /**  Trailer ID.  */  
   TrailerID:string,
      /**  Bond or Security Seal ID.  */  
   SecuritySealID:string,
      /**  Raw PCID as scanned or generated.  */  
   RawPCIDLicensePlate:string,
      /**  GS1-128 as generated by the Legal Number process.  GS1-128 supersedes the former UCC/EAN128 standards.  */  
   GS1128:string,
      /**  For a static PCID, each time the PCID is collapsed this counter is incremented, and the collapse counter is stamped on any PartTran records generated throughout the life of the PCID.  */  
   PkgControlCollapseCounter:number,
      /**  System date and time when the row was created.  */  
   CreatedDate:string,
      /**  The user ID that created this row.  */  
   CreatedBy:string,
      /**  System date and time when the row was last updated.  */  
   UpdatedDate:string,
      /**  The user ID that last updated this row.  */  
   UpdatedBy:string,
      /**  Last PCID Scanned.  */  
   LastPCIDScanned:string,
      /**  Number of next level down child PCIDs associated to this PCID.  */  
   NumberOfPCIDs:number,
      /**  Flag used to fire the auto print rule that will print the labels.  */  
   AutoPrint:boolean,
      /**  System date and time when the row was created.  */  
   LPCCreatedDate:string,
      /**  The user ID that created this record.  */  
   LPCCreatedBy:string,
      /**  Printer ID that printed the label.  */  
   LPCPrinterID:string,
      /**  User that printed the label.  */  
   LPCPrintedBy:string,
      /**  Label feature. Displays what transaction the label was printed from.  */  
   LPCPrintedFromTx:string,
      /**  Ad Hoc feature. Displays what transaction type the label was printed from.  */  
   LPCPrintedFromTxType:string,
      /**  The job for which the label was printed.  */  
   LPCJobNum:string,
      /**  The operation sequence for which the label was printed.  */  
   LPCOprSeq:number,
      /**  The assembly sequence for which the label was printed.  */  
   LPCAssemblySeq:number,
      /**  Shift that the label was created on or shift entered in Ad Hoc print program.  */  
   LPCShift:number,
      /**  Operator who created the label if printed from MES, Labor Reporting employee if printed from Ad Hoc Manufacturing Backup, or blank otherwise.  */  
   LPCOperatorEmpID:string,
      /**  Original Source PCID for repack. This field will be populated with the source container PCID when assigning a repack label.  */  
   OriginalSourcePCID:string,
      /**  This field will be populated with the new PCID that replaced this PCID when using the overlay feature.  */  
   OverlaidByPCID:string,
      /**  Set to True when PCID has been overlaid using the overlay feature.  */  
   Overlaid:boolean,
      /**  Partial Container – set to true when the container is created from the Ad Hoc – Partial program.  */  
   ContainerPartial:boolean,
      /**  If true the container was repacked.  */  
   ContainerRepacked:boolean,
      /**  If true the container used is a returnable container.  */  
   ContainerReturnable:boolean,
      /**  Our Vendor ID for the Customer being Shipped To.  */  
   OurSupplierCode:string,
      /**  Site Name.  */  
   PlantName:string,
      /**  Site Address line 1.  */  
   PlantAddress1:string,
      /**  Site Address line 2.  */  
   PlantAddress2:string,
      /**  Site Address line 3.  */  
   PlantAddress3:string,
      /**  Site City.  */  
   PlantCity:string,
      /**  Site State.  */  
   PlantState:string,
      /**  Site Zip.  */  
   PlantZip:string,
      /**  Site Country Number.  */  
   PlantCountryNum:number,
      /**  Site Country Description.  */  
   PlantCountryDesc:string,
      /**  Site Phone.  */  
   PlantPhone:string,
      /**  Pack Number if applicable.  */  
   PackNum:number,
      /**  Ship To Customer Container Part Number.  */  
   CustContainerPartNum:string,
      /**  EDI Ship To Number populated with the final destination if shipping to an Intermediate Consignee, otherwise an actual ShipToNum.  */  
   EDIShipToNum:string,
      /**  Ship To Number.  */  
   ShipToNum:string,
      /**  Name of the Ship To that the PCID is going to.  */  
   ShipToName:string,
      /**  Address line 1 of the Ship To that the PCID is going to.  */  
   ShipToAddress1:string,
      /**  Address line 2 of the Ship To that the PCID is going to.  */  
   ShipToAddress2:string,
      /**  Address line 3 of the Ship To that the PCID is going to.  */  
   ShipToAddress3:string,
      /**  City of the Ship To that the PCID is going to.  */  
   ShipToCity:string,
      /**  State of the Ship To that the PCID is going to.  */  
   ShipToState:string,
      /**  Zip of the Ship To that the PCID is going to.  */  
   ShipToZip:string,
      /**  Country number of the Ship To that the PCID is going to.  */  
   ShipToCountryNum:number,
      /**  Country of the Ship To that the PCID is going to.  */  
   ShipToCountryDesc:string,
      /**  The dock that the parts should be shipped to.  */  
   ShipToDock:string,
      /**  The Internal PartNum for the Package Code.  */  
   PkgCodePartNum:string,
      /**  Vendor Number.  */  
   VendorNum:number,
      /**  Vendor ID.  */  
   VendorID:string,
      /**  Vendor Purchase Point.  */  
   VendorPurPoint:string,
      /**  Vendor Address line 1.  */  
   VendorAddress1:string,
      /**  Vendor Address line 2.  */  
   VendorAddress2:string,
      /**  Vendor Address line 3.  */  
   VendorAddress3:string,
      /**  Vendor City.  */  
   VendorCity:string,
      /**  Vendor State.  */  
   VendorState:string,
      /**  Vendor Zip.  */  
   VendorZip:string,
      /**  Vendor Country Number.  */  
   VendorCountryNum:number,
      /**  Vendor Country Description.  */  
   VendorCountryDesc:string,
      /**  Our Dock ID.  */  
   OurDock:string,
      /**  Value to display on package control label.  */  
   LabelValue01:string,
      /**  Value to display on package control label.  */  
   LabelValue02:string,
      /**  Value to display on package control label.  */  
   LabelValue03:string,
      /**  Value to display on package control label.  */  
   LabelValue04:string,
      /**  Value to display on package control label.  */  
   LabelValue05:string,
      /**  Value to display on package control label.  */  
   LabelValue06:string,
      /**  Value to display on package control label.  */  
   LabelValue07:string,
      /**  Value to display on package control label.  */  
   LabelValue08:string,
      /**  Value to display on package control label.  */  
   LabelValue09:string,
      /**  Value to display on package control label.  */  
   LabelValue10:string,
      /**  Value to display on package control label.  */  
   LabelValue11:string,
      /**  Value to display on package control label.  */  
   LabelValue12:string,
      /**  Value to display on package control label.  */  
   LabelValue13:string,
      /**  Value to display on package control label.  */  
   LabelValue14:string,
      /**  Value to display on package control label.  */  
   LabelValue15:string,
      /**  Value to display on package control label.  */  
   LabelValue16:string,
      /**  Value to display on package control label.  */  
   LabelValue17:string,
      /**  Value to display on package control label.  */  
   LabelValue18:string,
      /**  Value to display on package control label.  */  
   LabelValue19:string,
      /**  Value to display on package control label.  */  
   LabelValue20:string,
      /**  Value to display on package control label.  */  
   LabelValue21:string,
      /**  Value to display on package control label.  */  
   LabelValue22:string,
      /**  Value to display on package control label.  */  
   LabelValue23:string,
      /**  Value to display on package control label.  */  
   LabelValue24:string,
      /**  Value to display on package control label.  */  
   LabelValue25:string,
      /**  Value to display on package control label.  */  
   LabelValue26:string,
      /**  Value to display on package control label.  */  
   LabelValue27:string,
      /**  Value to display on package control label.  */  
   LabelValue28:string,
      /**  Value to display on package control label.  */  
   LabelValue29:string,
      /**  Value to display on package control label.  */  
   LabelValue30:string,
      /**  Reserved for development use.  */  
   PkgControlCharacter01:string,
      /**  Reserved for development use.  */  
   PkgControlCharacter02:string,
      /**  Reserved for development use.  */  
   PkgControlCharacter03:string,
      /**  Reserved for development use.  */  
   PkgControlCharacter04:string,
      /**  Reserved for development use.  */  
   PkgControlCharacter05:string,
      /**  Reserved for development use.  */  
   PkgControlDate01:string,
      /**  Reserved for development use.  */  
   PkgControlDate02:string,
      /**  Reserved for development use.  */  
   PkgControlBoolean01:boolean,
      /**  Reserved for development use.  */  
   PkgControlBoolean02:boolean,
      /**  Reserved for development use.  */  
   PkgControlInteger01:number,
      /**  Reserved for development use.  */  
   PkgControlInteger02:number,
      /**  Reserved for development use.  */  
   PkgControlDecimal01:number,
      /**  Reserved for development use.  */  
   PkgControlDecimal02:number,
      /**  Package Control Type.  Valid values are “Static” or “Dynamic”.  */  
   PkgControlType:string,
      /**  Package Control ID Code.  */  
   PkgControlIDCode:string,
      /**  External Length dimension.  */  
   ExternalLength:number,
      /**  External Width dimension.  */  
   ExternalWidth:number,
      /**  External Height dimension.  */  
   ExternalHeight:number,
      /**  External Volume.  */  
   ExternalVolume:number,
      /**  Tare Weight.  */  
   TareWeight:number,
      /**  Incremental tally of number of times PCID label has been printed.  */  
   LabelPrintCount:number,
      /**  Indicates if the expendable PCID will be tracked.  */  
   TrackExpendable:boolean,
      /**  Indicates if the returnable PCID will be tracked.  */  
   TrackReturnable:boolean,
      /**  Label Type.  */  
   LabelType:string,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  Ship To Customer Number.  */  
   CustNum:number,
      /**  Indicates if the PCID is expendable.  */  
   ContainerExpendable:boolean,
      /**  Ship To Customer ID.  */  
   CustID:string,
      /**  Ship To Customer Name.  */  
   CustName:string,
      /**  Vendor Name.  */  
   VendorName:string,
      /**  Vendor Purchase Point Name.  */  
   VendorPPName:string,
      /**  True if the inventory referenced during Adhoc PCID had not yet been received and the PCID needed to be staged.  */  
   AdhocStagedInventory:boolean,
      /**  UpdatedByEmpID  */  
   UpdatedByEmpID:string,
      /**  Raw Barcode Scan prior to execution of any extract logic.  */  
   RawBarcodeScan:string,
      /**  OutboundContainer  */  
   OutboundContainer:boolean,
      /**  PkgControlStatus value prior to being added to a pack.  */  
   BeforePackPkgControlStatus:string,
      /**  LabelPrintControlStatus value prior to being added to a pack.  */  
   BeforePackLabelPrintControlStatus:string,
      /**  To indicate the source process when a PCID was added to a pack.  */  
   PackedFromSource:string,
      /**  Date last counted.  Updated during the cycle count Posting Process.  */  
   LastCountedDate:string,
      /**  TFPackNum  */  
   TFPackNum:number,
      /**  Child PCID count  */  
   ChildPCIDCount:number,
      /**  Indicates if EnableCboReasonCode control should be Enabled.  */  
   EnableCboReasonCode:boolean,
      /**  if the PkgControlID is expendable  */  
   Expendable:boolean,
   ExtensionDigit:number,
      /**  Used for Handheld, this field will determine if the ASN (Advanced Ship Notice) has been sent/printed  */  
   HHASN:boolean,
   HHItemIUM:string,
   HHItemPartNum:string,
      /**  Used for Handheld.  */  
   HHItemQuantity:number,
   HHItemRevisionNum:string,
      /**  Used for HandHeld, it can be either PkgControlHeader.LabelPrintControlStatus OR PkgControlHeader.PkgControlStatus  */  
   HHLabelStatus:string,
      /**   Used for handHeld             
If PkgControlHeader.PkgControlType = Static then PkgControlHeader.PackNum
If PkgControlHeader.PkgControlType = Dynamic then PkgControlItem.PackNum  */  
   HHPackSlip:number,
      /**  Used for HandHeld, It could contains a list of PackNum from the children  */  
   HHPackSlipList:string,
   LWHDimUOM:string,
      /**  Warehouse Bin where the Parent PCID is currently located.  */  
   ParentBinNum:string,
      /**  System date and time when the row was created.  */  
   ParentCreatedDate:string,
      /**  Ship To Customer Container Part Number.  */  
   ParentCustContainerPartNum:string,
      /**  Parent Ship To Customer ID.  */  
   ParentCustID:string,
      /**  If false then the standard PCID printing logic is used. If true then the Label Print Control logic and rules will apply and be enforced.  */  
   ParentLabelPrintControlled:boolean,
      /**  Label Print Control status.  */  
   ParentLabelPrintControlStatus:string,
      /**  Label Type.  */  
   ParentLabelType:string,
      /**  Number of next level down child PCIDs associated to this PCID.  */  
   ParentNumberOfPCIDs:number,
      /**  Pack Number if applicable.  */  
   ParentPackNum:number,
      /**  Parent Package Control Identification Number  */  
   ParentPCID:string,
      /**  Unique packaging code assigned by the user.  */  
   ParentPkgCode:string,
      /**  The Internal PartNum for the Package Code.  */  
   ParentPkgCodePartNum:string,
      /**  PCID current status.  */  
   ParentPkgControlStatus:string,
      /**  Package Control Type.  Valid values are “Static” or “Dynamic”.  */  
   ParentPkgControlType:string,
      /**  Site where the Parent PCID is currently located.  */  
   ParentPlant:string,
      /**  Site Name.  */  
   ParentPlantName:string,
      /**  Parent Ship To Number.  */  
   ParentShipToNum:string,
      /**  Warehouse where the Parent PCID is currently located.  */  
   ParentWarehouseCode:string,
   ParentWhseDesc:string,
   PartDesc:string,
   PkgCodeDesc:string,
   PkgType:string,
      /**  Reason Code  */  
   ReasonCode:string,
   ResCodeIn:string,
   ResCodeOut:string,
   RTWhseDesc:string,
      /**  Ship To Container Part ID  */  
   ShipToContainerPartID:string,
      /**  Transaction document type  */  
   TranDocTypeID:string,
   WhseDesc:string,
      /**  Adjust Inventory  */  
   AdjustInventory:boolean,
      /**  Container UOM  */  
   ContainerUOM:string,
   DisableReasonCode:boolean,
      /**  Indicates if BtnVoidPCIDInv control should be Enabled.  */  
   EnableBtnVoidPCIDInv:boolean,
   BitFlag:number,
   BinDescription:string,
   WarehouseDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PkgControlIDListTableset{
   PkgControlHeaderList:Erp_Tablesets_PkgControlHeaderListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_PkgControlIDTableset{
   PkgControlHeader:Erp_Tablesets_PkgControlHeaderRow[],
   PkgControlCustPartNum:Erp_Tablesets_PkgControlCustPartNumRow[],
   PCLabelValues:Erp_Tablesets_PCLabelValuesRow[],
   PkgControlItem:Erp_Tablesets_PkgControlItemRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_PkgControlItemRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Package Control Identification Number  */  
   PCID:string,
      /**  PCID Item Sequence  */  
   PCIDItemSeq:number,
      /**  The PCID of the item in this PCID.  */  
   ItemPCID:string,
      /**  The Part Number of the item in this PCID.  */  
   ItemPartNum:string,
      /**  The Revision Number of the item in this PCID.  */  
   ItemRevisionNum:string,
      /**  The Part Description of the item in this PCID.  */  
   ItemPartDesc:string,
      /**  The Lot Number of the item in this PCID.  */  
   ItemLotNum:string,
      /**  The Inventory UOM of the item in this PCID.  */  
   ItemIUM:string,
      /**  The Quantity of the item in this PCID.  */  
   ItemQuantity:number,
      /**  Site Identifier.  */  
   Plant:string,
      /**  Demand Type.  */  
   DemandType:string,
      /**  Order Number of the demand.  */  
   OrderNum:number,
      /**  Order Line Number of the demand.  */  
   OrderLine:number,
      /**  Order Release Number of the demand.  */  
   OrderRelNum:number,
      /**  Job Number of the demand.  */  
   JobNum:string,
      /**  Assembly Sequence Number of the demand.  */  
   AssemblySeq:number,
      /**  Material Sequence Number of the demand.  */  
   MtlSeq:number,
      /**  Transfer Order Number of the demand.  */  
   TFOrdNum:string,
      /**  Transfer Order Line of the demand.  */  
   TFOrdLine:number,
      /**  Pack Number if applicable.  */  
   PackNum:number,
      /**  Pack Line Number if applicable.  */  
   PackLine:number,
      /**  Ship To Customer Part Number.  */  
   CustPartNum:string,
      /**  Ship To Customer Part Revision.  */  
   CustPartRev:string,
      /**  The PO number that these parts were created against.  */  
   CustPONum:string,
      /**  Engineering Alert to display on the label.  */  
   CustShipToEngineerAlert:string,
      /**  Safety Indicator to display on the label.  */  
   SafetyIndicator:boolean,
      /**  The Internal PartNum for the Package Code.  */  
   PkgCodePartNum:string,
      /**  Purchase Order Type.  */  
   VendorPOType:string,
      /**  Purchase Order Number.  */  
   VendorPONum:number,
      /**  Purchase Order Line Number.  */  
   VendorPOLine:number,
      /**  Purchase Order Release Number.  */  
   VendorPORelNum:number,
      /**  Supplier Part Number.  */  
   VendorPartNum:string,
      /**  Supplier Unit of Measure.  */  
   VendorUOM:string,
      /**  Supplier Quantity.  */  
   VendorQty:number,
      /**  Receipt Packing Slip.  */  
   ReceiptPackSlip:string,
      /**  Receipt Type.  */  
   ReceiptType:string,
      /**  Receipt Date.  */  
   ReceiptDate:string,
      /**  Receipt UOM.  */  
   ReceiptUOM:string,
      /**  Receipt Quantity.  */  
   ReceiptQty:number,
      /**  RMA Number.  */  
   RMANum:number,
      /**  RMA Line.  */  
   RMALine:number,
      /**  Reserved for development use.  */  
   PkgControlCharacter01:string,
      /**  Reserved for development use.  */  
   PkgControlCharacter02:string,
      /**  Reserved for development use.  */  
   PkgControlCharacter03:string,
      /**  Reserved for development use.  */  
   PkgControlCharacter04:string,
      /**  Reserved for development use.  */  
   PkgControlCharacter05:string,
      /**  Reserved for development use.  */  
   PkgControlDate01:string,
      /**  Reserved for development use.  */  
   PkgControlDate02:string,
      /**  Reserved for development  */  
   PkgControlBoolean01:boolean,
      /**  Reserved for development use.  */  
   PkgControlBoolean02:boolean,
      /**  Reserved for development use.  */  
   PkgControlDecimal01:number,
      /**  Reserved for development use.  */  
   PkgControlDecimal02:number,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  Set to INVOICED when invoice created, set to POSTED when invoice is posted.  */  
   ShipmentInvoicedPosted:string,
      /**  The job number on which the quantity on this record were produced  */  
   SupplyJobNum:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   ItemAttributeSetID:number,
      /**  TFPackNum  */  
   TFPackNum:number,
      /**  TFPackLine  */  
   TFPackLine:number,
      /**  Set to true if this PkgControlItem record was created by processing a mtl queue picking record  */  
   ItemPicked:boolean,
      /**  SysRowID of the PartWip to which this item relates. The value is a GUID.  If the item is not WIP, this column is blank.  This value should only ever be populated in a Staging or History PCID, never an Inventory PCID.  */  
   ItemPartWipSysRowID:string,
      /**  Internal flag to distiguish between tracking of issued raw material, and the actual manufactured product.  "R" - Raw Material a part which was issued to the job.  "M" - Manufactured Part. The part that is being manufactured.  */  
   TrackType:string,
      /**  Job operation sequence number that part is related to.  */  
   OprSeq:number,
      /**  Indicates if the WIP has been sent to Non-Conformance.  */  
   InNonConformance:boolean,
      /**  Indicates if the WIP has failed Non-Conformance and has been moved to DMR Processing.  */  
   InDMRProcessing:boolean,
   ChildPCIDOrPart:string,
   CustID:string,
   CustName:string,
      /**  Number of next level down child PCIDs associated to this PCID.  */  
   NumberOfPCIDs:number,
   PackageCode:string,
      /**  Site Name.  */  
   PlantName:string,
      /**  Warehouse where the PCID is currently located.  */  
   WarehouseCode:string,
   WhseDesc:string,
      /**  Warehouse Bin where the PCID is currently located.  */  
   BinNum:string,
      /**  The Full Description of the Attribute Set.  */  
   ItemAttributeSetDescription:string,
      /**  The Short Description of the Attribute Set.  */  
   ItemAttributeSetShortDescription:string,
   ItemPartAttrClassID:string,
   ItemType:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_UpdExtPkgControlIDTableset{
   PkgControlHeader:Erp_Tablesets_PkgControlHeaderRow[],
   PkgControlCustPartNum:Erp_Tablesets_PkgControlCustPartNumRow[],
   PCLabelValues:Erp_Tablesets_PCLabelValuesRow[],
   PkgControlItem:Erp_Tablesets_PkgControlItemRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param pcID
   */  
export interface GetByID_input{
   pcID:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_PkgControlIDTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_PkgControlIDTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_PkgControlIDTableset[],
}

   /** Required : 
      @param WhereClause
      @param PageSize
      @param AbsolutePage
   */  
export interface GetListCoreStageHX_input{
      /**  Whereclause.  */  
   WhereClause:string,
      /**  Page size.  */  
   PageSize:number,
      /**  Absolute page.  */  
   AbsolutePage:number,
}

export interface GetListCoreStageHX_output{
   returnObj:Erp_Tablesets_PkgControlIDListTableset[],
parameters : {
      /**  output parameters  */  
   MorePages:boolean,
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
   returnObj:Erp_Tablesets_PkgControlIDListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param pcID
   */  
export interface GetNewPkgControlCustPartNum_input{
   ds:Erp_Tablesets_PkgControlIDTableset[],
   pcID:string,
}

export interface GetNewPkgControlCustPartNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PkgControlIDTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewPkgControlHeader_input{
   ds:Erp_Tablesets_PkgControlIDTableset[],
}

export interface GetNewPkgControlHeader_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PkgControlIDTableset[],
}
}

   /** Required : 
      @param ds
      @param pcID
   */  
export interface GetNewPkgControlItem_input{
   ds:Erp_Tablesets_PkgControlIDTableset[],
   pcID:string,
}

export interface GetNewPkgControlItem_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PkgControlIDTableset[],
}
}

   /** Required : 
      @param ipPackNum
   */  
export interface GetPCIDList_input{
      /**  Packnum  */  
   ipPackNum:number,
}

export interface GetPCIDList_output{
   returnObj:Erp_Tablesets_PkgControlIDListTableset[],
}

   /** Required : 
      @param whereClausePkgControlHeader
      @param whereClausePkgControlCustPartNum
      @param whereClausePCLabelValues
      @param whereClausePkgControlItem
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClausePkgControlHeader:string,
   whereClausePkgControlCustPartNum:string,
   whereClausePCLabelValues:string,
   whereClausePkgControlItem:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_PkgControlIDTableset[],
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
      @param ipPCID
      @param ds
   */  
export interface OnChangePCID_input{
      /**  Proposed PCID value  */  
   ipPCID:string,
   ds:Erp_Tablesets_PkgControlIDTableset[],
}

export interface OnChangePCID_output{
   returnObj:string,
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PkgControlIDTableset[],
}
}

   /** Required : 
      @param ipPCID
   */  
export interface PCIDExists_input{
      /**  PCID  */  
   ipPCID:string,
}

export interface PCIDExists_output{
      /**  bool  */  
   returnObj:boolean,
}

export interface PasswordConfigured_output{
   returnObj:boolean,
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtPkgControlIDTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtPkgControlIDTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_PkgControlIDTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PkgControlIDTableset[],
}
}

   /** Required : 
      @param WarehouseCode
      @param PlantID
   */  
export interface WarehseEnforcePkgControlRulesExists_input{
      /**  WarehouseCode to search for  */  
   WarehouseCode:string,
      /**  Current PlantID  */  
   PlantID:string,
}

export interface WarehseEnforcePkgControlRulesExists_output{
      /**  True if Warehouse exists  */  
   returnObj:boolean,
}

   /** Required : 
      @param WarehouseCode
      @param BinNum
   */  
export interface WhseBinExists_input{
      /**  Current WarehouseCode  */  
   WarehouseCode:string,
      /**  BinNum to search for  */  
   BinNum:string,
}

export interface WhseBinExists_output{
      /**  True if WhseBin exists  */  
   returnObj:boolean,
}
