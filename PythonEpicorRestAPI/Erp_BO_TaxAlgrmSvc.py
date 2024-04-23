import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.TaxAlgrmSvc
# Description: Add your summary for this object here
# Version: v1



#########################################################################
# OData methods:
#########################################################################
async def getServiceDocument(epicorHeaders = None):
   """  
   Summary: Get service document
   Description: Get service document for the service
   OperationID: GetServiceDocument
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => application/json
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaxAlgrmSvc/",headers=creds) as resp:
           return await resp.json()

async def get_metadata(epicorHeaders = None):
   """  
   Summary: Get metadata document
   Description: Get service ODATA metadata in XML format
   OperationID: GetMetadata
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: Returns metadata document => content
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaxAlgrmSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_TaxAlgrms(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get TaxAlgrms items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_TaxAlgrms
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TaxAlgrmRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaxAlgrmSvc/TaxAlgrms",headers=creds) as resp:
           return await resp.json()

async def post_TaxAlgrms(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_TaxAlgrms
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.TaxAlgrmRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.TaxAlgrmRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaxAlgrmSvc/TaxAlgrms", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_TaxAlgrms_Company_Algorithm(Company, Algorithm, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the TaxAlgrm item
   Description: Calls GetByID to retrieve the TaxAlgrm item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TaxAlgrm
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Algorithm: Desc: Algorithm   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TaxAlgrmRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaxAlgrmSvc/TaxAlgrms(" + Company + "," + Algorithm + ")",headers=creds) as resp:
           return await resp.json()

async def patch_TaxAlgrms_Company_Algorithm(Company, Algorithm, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update TaxAlgrm for the service
   Description: Calls UpdateExt to update TaxAlgrm. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_TaxAlgrm
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Algorithm: Desc: Algorithm   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.TaxAlgrmRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.TaxAlgrmSvc/TaxAlgrms(" + Company + "," + Algorithm + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_TaxAlgrms_Company_Algorithm(Company, Algorithm, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete TaxAlgrm item
   Description: Call UpdateExt to delete TaxAlgrm item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_TaxAlgrm
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Algorithm: Desc: Algorithm   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.TaxAlgrmSvc/TaxAlgrms(" + Company + "," + Algorithm + ")",headers=creds) as resp:
           return await resp.json()

async def get_TaxAlgrms_Company_Algorithm_TaxAlDtls(Company, Algorithm, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get TaxAlDtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_TaxAlDtls1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Algorithm: Desc: Algorithm   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TaxAlDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaxAlgrmSvc/TaxAlgrms(" + Company + "," + Algorithm + ")/TaxAlDtls",headers=creds) as resp:
           return await resp.json()

async def get_TaxAlgrms_Company_Algorithm_TaxAlDtls_Company_Algorithm_LineNum(Company, Algorithm, LineNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the TaxAlDtl item
   Description: Calls GetByID to retrieve the TaxAlDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TaxAlDtl1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Algorithm: Desc: Algorithm   Required: True   Allow empty value : True
      :param LineNum: Desc: LineNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TaxAlDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaxAlgrmSvc/TaxAlgrms(" + Company + "," + Algorithm + ")/TaxAlDtls(" + Company + "," + Algorithm + "," + LineNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_TaxAlDtls(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get TaxAlDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_TaxAlDtls
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TaxAlDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaxAlgrmSvc/TaxAlDtls",headers=creds) as resp:
           return await resp.json()

async def post_TaxAlDtls(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_TaxAlDtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.TaxAlDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.TaxAlDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaxAlgrmSvc/TaxAlDtls", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_TaxAlDtls_Company_Algorithm_LineNum(Company, Algorithm, LineNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the TaxAlDtl item
   Description: Calls GetByID to retrieve the TaxAlDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TaxAlDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Algorithm: Desc: Algorithm   Required: True   Allow empty value : True
      :param LineNum: Desc: LineNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TaxAlDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaxAlgrmSvc/TaxAlDtls(" + Company + "," + Algorithm + "," + LineNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_TaxAlDtls_Company_Algorithm_LineNum(Company, Algorithm, LineNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update TaxAlDtl for the service
   Description: Calls UpdateExt to update TaxAlDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_TaxAlDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Algorithm: Desc: Algorithm   Required: True   Allow empty value : True
      :param LineNum: Desc: LineNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.TaxAlDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.TaxAlgrmSvc/TaxAlDtls(" + Company + "," + Algorithm + "," + LineNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_TaxAlDtls_Company_Algorithm_LineNum(Company, Algorithm, LineNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete TaxAlDtl item
   Description: Call UpdateExt to delete TaxAlDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_TaxAlDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Algorithm: Desc: Algorithm   Required: True   Allow empty value : True
      :param LineNum: Desc: LineNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.TaxAlgrmSvc/TaxAlDtls(" + Company + "," + Algorithm + "," + LineNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_List(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetList for the service
   Description: Get list of items<div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetList
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TaxAlgrmListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaxAlgrmSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseTaxAlgrm, whereClauseTaxAlDtl, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseTaxAlgrm=" + whereClauseTaxAlgrm
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseTaxAlDtl=" + whereClauseTaxAlDtl
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "pageSize=" + pageSize
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "absolutePage=" + absolutePage

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaxAlgrmSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(algorithm, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "algorithm=" + algorithm

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaxAlgrmSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetList(whereClause, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetList
   Description: Returns a list of rows that satisfy the where clause.
   OperationID: Get_GetList
      :param whereClause: Desc: An expression used to filter the rows. Can be left blank for all rows.   Required: True   Allow empty value : True
      :param pageSize: Desc: The maximum number of rows to return. Leave as zero for no maximum.   Required: True
      :param absolutePage: Desc: Page of rows to return.   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClause=" + whereClause
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "pageSize=" + pageSize
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "absolutePage=" + absolutePage

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaxAlgrmSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_ChangeOperand1(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeOperand1
   Description: Update multiple fields when  the Operand1 changes.
   OperationID: ChangeOperand1
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeOperand1_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeOperand1_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaxAlgrmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeOperand2(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeOperand2
   Description: Update multiple fields when  the Operand2 changes.
   OperationID: ChangeOperand2
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeOperand2_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeOperand2_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaxAlgrmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeOperator(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeOperator
   Description: Update multiple fields when  the operator changes.
   OperationID: ChangeOperator
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeOperator_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeOperator_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaxAlgrmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckBaseLine(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckBaseLine
   Description: Uncheck the Base line flag if different line is flagged as BaseLine  .
   OperationID: CheckBaseLine
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckBaseLine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckBaseLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaxAlgrmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckTaxLine(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckTaxLine
   Description: Uncheck the Tax Line flag if different line is flagged as TaxLine.
   OperationID: CheckTaxLine
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckTaxLine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckTaxLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaxAlgrmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateOperand1(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateOperand1
   Description: Validates the value of "Operand1"
   OperationID: ValidateOperand1
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateOperand1_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateOperand1_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaxAlgrmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateOperand2(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateOperand2
   Description: Validates the value of "Operand2"
   OperationID: ValidateOperand2
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateOperand2_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateOperand2_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaxAlgrmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateOperand3(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateOperand3
   Description: Validates the value of "Operand3"
   OperationID: ValidateOperand3
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateOperand3_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateOperand3_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaxAlgrmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateOperand4(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateOperand4
   Description: Validates the value of "Operand4"
   OperationID: ValidateOperand4
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateOperand4_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateOperand4_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaxAlgrmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateOperator(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateOperator
   Description: Validates the value of "Operand2"
   OperationID: ValidateOperator
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateOperator_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateOperator_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaxAlgrmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateTaxCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateTaxCode
   Description: Validates the value of "Operand3TaxCode" and "Operand4TaxCode"
   OperationID: ValidateTaxCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateTaxCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateTaxCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaxAlgrmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCodeDescList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCodeDescList
   Description: To return the CodeDescriptionList values of a given table.field.
   OperationID: GetCodeDescList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCodeDescList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCodeDescList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaxAlgrmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewTaxAlgrm(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewTaxAlgrm
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewTaxAlgrm
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewTaxAlgrm_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewTaxAlgrm_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaxAlgrmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewTaxAlDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewTaxAlDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewTaxAlDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewTaxAlDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewTaxAlDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaxAlgrmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteByID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteByID
   Description: Deletes a row given its ID.
   OperationID: DeleteByID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaxAlgrmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GetBySysRowID(id, epicorHeaders = None):
   """  
   Summary: Invoke method GetBySysRowID
   OperationID: Get_GetBySysRowID
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBySysRowID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "id=" + id

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaxAlgrmSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetBySysRowIDs(ids, epicorHeaders = None):
   """  
   Summary: Invoke method GetBySysRowIDs
   OperationID: Get_GetBySysRowIDs
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBySysRowIDs_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "ids=" + ids

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaxAlgrmSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_Update(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method Update
   Description: Commits the DataSet changes to the data store.
   OperationID: Update
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Update_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Update_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaxAlgrmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateExt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateExt
   Description: Apply input data to service by calling GetByID/GetNew/Update methods.
   OperationID: UpdateExt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateExt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateExt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaxAlgrmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaxAlDtlRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_TaxAlDtlRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaxAlgrmListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_TaxAlgrmListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaxAlgrmRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_TaxAlgrmRow] = obj["value"]
      pass

class Erp_Tablesets_TaxAlDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Algorithm:str = obj["Algorithm"]
      """  Unique ID for algorithm  """  
      self.LineNum:int = obj["LineNum"]
      """  Line Number  """  
      self.Operand1:str = obj["Operand1"]
      """   First operand in equation.  Valid values:
NV - Net Value, GV - Gross Value, SV - Sales Value, TA - Tax Amount before exemptions, TE - Tax Amount after exemptions, Lxx - Result of expression in line xx, PT - Payment Total, PI - Payment Proportion, or a numeric contant  """  
      self.Operator:str = obj["Operator"]
      """  Valid Values: +, -, /, *  (math between Operand 1 and Operand 2), % (Operand 2 % of Operand 1),  >, <, =(compare Operand 1 and 2), TR (calculate tax rate)  """  
      self.Operand2:str = obj["Operand2"]
      """   First operand in equation.  Valid values:
NV - Net Value, GV - Gross Value, SV - Sales Value, TA - Tax Amount before exemptions, TE - Tax Amount after exemptions, Lxx - Result of expression in line xx, PT - Payment Total, PI - Payment Proportion, or a numeric contant  """  
      self.Operand3:str = obj["Operand3"]
      """  If Operand is > or < then a valid Operand is valid  """  
      self.Operand4:str = obj["Operand4"]
      """  If Operand is > or < then a valid Operand is valid  """  
      self.BaseLine:bool = obj["BaseLine"]
      """  If checked the result of this line will be used as the taxable base amount.  Only one line allowed as the BaseLine  """  
      self.TaxLine:bool = obj["TaxLine"]
      """  If checked the result of this line will be used as the tax amount.  Only one line allowed as the TaxLine  """  
      self.Operand3TaxCode:str = obj["Operand3TaxCode"]
      """  If Operand 1 is TE or TA then a SalesTax code is valid  """  
      self.Operand4TaxCode:str = obj["Operand4TaxCode"]
      """  If Operand 2 is TE or TA then a SalesTax code is valid  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.Op2Disabled:bool = obj["Op2Disabled"]
      """  Flag to determine if Operator2 prompt is available for the user  """  
      self.Op3Disabled:bool = obj["Op3Disabled"]
      """  Flag to determine if Operator3 prompt is available for the user  """  
      self.Op4Disabled:bool = obj["Op4Disabled"]
      """  Flag to determine if Operator 4 prompt is available for the user  """  
      self.Op3TaxDisabled:bool = obj["Op3TaxDisabled"]
      """  Flag to determine if Operator3TaxCode  prompt is available for the user  """  
      self.Op4TaxDisabled:bool = obj["Op4TaxDisabled"]
      """  Flag to determine if Operator4TaxCode prompt is available for the user  """  
      self.BitFlag:int = obj["BitFlag"]
      self.Operand3TaxCodeDescription:str = obj["Operand3TaxCodeDescription"]
      self.Operand4TaxCodeDescription:str = obj["Operand4TaxCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TaxAlgrmListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Algorithm:str = obj["Algorithm"]
      """  Unique ID for algorithm  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TaxAlgrmRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Algorithm:str = obj["Algorithm"]
      """  Unique ID for algorithm  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class ChangeOperand1_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_TaxAlgrmTableset] = obj["ds"]
      pass

class ChangeOperand1_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TaxAlgrmTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeOperand2_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_TaxAlgrmTableset] = obj["ds"]
      pass

class ChangeOperand2_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TaxAlgrmTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeOperator_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_TaxAlgrmTableset] = obj["ds"]
      pass

class ChangeOperator_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TaxAlgrmTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckBaseLine_input:
   """ Required : 
   iBaseLine
   """  
   def __init__(self, obj):
      self.iBaseLine:bool = obj["iBaseLine"]
      """  The proposed flag for Base Line  """  
      pass

class CheckBaseLine_output:
   def __init__(self, obj):
      pass

class CheckTaxLine_input:
   """ Required : 
   iTaxLine
   """  
   def __init__(self, obj):
      self.iTaxLine:bool = obj["iTaxLine"]
      """  The proposed flag for Tax Line  """  
      pass

class CheckTaxLine_output:
   def __init__(self, obj):
      pass

class DeleteByID_input:
   """ Required : 
   algorithm
   """  
   def __init__(self, obj):
      self.algorithm:str = obj["algorithm"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_TaxAlDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Algorithm:str = obj["Algorithm"]
      """  Unique ID for algorithm  """  
      self.LineNum:int = obj["LineNum"]
      """  Line Number  """  
      self.Operand1:str = obj["Operand1"]
      """   First operand in equation.  Valid values:
NV - Net Value, GV - Gross Value, SV - Sales Value, TA - Tax Amount before exemptions, TE - Tax Amount after exemptions, Lxx - Result of expression in line xx, PT - Payment Total, PI - Payment Proportion, or a numeric contant  """  
      self.Operator:str = obj["Operator"]
      """  Valid Values: +, -, /, *  (math between Operand 1 and Operand 2), % (Operand 2 % of Operand 1),  >, <, =(compare Operand 1 and 2), TR (calculate tax rate)  """  
      self.Operand2:str = obj["Operand2"]
      """   First operand in equation.  Valid values:
NV - Net Value, GV - Gross Value, SV - Sales Value, TA - Tax Amount before exemptions, TE - Tax Amount after exemptions, Lxx - Result of expression in line xx, PT - Payment Total, PI - Payment Proportion, or a numeric contant  """  
      self.Operand3:str = obj["Operand3"]
      """  If Operand is > or < then a valid Operand is valid  """  
      self.Operand4:str = obj["Operand4"]
      """  If Operand is > or < then a valid Operand is valid  """  
      self.BaseLine:bool = obj["BaseLine"]
      """  If checked the result of this line will be used as the taxable base amount.  Only one line allowed as the BaseLine  """  
      self.TaxLine:bool = obj["TaxLine"]
      """  If checked the result of this line will be used as the tax amount.  Only one line allowed as the TaxLine  """  
      self.Operand3TaxCode:str = obj["Operand3TaxCode"]
      """  If Operand 1 is TE or TA then a SalesTax code is valid  """  
      self.Operand4TaxCode:str = obj["Operand4TaxCode"]
      """  If Operand 2 is TE or TA then a SalesTax code is valid  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.Op2Disabled:bool = obj["Op2Disabled"]
      """  Flag to determine if Operator2 prompt is available for the user  """  
      self.Op3Disabled:bool = obj["Op3Disabled"]
      """  Flag to determine if Operator3 prompt is available for the user  """  
      self.Op4Disabled:bool = obj["Op4Disabled"]
      """  Flag to determine if Operator 4 prompt is available for the user  """  
      self.Op3TaxDisabled:bool = obj["Op3TaxDisabled"]
      """  Flag to determine if Operator3TaxCode  prompt is available for the user  """  
      self.Op4TaxDisabled:bool = obj["Op4TaxDisabled"]
      """  Flag to determine if Operator4TaxCode prompt is available for the user  """  
      self.BitFlag:int = obj["BitFlag"]
      self.Operand3TaxCodeDescription:str = obj["Operand3TaxCodeDescription"]
      self.Operand4TaxCodeDescription:str = obj["Operand4TaxCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TaxAlgrmListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Algorithm:str = obj["Algorithm"]
      """  Unique ID for algorithm  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TaxAlgrmListTableset:
   def __init__(self, obj):
      self.TaxAlgrmList:list[Erp_Tablesets_TaxAlgrmListRow] = obj["TaxAlgrmList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_TaxAlgrmRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Algorithm:str = obj["Algorithm"]
      """  Unique ID for algorithm  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TaxAlgrmTableset:
   def __init__(self, obj):
      self.TaxAlgrm:list[Erp_Tablesets_TaxAlgrmRow] = obj["TaxAlgrm"]
      self.TaxAlDtl:list[Erp_Tablesets_TaxAlDtlRow] = obj["TaxAlDtl"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtTaxAlgrmTableset:
   def __init__(self, obj):
      self.TaxAlgrm:list[Erp_Tablesets_TaxAlgrmRow] = obj["TaxAlgrm"]
      self.TaxAlDtl:list[Erp_Tablesets_TaxAlDtlRow] = obj["TaxAlDtl"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   algorithm
   """  
   def __init__(self, obj):
      self.algorithm:str = obj["algorithm"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_TaxAlgrmTableset] = obj["returnObj"]
      pass

class GetBySysRowID_input:
   """ Required : 
   id
   """  
   def __init__(self, obj):
      self.id:str = obj["id"]
      pass

class GetBySysRowID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_TaxAlgrmTableset] = obj["returnObj"]
      pass

class GetBySysRowIDs_input:
   """ Required : 
   ids
   """  
   def __init__(self, obj):
      self.ids:str = obj["ids"]
      pass

class GetBySysRowIDs_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_TaxAlgrmTableset] = obj["returnObj"]
      pass

class GetCodeDescList_input:
   """ Required : 
   tableName
   fieldName
   """  
   def __init__(self, obj):
      self.tableName:str = obj["tableName"]
      self.fieldName:str = obj["fieldName"]
      pass

class GetCodeDescList_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetList_input:
   """ Required : 
   whereClause
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      """  An expression used to filter the rows. Can be left blank for all rows.  """  
      self.pageSize:int = obj["pageSize"]
      """  The maximum number of rows to return. Leave as zero for no maximum.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Page of rows to return.  """  
      pass

class GetList_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_TaxAlgrmListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewTaxAlDtl_input:
   """ Required : 
   ds
   algorithm
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_TaxAlgrmTableset] = obj["ds"]
      self.algorithm:str = obj["algorithm"]
      pass

class GetNewTaxAlDtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TaxAlgrmTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewTaxAlgrm_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_TaxAlgrmTableset] = obj["ds"]
      pass

class GetNewTaxAlgrm_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TaxAlgrmTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseTaxAlgrm
   whereClauseTaxAlDtl
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseTaxAlgrm:str = obj["whereClauseTaxAlgrm"]
      self.whereClauseTaxAlDtl:str = obj["whereClauseTaxAlDtl"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_TaxAlgrmTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class Ice_BOUpdErrorRow:
   def __init__(self, obj):
      self.TableName:str = obj["TableName"]
      self.ErrorLevel:str = obj["ErrorLevel"]
      self.ErrorType:str = obj["ErrorType"]
      self.ErrorText:str = obj["ErrorText"]
      self.ErrorSysRowID:str = obj["ErrorSysRowID"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      pass

class Ice_BOUpdErrorTableset:
   def __init__(self, obj):
      self.BOUpdError:list[Ice_BOUpdErrorRow] = obj["BOUpdError"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Extensions_ExtensionRow:
   def __init__(self, obj):
      self.ColumnValues:object
      self.RowMod:str = obj["RowMod"]
      self.SysRowID:str = obj["SysRowID"]
      pass

class Ice_Extensions_ExtensionTableColumn:
   def __init__(self, obj):
      self.ColumnName:str = obj["ColumnName"]
      self.ColumnType:str = obj["ColumnType"]
      pass

class Ice_Extensions_ExtensionTableData:
   def __init__(self, obj):
      self.Table:list[Ice_Extensions_ExtensionRow] = obj["Table"]
      self.SystemCode:str = obj["SystemCode"]
      self.TableName:str = obj["TableName"]
      self.Columns:list[Ice_Extensions_ExtensionTableColumn] = obj["Columns"]
      self.PrimaryKeyColumns:str = obj["PrimaryKeyColumns"]
      self.PeerTableSystemCode:str = obj["PeerTableSystemCode"]
      self.PeerTableName:str = obj["PeerTableName"]
      pass

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtTaxAlgrmTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtTaxAlgrmTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_TaxAlgrmTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TaxAlgrmTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateOperand1_input:
   """ Required : 
   proposedOperand1
   iLine
   iAlgorithm
   """  
   def __init__(self, obj):
      self.proposedOperand1:str = obj["proposedOperand1"]
      """  Proposed Operand1 value  """  
      self.iLine:int = obj["iLine"]
      """  Line Number  """  
      self.iAlgorithm:str = obj["iAlgorithm"]
      """  Algorithm code  """  
      pass

class ValidateOperand1_output:
   def __init__(self, obj):
      pass

class ValidateOperand2_input:
   """ Required : 
   proposedOperand2
   iLine
   iAlgorithm
   iOperator
   """  
   def __init__(self, obj):
      self.proposedOperand2:str = obj["proposedOperand2"]
      """  Proposed Operand2 value  """  
      self.iLine:int = obj["iLine"]
      """  Line Number  """  
      self.iAlgorithm:str = obj["iAlgorithm"]
      """  Algorithm code  """  
      self.iOperator:str = obj["iOperator"]
      """  Operator code  """  
      pass

class ValidateOperand2_output:
   def __init__(self, obj):
      pass

class ValidateOperand3_input:
   """ Required : 
   proposedOperand3
   iLine
   iAlgorithm
   """  
   def __init__(self, obj):
      self.proposedOperand3:str = obj["proposedOperand3"]
      """  Proposed Operand3 value  """  
      self.iLine:int = obj["iLine"]
      """  Line Number  """  
      self.iAlgorithm:str = obj["iAlgorithm"]
      """  Algorithm code  """  
      pass

class ValidateOperand3_output:
   def __init__(self, obj):
      pass

class ValidateOperand4_input:
   """ Required : 
   proposedOperand4
   iLine
   iAlgorithm
   """  
   def __init__(self, obj):
      self.proposedOperand4:str = obj["proposedOperand4"]
      """  Proposed Operand4 value  """  
      self.iLine:int = obj["iLine"]
      """  Line Number  """  
      self.iAlgorithm:str = obj["iAlgorithm"]
      """  Algorithm code  """  
      pass

class ValidateOperand4_output:
   def __init__(self, obj):
      pass

class ValidateOperator_input:
   """ Required : 
   proposedOperator
   iOperand1
   """  
   def __init__(self, obj):
      self.proposedOperator:str = obj["proposedOperator"]
      """  Proposed Operator value  """  
      self.iOperand1:str = obj["iOperand1"]
      """  Operator code  """  
      pass

class ValidateOperator_output:
   def __init__(self, obj):
      pass

class ValidateTaxCode_input:
   """ Required : 
   proposedTaxCode
   """  
   def __init__(self, obj):
      self.proposedTaxCode:str = obj["proposedTaxCode"]
      """  Proposed Tax Code  """  
      pass

class ValidateTaxCode_output:
   def __init__(self, obj):
      pass

