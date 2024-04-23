import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.CNGoldenTaxInterfaceSvc
# Description: CN Golden Tax Interface Service
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CNGoldenTaxInterfaceSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CNGoldenTaxInterfaceSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_CNGoldenTaxInterfaces(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get CNGoldenTaxInterfaces items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CNGoldenTaxInterfaces
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GTIInvcHeadRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CNGoldenTaxInterfaceSvc/CNGoldenTaxInterfaces",headers=creds) as resp:
           return await resp.json()

async def post_CNGoldenTaxInterfaces(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CNGoldenTaxInterfaces
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.GTIInvcHeadRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.GTIInvcHeadRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CNGoldenTaxInterfaceSvc/CNGoldenTaxInterfaces", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_CNGoldenTaxInterfaces_Company_GroupNum_GroupSuffix(Company, GroupNum, GroupSuffix, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the CNGoldenTaxInterface item
   Description: Calls GetByID to retrieve the CNGoldenTaxInterface item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CNGoldenTaxInterface
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupNum: Desc: GroupNum   Required: True
      :param GroupSuffix: Desc: GroupSuffix   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.GTIInvcHeadRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CNGoldenTaxInterfaceSvc/CNGoldenTaxInterfaces(" + Company + "," + GroupNum + "," + GroupSuffix + ")",headers=creds) as resp:
           return await resp.json()

async def patch_CNGoldenTaxInterfaces_Company_GroupNum_GroupSuffix(Company, GroupNum, GroupSuffix, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update CNGoldenTaxInterface for the service
   Description: Calls UpdateExt to update CNGoldenTaxInterface. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CNGoldenTaxInterface
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupNum: Desc: GroupNum   Required: True
      :param GroupSuffix: Desc: GroupSuffix   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.GTIInvcHeadRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.CNGoldenTaxInterfaceSvc/CNGoldenTaxInterfaces(" + Company + "," + GroupNum + "," + GroupSuffix + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_CNGoldenTaxInterfaces_Company_GroupNum_GroupSuffix(Company, GroupNum, GroupSuffix, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete CNGoldenTaxInterface item
   Description: Call UpdateExt to delete CNGoldenTaxInterface item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CNGoldenTaxInterface
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupNum: Desc: GroupNum   Required: True
      :param GroupSuffix: Desc: GroupSuffix   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.CNGoldenTaxInterfaceSvc/CNGoldenTaxInterfaces(" + Company + "," + GroupNum + "," + GroupSuffix + ")",headers=creds) as resp:
           return await resp.json()

async def get_CNGoldenTaxInterfaces_Company_GroupNum_GroupSuffix_GTIInvcDtls(Company, GroupNum, GroupSuffix, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get GTIInvcDtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_GTIInvcDtls1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupNum: Desc: GroupNum   Required: True
      :param GroupSuffix: Desc: GroupSuffix   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GTIInvcDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CNGoldenTaxInterfaceSvc/CNGoldenTaxInterfaces(" + Company + "," + GroupNum + "," + GroupSuffix + ")/GTIInvcDtls",headers=creds) as resp:
           return await resp.json()

async def get_CNGoldenTaxInterfaces_Company_GroupNum_GroupSuffix_GTIInvcDtls_Company_GroupNum_GroupSuffix_InvoiceNum_InvoiceLine(Company, GroupNum, GroupSuffix, InvoiceNum, InvoiceLine, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the GTIInvcDtl item
   Description: Calls GetByID to retrieve the GTIInvcDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GTIInvcDtl1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupNum: Desc: GroupNum   Required: True
      :param GroupSuffix: Desc: GroupSuffix   Required: True
      :param InvoiceNum: Desc: InvoiceNum   Required: True
      :param InvoiceLine: Desc: InvoiceLine   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.GTIInvcDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CNGoldenTaxInterfaceSvc/CNGoldenTaxInterfaces(" + Company + "," + GroupNum + "," + GroupSuffix + ")/GTIInvcDtls(" + Company + "," + GroupNum + "," + GroupSuffix + "," + InvoiceNum + "," + InvoiceLine + ")",headers=creds) as resp:
           return await resp.json()

async def get_GTIInvcDtls(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get GTIInvcDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_GTIInvcDtls
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GTIInvcDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CNGoldenTaxInterfaceSvc/GTIInvcDtls",headers=creds) as resp:
           return await resp.json()

async def post_GTIInvcDtls(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_GTIInvcDtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.GTIInvcDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.GTIInvcDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CNGoldenTaxInterfaceSvc/GTIInvcDtls", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GTIInvcDtls_Company_GroupNum_GroupSuffix_InvoiceNum_InvoiceLine(Company, GroupNum, GroupSuffix, InvoiceNum, InvoiceLine, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the GTIInvcDtl item
   Description: Calls GetByID to retrieve the GTIInvcDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GTIInvcDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupNum: Desc: GroupNum   Required: True
      :param GroupSuffix: Desc: GroupSuffix   Required: True
      :param InvoiceNum: Desc: InvoiceNum   Required: True
      :param InvoiceLine: Desc: InvoiceLine   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.GTIInvcDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CNGoldenTaxInterfaceSvc/GTIInvcDtls(" + Company + "," + GroupNum + "," + GroupSuffix + "," + InvoiceNum + "," + InvoiceLine + ")",headers=creds) as resp:
           return await resp.json()

async def patch_GTIInvcDtls_Company_GroupNum_GroupSuffix_InvoiceNum_InvoiceLine(Company, GroupNum, GroupSuffix, InvoiceNum, InvoiceLine, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update GTIInvcDtl for the service
   Description: Calls UpdateExt to update GTIInvcDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_GTIInvcDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupNum: Desc: GroupNum   Required: True
      :param GroupSuffix: Desc: GroupSuffix   Required: True
      :param InvoiceNum: Desc: InvoiceNum   Required: True
      :param InvoiceLine: Desc: InvoiceLine   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.GTIInvcDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.CNGoldenTaxInterfaceSvc/GTIInvcDtls(" + Company + "," + GroupNum + "," + GroupSuffix + "," + InvoiceNum + "," + InvoiceLine + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_GTIInvcDtls_Company_GroupNum_GroupSuffix_InvoiceNum_InvoiceLine(Company, GroupNum, GroupSuffix, InvoiceNum, InvoiceLine, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete GTIInvcDtl item
   Description: Call UpdateExt to delete GTIInvcDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_GTIInvcDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupNum: Desc: GroupNum   Required: True
      :param GroupSuffix: Desc: GroupSuffix   Required: True
      :param InvoiceNum: Desc: InvoiceNum   Required: True
      :param InvoiceLine: Desc: InvoiceLine   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.CNGoldenTaxInterfaceSvc/GTIInvcDtls(" + Company + "," + GroupNum + "," + GroupSuffix + "," + InvoiceNum + "," + InvoiceLine + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GTIInvcHeadListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CNGoldenTaxInterfaceSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseGTIInvcHead, whereClauseGTIInvcDtl, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseGTIInvcHead=" + whereClauseGTIInvcHead
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseGTIInvcDtl=" + whereClauseGTIInvcDtl
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CNGoldenTaxInterfaceSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(groupNum, groupSuffix, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True
   Required: True
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
   params += "groupNum=" + groupNum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "groupSuffix=" + groupSuffix

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CNGoldenTaxInterfaceSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CNGoldenTaxInterfaceSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_CreateNewGTIRecords(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CreateNewGTIRecords
   Description: Creates records in GTIInvcHead and GTIInvcDtl for correspondent records selected by user.
   OperationID: CreateNewGTIRecords
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateNewGTIRecords_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateNewGTIRecords_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CNGoldenTaxInterfaceSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CreateNewGTIRecordsAndGetRows(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CreateNewGTIRecordsAndGetRows
   Description: Creates records in GTIInvcHead and GTIInvcDtl for correspondent records selected by user.
   OperationID: CreateNewGTIRecordsAndGetRows
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateNewGTIRecordsAndGetRows_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateNewGTIRecordsAndGetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CNGoldenTaxInterfaceSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetStatus(epicorHeaders = None):
   """  
   Summary: Invoke method GetStatus
   Description: This method return the list of possible statuses for search form.
   OperationID: GetStatus
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetStatus_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CNGoldenTaxInterfaceSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_InvoiceMerge(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method InvoiceMerge
   Description: Creates new record in GTIInvcHead during Invoice Merge on the base of existant ones if validation is passed.
   OperationID: InvoiceMerge
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/InvoiceMerge_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/InvoiceMerge_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CNGoldenTaxInterfaceSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_InvoiceSplit(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method InvoiceSplit
   Description: Creates new record in GTIInvcHead during Invoice Split on the base of existant ones if validation is passed.
   OperationID: InvoiceSplit
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/InvoiceSplit_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/InvoiceSplit_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CNGoldenTaxInterfaceSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeofShipToNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeofShipToNum
   Description: This method should be called when the ship to number on the invoice detail
record is changed.
   OperationID: OnChangeofShipToNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeofShipToNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeofShipToNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CNGoldenTaxInterfaceSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteObsoleGTIRecs(epicorHeaders = None):
   """  
   Summary: Invoke method DeleteObsoleGTIRecs
   Description: This method deletes records from GTIInvcHead and GTIInvcDtl, for which correcpondent records in InvcHead and InvcDtl were deleted
   OperationID: DeleteObsoleGTIRecs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteObsoleGTIRecs_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CNGoldenTaxInterfaceSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetByIDForGTIS(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetByIDForGTIS
   Description: Returns GTIInvcHead record.
   OperationID: GetByIDForGTIS
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetByIDForGTIS_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByIDForGTIS_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CNGoldenTaxInterfaceSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRowsForGTIS_Lite(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsForGTIS_Lite
   Description: Returns GTIInvcHead records.
   OperationID: GetRowsForGTIS_Lite
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsForGTIS_Lite_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsForGTIS_Lite_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CNGoldenTaxInterfaceSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRowsForGTIS(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsForGTIS
   Description: Returns GTIInvcHead records.
   OperationID: GetRowsForGTIS
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsForGTIS_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsForGTIS_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CNGoldenTaxInterfaceSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeOfInvoiceLineQty(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeOfInvoiceLineQty
   Description: Invoice Line quantity change event handler
   OperationID: OnChangeOfInvoiceLineQty
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeOfInvoiceLineQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeOfInvoiceLineQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CNGoldenTaxInterfaceSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SaveSplittedInvoiceLine(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SaveSplittedInvoiceLine
   Description: Save splitted lines to DB.
   OperationID: SaveSplittedInvoiceLine
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SaveSplittedInvoiceLine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SaveSplittedInvoiceLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CNGoldenTaxInterfaceSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SplitInvoiceLine(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SplitInvoiceLine
   Description: Creates empty record in tableset for GTIInvcDtl.
   OperationID: SplitInvoiceLine
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SplitInvoiceLine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SplitInvoiceLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CNGoldenTaxInterfaceSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewGTIInvcHead(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewGTIInvcHead
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewGTIInvcHead
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewGTIInvcHead_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewGTIInvcHead_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CNGoldenTaxInterfaceSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewGTIInvcDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewGTIInvcDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewGTIInvcDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewGTIInvcDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewGTIInvcDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CNGoldenTaxInterfaceSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CNGoldenTaxInterfaceSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CNGoldenTaxInterfaceSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CNGoldenTaxInterfaceSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CNGoldenTaxInterfaceSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CNGoldenTaxInterfaceSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GTIInvcDtlRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_GTIInvcDtlRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GTIInvcHeadListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_GTIInvcHeadListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GTIInvcHeadRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_GTIInvcHeadRow] = obj["value"]
      pass

class Erp_Tablesets_GTIInvcDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.GroupNum:int = obj["GroupNum"]
      """  GroupNum  """  
      self.GroupSuffix:int = obj["GroupSuffix"]
      """  GroupSuffix  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  InvoiceNum  """  
      self.InvoiceLine:int = obj["InvoiceLine"]
      """  InvoiceLine  """  
      self.PartNum:str = obj["PartNum"]
      """  PartNum  """  
      self.Qty:int = obj["Qty"]
      """  Qty  """  
      self.UnitPrice:int = obj["UnitPrice"]
      """  UnitPrice  """  
      self.DiscountAmt:int = obj["DiscountAmt"]
      """  DiscountAmt  """  
      self.DiscountTaxAmt:int = obj["DiscountTaxAmt"]
      """  DiscountTaxAmt  """  
      self.TaxAmt:int = obj["TaxAmt"]
      """  TaxAmt  """  
      self.TotalAmt:int = obj["TotalAmt"]
      """  TotalAmt  """  
      self.TaxCode:str = obj["TaxCode"]
      """  TaxCode  """  
      self.TaxRate:int = obj["TaxRate"]
      """  TaxRate  """  
      self.PartDescription:str = obj["PartDescription"]
      """  PartDescription  """  
      self.IUM:str = obj["IUM"]
      """  IUM  """  
      self.Specification:str = obj["Specification"]
      """  Specification  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.IUMDescription:str = obj["IUMDescription"]
      """  IUMDescription  """  
      self.CodeVersion:str = obj["CodeVersion"]
      """  Code Version for China GTI purposes  """  
      self.TaxCategoryCode:str = obj["TaxCategoryCode"]
      """  Tax Category Code for China GTI purposes  """  
      self.HasPreferentialTreatment:bool = obj["HasPreferentialTreatment"]
      """  Has Preferential Treatment value  for China GTI purposes  """  
      self.PreferentialTreatmentContent:str = obj["PreferentialTreatmentContent"]
      """  Preferential Treatment Content for China GTI purposes  """  
      self.ZeroTaxRateMark:str = obj["ZeroTaxRateMark"]
      """  Zero Tax Rate Mark  for China GTI purposes  """  
      self.DeductionAmount:int = obj["DeductionAmount"]
      """  Deduction Amount for China GTI purposes  """  
      self.IsSelected:bool = obj["IsSelected"]
      self.TotalNetAmt:int = obj["TotalNetAmt"]
      self.LimitExceeded:bool = obj["LimitExceeded"]
      self.SelectedForAction:bool = obj["SelectedForAction"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GTIInvcHeadListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.GroupNum:int = obj["GroupNum"]
      """  GroupNum  """  
      self.GroupSuffix:int = obj["GroupSuffix"]
      """  GroupSuffix  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  InvoiceNum  """  
      self.Action:str = obj["Action"]
      """  Action  """  
      self.Status1:str = obj["Status1"]
      """  Status1  """  
      self.Status2:bool = obj["Status2"]
      """  Status2  """  
      self.IsSplitMerge:bool = obj["IsSplitMerge"]
      """  IsSplitMerge  """  
      self.GTIInvoiceNum:str = obj["GTIInvoiceNum"]
      """  GTIInvoiceNum  """  
      self.GTIInvoiceType:int = obj["GTIInvoiceType"]
      """  GTIInvoiceType  """  
      self.GTIInvoiceDate:str = obj["GTIInvoiceDate"]
      """  GTIInvoiceDate  """  
      self.GTIInvoiceAmt:int = obj["GTIInvoiceAmt"]
      """  GTIInvoiceAmt  """  
      self.GTITaxAmnt:int = obj["GTITaxAmnt"]
      """  GTITaxAmnt  """  
      self.CustNum:int = obj["CustNum"]
      """  CustNum  """  
      self.InvoiceDate:str = obj["InvoiceDate"]
      """  InvoiceDate  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  CurrencyCode  """  
      self.TaxPeriod:str = obj["TaxPeriod"]
      """  TaxPeriod  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  TaxRegionCode  """  
      self.Comments:str = obj["Comments"]
      """  Comments  """  
      self.Notes:str = obj["Notes"]
      """  Notes  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  ShipToNum  """  
      self.ExportDate:str = obj["ExportDate"]
      """  ExportDate  """  
      self.ImportDate:str = obj["ImportDate"]
      """  ImportDate  """  
      self.ExportedBy:str = obj["ExportedBy"]
      """  ExportedBy  """  
      self.ImportedBy:str = obj["ImportedBy"]
      """  ImportedBy  """  
      self.IsWaitForExport:bool = obj["IsWaitForExport"]
      """  IsWaitForExport  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GTIInvcHeadRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.GroupNum:int = obj["GroupNum"]
      """  GroupNum  """  
      self.GroupSuffix:int = obj["GroupSuffix"]
      """  GroupSuffix  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  InvoiceNum  """  
      self.Action:str = obj["Action"]
      """  Action  """  
      self.Status1:str = obj["Status1"]
      """  Status1  """  
      self.Status2:bool = obj["Status2"]
      """  Status2  """  
      self.IsSplitMerge:bool = obj["IsSplitMerge"]
      """  IsSplitMerge  """  
      self.GTIInvoiceNum:str = obj["GTIInvoiceNum"]
      """  GTIInvoiceNum  """  
      self.GTIInvoiceType:int = obj["GTIInvoiceType"]
      """  GTIInvoiceType  """  
      self.GTIInvoiceDate:str = obj["GTIInvoiceDate"]
      """  GTIInvoiceDate  """  
      self.GTIInvoiceAmt:int = obj["GTIInvoiceAmt"]
      """  GTIInvoiceAmt  """  
      self.GTITaxAmnt:int = obj["GTITaxAmnt"]
      """  GTITaxAmnt  """  
      self.CustNum:int = obj["CustNum"]
      """  CustNum  """  
      self.InvoiceDate:str = obj["InvoiceDate"]
      """  InvoiceDate  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  CurrencyCode  """  
      self.TaxPeriod:str = obj["TaxPeriod"]
      """  TaxPeriod  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  TaxRegionCode  """  
      self.Comments:str = obj["Comments"]
      """  Comments  """  
      self.Notes:str = obj["Notes"]
      """  Notes  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  ShipToNum  """  
      self.ExportDate:str = obj["ExportDate"]
      """  ExportDate  """  
      self.ImportDate:str = obj["ImportDate"]
      """  ImportDate  """  
      self.ExportedBy:str = obj["ExportedBy"]
      """  ExportedBy  """  
      self.ImportedBy:str = obj["ImportedBy"]
      """  ImportedBy  """  
      self.IsWaitForExport:bool = obj["IsWaitForExport"]
      """  IsWaitForExport  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.TaxCode:str = obj["TaxCode"]
      self.BankAcctNumber:str = obj["BankAcctNumber"]
      self.ShipToName:str = obj["ShipToName"]
      self.ShipToNameAndAddress:str = obj["ShipToNameAndAddress"]
      self.ShipToAddess:str = obj["ShipToAddess"]
      self.InvoiceAmt:int = obj["InvoiceAmt"]
      """  Invoice amount = InvcHead.InvoiceAmt - InvcHead.WithholdAmt  """  
      self.GrossInvoiceAmt:int = obj["GrossInvoiceAmt"]
      self.GroupNumSuffix:str = obj["GroupNumSuffix"]
      self.GroupID:str = obj["GroupID"]
      self.IsSelected:bool = obj["IsSelected"]
      self.SellerAddress:str = obj["SellerAddress"]
      self.SellerBankName:str = obj["SellerBankName"]
      self.CustID:str = obj["CustID"]
      self.AllowedActions:str = obj["AllowedActions"]
      """  Allowed Actions LIst separeted by ~  """  
      self.LimitExceeded:bool = obj["LimitExceeded"]
      self.AllowedActionsWithDesc:str = obj["AllowedActionsWithDesc"]
      self.ActionDescription:str = obj["ActionDescription"]
      self.SelectedForAction:bool = obj["SelectedForAction"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class CreateNewGTIRecordsAndGetRows_input:
   """ Required : 
   cGroupList
   """  
   def __init__(self, obj):
      self.cGroupList:str = obj["cGroupList"]
      """  List of Group, which data should be got for UI  """  
      pass

class CreateNewGTIRecordsAndGetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CNGoldenTaxInterfaceTableset] = obj["returnObj"]
      pass

class CreateNewGTIRecords_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CNGoldenTaxInterfaceTableset] = obj["ds"]
      pass

class CreateNewGTIRecords_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CNGoldenTaxInterfaceTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   groupNum
   groupSuffix
   """  
   def __init__(self, obj):
      self.groupNum:int = obj["groupNum"]
      self.groupSuffix:int = obj["groupSuffix"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class DeleteObsoleGTIRecs_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_CNGoldenTaxInterfaceListTableset:
   def __init__(self, obj):
      self.GTIInvcHeadList:list[Erp_Tablesets_GTIInvcHeadListRow] = obj["GTIInvcHeadList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_CNGoldenTaxInterfaceTableset:
   def __init__(self, obj):
      self.GTIInvcHead:list[Erp_Tablesets_GTIInvcHeadRow] = obj["GTIInvcHead"]
      self.GTIInvcDtl:list[Erp_Tablesets_GTIInvcDtlRow] = obj["GTIInvcDtl"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_GTIInvcDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.GroupNum:int = obj["GroupNum"]
      """  GroupNum  """  
      self.GroupSuffix:int = obj["GroupSuffix"]
      """  GroupSuffix  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  InvoiceNum  """  
      self.InvoiceLine:int = obj["InvoiceLine"]
      """  InvoiceLine  """  
      self.PartNum:str = obj["PartNum"]
      """  PartNum  """  
      self.Qty:int = obj["Qty"]
      """  Qty  """  
      self.UnitPrice:int = obj["UnitPrice"]
      """  UnitPrice  """  
      self.DiscountAmt:int = obj["DiscountAmt"]
      """  DiscountAmt  """  
      self.DiscountTaxAmt:int = obj["DiscountTaxAmt"]
      """  DiscountTaxAmt  """  
      self.TaxAmt:int = obj["TaxAmt"]
      """  TaxAmt  """  
      self.TotalAmt:int = obj["TotalAmt"]
      """  TotalAmt  """  
      self.TaxCode:str = obj["TaxCode"]
      """  TaxCode  """  
      self.TaxRate:int = obj["TaxRate"]
      """  TaxRate  """  
      self.PartDescription:str = obj["PartDescription"]
      """  PartDescription  """  
      self.IUM:str = obj["IUM"]
      """  IUM  """  
      self.Specification:str = obj["Specification"]
      """  Specification  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.IUMDescription:str = obj["IUMDescription"]
      """  IUMDescription  """  
      self.CodeVersion:str = obj["CodeVersion"]
      """  Code Version for China GTI purposes  """  
      self.TaxCategoryCode:str = obj["TaxCategoryCode"]
      """  Tax Category Code for China GTI purposes  """  
      self.HasPreferentialTreatment:bool = obj["HasPreferentialTreatment"]
      """  Has Preferential Treatment value  for China GTI purposes  """  
      self.PreferentialTreatmentContent:str = obj["PreferentialTreatmentContent"]
      """  Preferential Treatment Content for China GTI purposes  """  
      self.ZeroTaxRateMark:str = obj["ZeroTaxRateMark"]
      """  Zero Tax Rate Mark  for China GTI purposes  """  
      self.DeductionAmount:int = obj["DeductionAmount"]
      """  Deduction Amount for China GTI purposes  """  
      self.IsSelected:bool = obj["IsSelected"]
      self.TotalNetAmt:int = obj["TotalNetAmt"]
      self.LimitExceeded:bool = obj["LimitExceeded"]
      self.SelectedForAction:bool = obj["SelectedForAction"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GTIInvcHeadListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.GroupNum:int = obj["GroupNum"]
      """  GroupNum  """  
      self.GroupSuffix:int = obj["GroupSuffix"]
      """  GroupSuffix  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  InvoiceNum  """  
      self.Action:str = obj["Action"]
      """  Action  """  
      self.Status1:str = obj["Status1"]
      """  Status1  """  
      self.Status2:bool = obj["Status2"]
      """  Status2  """  
      self.IsSplitMerge:bool = obj["IsSplitMerge"]
      """  IsSplitMerge  """  
      self.GTIInvoiceNum:str = obj["GTIInvoiceNum"]
      """  GTIInvoiceNum  """  
      self.GTIInvoiceType:int = obj["GTIInvoiceType"]
      """  GTIInvoiceType  """  
      self.GTIInvoiceDate:str = obj["GTIInvoiceDate"]
      """  GTIInvoiceDate  """  
      self.GTIInvoiceAmt:int = obj["GTIInvoiceAmt"]
      """  GTIInvoiceAmt  """  
      self.GTITaxAmnt:int = obj["GTITaxAmnt"]
      """  GTITaxAmnt  """  
      self.CustNum:int = obj["CustNum"]
      """  CustNum  """  
      self.InvoiceDate:str = obj["InvoiceDate"]
      """  InvoiceDate  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  CurrencyCode  """  
      self.TaxPeriod:str = obj["TaxPeriod"]
      """  TaxPeriod  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  TaxRegionCode  """  
      self.Comments:str = obj["Comments"]
      """  Comments  """  
      self.Notes:str = obj["Notes"]
      """  Notes  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  ShipToNum  """  
      self.ExportDate:str = obj["ExportDate"]
      """  ExportDate  """  
      self.ImportDate:str = obj["ImportDate"]
      """  ImportDate  """  
      self.ExportedBy:str = obj["ExportedBy"]
      """  ExportedBy  """  
      self.ImportedBy:str = obj["ImportedBy"]
      """  ImportedBy  """  
      self.IsWaitForExport:bool = obj["IsWaitForExport"]
      """  IsWaitForExport  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GTIInvcHeadRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.GroupNum:int = obj["GroupNum"]
      """  GroupNum  """  
      self.GroupSuffix:int = obj["GroupSuffix"]
      """  GroupSuffix  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  InvoiceNum  """  
      self.Action:str = obj["Action"]
      """  Action  """  
      self.Status1:str = obj["Status1"]
      """  Status1  """  
      self.Status2:bool = obj["Status2"]
      """  Status2  """  
      self.IsSplitMerge:bool = obj["IsSplitMerge"]
      """  IsSplitMerge  """  
      self.GTIInvoiceNum:str = obj["GTIInvoiceNum"]
      """  GTIInvoiceNum  """  
      self.GTIInvoiceType:int = obj["GTIInvoiceType"]
      """  GTIInvoiceType  """  
      self.GTIInvoiceDate:str = obj["GTIInvoiceDate"]
      """  GTIInvoiceDate  """  
      self.GTIInvoiceAmt:int = obj["GTIInvoiceAmt"]
      """  GTIInvoiceAmt  """  
      self.GTITaxAmnt:int = obj["GTITaxAmnt"]
      """  GTITaxAmnt  """  
      self.CustNum:int = obj["CustNum"]
      """  CustNum  """  
      self.InvoiceDate:str = obj["InvoiceDate"]
      """  InvoiceDate  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  CurrencyCode  """  
      self.TaxPeriod:str = obj["TaxPeriod"]
      """  TaxPeriod  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  TaxRegionCode  """  
      self.Comments:str = obj["Comments"]
      """  Comments  """  
      self.Notes:str = obj["Notes"]
      """  Notes  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  ShipToNum  """  
      self.ExportDate:str = obj["ExportDate"]
      """  ExportDate  """  
      self.ImportDate:str = obj["ImportDate"]
      """  ImportDate  """  
      self.ExportedBy:str = obj["ExportedBy"]
      """  ExportedBy  """  
      self.ImportedBy:str = obj["ImportedBy"]
      """  ImportedBy  """  
      self.IsWaitForExport:bool = obj["IsWaitForExport"]
      """  IsWaitForExport  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.TaxCode:str = obj["TaxCode"]
      self.BankAcctNumber:str = obj["BankAcctNumber"]
      self.ShipToName:str = obj["ShipToName"]
      self.ShipToNameAndAddress:str = obj["ShipToNameAndAddress"]
      self.ShipToAddess:str = obj["ShipToAddess"]
      self.InvoiceAmt:int = obj["InvoiceAmt"]
      """  Invoice amount = InvcHead.InvoiceAmt - InvcHead.WithholdAmt  """  
      self.GrossInvoiceAmt:int = obj["GrossInvoiceAmt"]
      self.GroupNumSuffix:str = obj["GroupNumSuffix"]
      self.GroupID:str = obj["GroupID"]
      self.IsSelected:bool = obj["IsSelected"]
      self.SellerAddress:str = obj["SellerAddress"]
      self.SellerBankName:str = obj["SellerBankName"]
      self.CustID:str = obj["CustID"]
      self.AllowedActions:str = obj["AllowedActions"]
      """  Allowed Actions LIst separeted by ~  """  
      self.LimitExceeded:bool = obj["LimitExceeded"]
      self.AllowedActionsWithDesc:str = obj["AllowedActionsWithDesc"]
      self.ActionDescription:str = obj["ActionDescription"]
      self.SelectedForAction:bool = obj["SelectedForAction"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UpdExtCNGoldenTaxInterfaceTableset:
   def __init__(self, obj):
      self.GTIInvcHead:list[Erp_Tablesets_GTIInvcHeadRow] = obj["GTIInvcHead"]
      self.GTIInvcDtl:list[Erp_Tablesets_GTIInvcDtlRow] = obj["GTIInvcDtl"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByIDForGTIS_input:
   """ Required : 
   cGroupNumSuffix
   """  
   def __init__(self, obj):
      self.cGroupNumSuffix:str = obj["cGroupNumSuffix"]
      """  Group number and suffix  """  
      pass

class GetByIDForGTIS_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CNGoldenTaxInterfaceTableset] = obj["returnObj"]
      pass

class GetByID_input:
   """ Required : 
   groupNum
   groupSuffix
   """  
   def __init__(self, obj):
      self.groupNum:int = obj["groupNum"]
      self.groupSuffix:int = obj["groupSuffix"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CNGoldenTaxInterfaceTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_CNGoldenTaxInterfaceTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_CNGoldenTaxInterfaceTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_CNGoldenTaxInterfaceListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewGTIInvcDtl_input:
   """ Required : 
   ds
   groupNum
   groupSuffix
   invoiceNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CNGoldenTaxInterfaceTableset] = obj["ds"]
      self.groupNum:int = obj["groupNum"]
      self.groupSuffix:int = obj["groupSuffix"]
      self.invoiceNum:int = obj["invoiceNum"]
      pass

class GetNewGTIInvcDtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CNGoldenTaxInterfaceTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewGTIInvcHead_input:
   """ Required : 
   ds
   groupNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CNGoldenTaxInterfaceTableset] = obj["ds"]
      self.groupNum:int = obj["groupNum"]
      pass

class GetNewGTIInvcHead_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CNGoldenTaxInterfaceTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRowsForGTIS_Lite_input:
   """ Required : 
   whereClauseGTIInvcHead
   whereClauseGTIInvcDtl
   bSelectFromInvcHead
   whereClauseDateFrom
   whereClauseDateTo
   whereClauseCustNum
   whereClauseStatus1
   includeCM
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseGTIInvcHead:str = obj["whereClauseGTIInvcHead"]
      """  Base Whereclause for GTIInvcHead table.  """  
      self.whereClauseGTIInvcDtl:str = obj["whereClauseGTIInvcDtl"]
      """  Base Whereclause for GTIInvcDtl table.  """  
      self.bSelectFromInvcHead:bool = obj["bSelectFromInvcHead"]
      """  Flag: true - add records from InvcHead/InvcDtl to ds; false - select records from GTIInvcHead/GTIInvcDtl only.  """  
      self.whereClauseDateFrom:str = obj["whereClauseDateFrom"]
      """  Whereclause for Date from  """  
      self.whereClauseDateTo:str = obj["whereClauseDateTo"]
      """  Whereclause for Date to  """  
      self.whereClauseCustNum:int = obj["whereClauseCustNum"]
      """  Whereclause for CustNum  """  
      self.whereClauseStatus1:str = obj["whereClauseStatus1"]
      """  Whereclause for Status1  """  
      self.includeCM:bool = obj["includeCM"]
      """  Flag: Include or not Credit Memos  """  
      self.pageSize:int = obj["pageSize"]
      """  Page size.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Absolute page.  """  
      pass

class GetRowsForGTIS_Lite_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CNGoldenTaxInterfaceTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRowsForGTIS_input:
   """ Required : 
   whereClauseGTIInvcHead
   whereClauseGTIInvcDtl
   bSelectFromInvcHead
   whereClauseDateFrom
   whereClauseDateTo
   whereClauseCustNum
   whereClauseStatus1
   includeCM
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseGTIInvcHead:str = obj["whereClauseGTIInvcHead"]
      """  Base Whereclause for GTIInvcHead table.  """  
      self.whereClauseGTIInvcDtl:str = obj["whereClauseGTIInvcDtl"]
      """  Base Whereclause for GTIInvcDtl table.  """  
      self.bSelectFromInvcHead:bool = obj["bSelectFromInvcHead"]
      """  Flag: true - add records from InvcHead/InvcDtl to ds; false - select records from GTIInvcHead/GTIInvcDtl only.  """  
      self.whereClauseDateFrom:str = obj["whereClauseDateFrom"]
      """  Whereclause for Date from  """  
      self.whereClauseDateTo:str = obj["whereClauseDateTo"]
      """  Whereclause for Date to  """  
      self.whereClauseCustNum:int = obj["whereClauseCustNum"]
      """  Whereclause for CustNum  """  
      self.whereClauseStatus1:str = obj["whereClauseStatus1"]
      """  Whereclause for Status1  """  
      self.includeCM:bool = obj["includeCM"]
      """  Flag: Include or not Credit Memos  """  
      self.pageSize:int = obj["pageSize"]
      """  Page size.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Absolute page.  """  
      pass

class GetRowsForGTIS_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CNGoldenTaxInterfaceTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseGTIInvcHead
   whereClauseGTIInvcDtl
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseGTIInvcHead:str = obj["whereClauseGTIInvcHead"]
      self.whereClauseGTIInvcDtl:str = obj["whereClauseGTIInvcDtl"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CNGoldenTaxInterfaceTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetStatus_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  Default status  """  
      pass

   def parameters(self, obj):
      self.cDefaultStatus:str = obj["parameters"]
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

class InvoiceMerge_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CNGoldenTaxInterfaceTableset] = obj["ds"]
      pass

class InvoiceMerge_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CNGoldenTaxInterfaceTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CNGoldenTaxInterfaceTableset] = obj["ds"]
      pass

      """  output parameters  """  

class InvoiceSplit_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CNGoldenTaxInterfaceTableset] = obj["ds"]
      pass

class InvoiceSplit_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CNGoldenTaxInterfaceTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CNGoldenTaxInterfaceTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeOfInvoiceLineQty_input:
   """ Required : 
   proposedQty
   ds
   """  
   def __init__(self, obj):
      self.proposedQty:int = obj["proposedQty"]
      self.ds:list[Erp_Tablesets_CNGoldenTaxInterfaceTableset] = obj["ds"]
      pass

class OnChangeOfInvoiceLineQty_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CNGoldenTaxInterfaceTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeofShipToNum_input:
   """ Required : 
   iGroupNum
   iGroupSuffix
   cNewShipToNum
   ds
   """  
   def __init__(self, obj):
      self.iGroupNum:int = obj["iGroupNum"]
      """  Group Number  """  
      self.iGroupSuffix:int = obj["iGroupSuffix"]
      """  Group Suffix  """  
      self.cNewShipToNum:str = obj["cNewShipToNum"]
      """  Proposed ship to number  """  
      self.ds:list[Erp_Tablesets_CNGoldenTaxInterfaceTableset] = obj["ds"]
      pass

class OnChangeofShipToNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CNGoldenTaxInterfaceTableset] = obj["ds"]
      pass

      """  output parameters  """  

class SaveSplittedInvoiceLine_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CNGoldenTaxInterfaceTableset] = obj["ds"]
      pass

class SaveSplittedInvoiceLine_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CNGoldenTaxInterfaceTableset] = obj["ds"]
      pass

      """  output parameters  """  

class SplitInvoiceLine_input:
   """ Required : 
   sGroupNumSuffix
   sStatus1
   bStatus2
   ds
   """  
   def __init__(self, obj):
      self.sGroupNumSuffix:str = obj["sGroupNumSuffix"]
      """  Group Number and Suffix  """  
      self.sStatus1:str = obj["sStatus1"]
      """  Status1: New or Exported or Updated  """  
      self.bStatus2:bool = obj["bStatus2"]
      """  Status2: Regular or Voided  """  
      self.ds:list[Erp_Tablesets_CNGoldenTaxInterfaceTableset] = obj["ds"]
      pass

class SplitInvoiceLine_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CNGoldenTaxInterfaceTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtCNGoldenTaxInterfaceTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtCNGoldenTaxInterfaceTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CNGoldenTaxInterfaceTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CNGoldenTaxInterfaceTableset] = obj["ds"]
      pass

      """  output parameters  """  

