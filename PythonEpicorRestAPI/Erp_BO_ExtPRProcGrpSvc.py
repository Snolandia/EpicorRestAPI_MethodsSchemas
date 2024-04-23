import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.ExtPRProcGrpSvc
# Description: BO to create and process payroll employees, creating and exporting labor hours to an external Payroll System.
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ExtPRProcGrpSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ExtPRProcGrpSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_ExtPRProcGrps(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ExtPRProcGrps items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ExtPRProcGrps
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ExtPRProcGrpRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ExtPRProcGrpSvc/ExtPRProcGrps",headers=creds) as resp:
           return await resp.json()

async def post_ExtPRProcGrps(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ExtPRProcGrps
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ExtPRProcGrpRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ExtPRProcGrpRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ExtPRProcGrpSvc/ExtPRProcGrps", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ExtPRProcGrps_Company_GroupID(Company, GroupID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ExtPRProcGrp item
   Description: Calls GetByID to retrieve the ExtPRProcGrp item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ExtPRProcGrp
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ExtPRProcGrpRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ExtPRProcGrpSvc/ExtPRProcGrps(" + Company + "," + GroupID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ExtPRProcGrps_Company_GroupID(Company, GroupID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ExtPRProcGrp for the service
   Description: Calls UpdateExt to update ExtPRProcGrp. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ExtPRProcGrp
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ExtPRProcGrpRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ExtPRProcGrpSvc/ExtPRProcGrps(" + Company + "," + GroupID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ExtPRProcGrps_Company_GroupID(Company, GroupID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ExtPRProcGrp item
   Description: Call UpdateExt to delete ExtPRProcGrp item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ExtPRProcGrp
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ExtPRProcGrpSvc/ExtPRProcGrps(" + Company + "," + GroupID + ")",headers=creds) as resp:
           return await resp.json()

async def get_ExtPRProcGrps_Company_GroupID_ExtPRGrpEmps(Company, GroupID, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ExtPRGrpEmps items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ExtPRGrpEmps1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ExtPRGrpEmpRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ExtPRProcGrpSvc/ExtPRProcGrps(" + Company + "," + GroupID + ")/ExtPRGrpEmps",headers=creds) as resp:
           return await resp.json()

async def get_ExtPRProcGrps_Company_GroupID_ExtPRGrpEmps_Company_GroupID_EmpID(Company, GroupID, EmpID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ExtPRGrpEmp item
   Description: Calls GetByID to retrieve the ExtPRGrpEmp item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ExtPRGrpEmp1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param EmpID: Desc: EmpID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ExtPRGrpEmpRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ExtPRProcGrpSvc/ExtPRProcGrps(" + Company + "," + GroupID + ")/ExtPRGrpEmps(" + Company + "," + GroupID + "," + EmpID + ")",headers=creds) as resp:
           return await resp.json()

async def get_ExtPRGrpEmps(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ExtPRGrpEmps items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ExtPRGrpEmps
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ExtPRGrpEmpRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ExtPRProcGrpSvc/ExtPRGrpEmps",headers=creds) as resp:
           return await resp.json()

async def post_ExtPRGrpEmps(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ExtPRGrpEmps
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ExtPRGrpEmpRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ExtPRGrpEmpRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ExtPRProcGrpSvc/ExtPRGrpEmps", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ExtPRGrpEmps_Company_GroupID_EmpID(Company, GroupID, EmpID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ExtPRGrpEmp item
   Description: Calls GetByID to retrieve the ExtPRGrpEmp item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ExtPRGrpEmp
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param EmpID: Desc: EmpID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ExtPRGrpEmpRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ExtPRProcGrpSvc/ExtPRGrpEmps(" + Company + "," + GroupID + "," + EmpID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ExtPRGrpEmps_Company_GroupID_EmpID(Company, GroupID, EmpID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ExtPRGrpEmp for the service
   Description: Calls UpdateExt to update ExtPRGrpEmp. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ExtPRGrpEmp
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param EmpID: Desc: EmpID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ExtPRGrpEmpRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ExtPRProcGrpSvc/ExtPRGrpEmps(" + Company + "," + GroupID + "," + EmpID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ExtPRGrpEmps_Company_GroupID_EmpID(Company, GroupID, EmpID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ExtPRGrpEmp item
   Description: Call UpdateExt to delete ExtPRGrpEmp item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ExtPRGrpEmp
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param EmpID: Desc: EmpID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ExtPRProcGrpSvc/ExtPRGrpEmps(" + Company + "," + GroupID + "," + EmpID + ")",headers=creds) as resp:
           return await resp.json()

async def get_ExtPRGrpEmps_Company_GroupID_EmpID_ExtPRGrpEmpDtls(Company, GroupID, EmpID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ExtPRGrpEmpDtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ExtPRGrpEmpDtls1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param EmpID: Desc: EmpID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ExtPRGrpEmpDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ExtPRProcGrpSvc/ExtPRGrpEmps(" + Company + "," + GroupID + "," + EmpID + ")/ExtPRGrpEmpDtls",headers=creds) as resp:
           return await resp.json()

async def get_ExtPRGrpEmps_Company_GroupID_EmpID_ExtPRGrpEmpDtls_Company_GroupID_EmpID_DtlNum(Company, GroupID, EmpID, DtlNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ExtPRGrpEmpDtl item
   Description: Calls GetByID to retrieve the ExtPRGrpEmpDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ExtPRGrpEmpDtl1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param EmpID: Desc: EmpID   Required: True   Allow empty value : True
      :param DtlNum: Desc: DtlNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ExtPRGrpEmpDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ExtPRProcGrpSvc/ExtPRGrpEmps(" + Company + "," + GroupID + "," + EmpID + ")/ExtPRGrpEmpDtls(" + Company + "," + GroupID + "," + EmpID + "," + DtlNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_ExtPRGrpEmpDtls(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ExtPRGrpEmpDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ExtPRGrpEmpDtls
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ExtPRGrpEmpDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ExtPRProcGrpSvc/ExtPRGrpEmpDtls",headers=creds) as resp:
           return await resp.json()

async def post_ExtPRGrpEmpDtls(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ExtPRGrpEmpDtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ExtPRGrpEmpDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ExtPRGrpEmpDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ExtPRProcGrpSvc/ExtPRGrpEmpDtls", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ExtPRGrpEmpDtls_Company_GroupID_EmpID_DtlNum(Company, GroupID, EmpID, DtlNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ExtPRGrpEmpDtl item
   Description: Calls GetByID to retrieve the ExtPRGrpEmpDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ExtPRGrpEmpDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param EmpID: Desc: EmpID   Required: True   Allow empty value : True
      :param DtlNum: Desc: DtlNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ExtPRGrpEmpDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ExtPRProcGrpSvc/ExtPRGrpEmpDtls(" + Company + "," + GroupID + "," + EmpID + "," + DtlNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ExtPRGrpEmpDtls_Company_GroupID_EmpID_DtlNum(Company, GroupID, EmpID, DtlNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ExtPRGrpEmpDtl for the service
   Description: Calls UpdateExt to update ExtPRGrpEmpDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ExtPRGrpEmpDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param EmpID: Desc: EmpID   Required: True   Allow empty value : True
      :param DtlNum: Desc: DtlNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ExtPRGrpEmpDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ExtPRProcGrpSvc/ExtPRGrpEmpDtls(" + Company + "," + GroupID + "," + EmpID + "," + DtlNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ExtPRGrpEmpDtls_Company_GroupID_EmpID_DtlNum(Company, GroupID, EmpID, DtlNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ExtPRGrpEmpDtl item
   Description: Call UpdateExt to delete ExtPRGrpEmpDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ExtPRGrpEmpDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param EmpID: Desc: EmpID   Required: True   Allow empty value : True
      :param DtlNum: Desc: DtlNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ExtPRProcGrpSvc/ExtPRGrpEmpDtls(" + Company + "," + GroupID + "," + EmpID + "," + DtlNum + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ExtPRProcGrpListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ExtPRProcGrpSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseExtPRProcGrp, whereClauseExtPRGrpEmp, whereClauseExtPRGrpEmpDtl, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
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
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseExtPRProcGrp=" + whereClauseExtPRProcGrp
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseExtPRGrpEmp=" + whereClauseExtPRGrpEmp
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseExtPRGrpEmpDtl=" + whereClauseExtPRGrpEmpDtl
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ExtPRProcGrpSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(groupID, epicorHeaders = None):
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
   params += "groupID=" + groupID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ExtPRProcGrpSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ExtPRProcGrpSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_FillEmployeeData(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method FillEmployeeData
   Description: This will populate all the required fields for the ExtPRGrpEmp table.
   OperationID: FillEmployeeData
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/FillEmployeeData_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/FillEmployeeData_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ExtPRProcGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GenerateHours(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GenerateHours
   Description: This method will generate the hours for each employee that meets the group requirements.
   OperationID: GenerateHours
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GenerateHours_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateHours_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ExtPRProcGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CalculateOTDT(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CalculateOTDT
   Description: This method will redistribute the pay hours into Overtime and Double-time according to the Payroll Class configuration for the employee.
   OperationID: CalculateOTDT
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CalculateOTDT_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CalculateOTDT_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ExtPRProcGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ClosePayrollGroup(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ClosePayrollGroup
   Description: This method will close the payroll group.
   OperationID: ClosePayrollGroup
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ClosePayrollGroup_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ClosePayrollGroup_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ExtPRProcGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetWhereClause(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetWhereClause
   Description: This method will generate WHERE clause to use for ExtPREmpSvc->GetList request.
   OperationID: GetWhereClause
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetWhereClause_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetWhereClause_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ExtPRProcGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewExtPRProcGrp(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewExtPRProcGrp
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewExtPRProcGrp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewExtPRProcGrp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewExtPRProcGrp_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ExtPRProcGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewExtPRGrpEmp(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewExtPRGrpEmp
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewExtPRGrpEmp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewExtPRGrpEmp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewExtPRGrpEmp_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ExtPRProcGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewExtPRGrpEmpDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewExtPRGrpEmpDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewExtPRGrpEmpDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewExtPRGrpEmpDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewExtPRGrpEmpDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ExtPRProcGrpSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ExtPRProcGrpSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ExtPRProcGrpSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ExtPRProcGrpSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ExtPRProcGrpSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ExtPRProcGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ExtPRGrpEmpDtlRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ExtPRGrpEmpDtlRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ExtPRGrpEmpRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ExtPRGrpEmpRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ExtPRProcGrpListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ExtPRProcGrpListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ExtPRProcGrpRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ExtPRProcGrpRow] = obj["value"]
      pass

class Erp_Tablesets_ExtPRGrpEmpDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.GroupID:str = obj["GroupID"]
      """  Group ID  """  
      self.EmpID:str = obj["EmpID"]
      """  Employee ID  """  
      self.DtlNum:int = obj["DtlNum"]
      """  DtlNum  """  
      self.PayrollDate:str = obj["PayrollDate"]
      """  Date for the entered work/labor hours.  """  
      self.PayTypeID:str = obj["PayTypeID"]
      """  Pay Type selected for the hours detail record.  """  
      self.BaseHours:int = obj["BaseHours"]
      """  Number of Base Hours.  """  
      self.OTHours:int = obj["OTHours"]
      """  Number of overtime hours.  """  
      self.Hours3:int = obj["Hours3"]
      """  This are usually other hours apart from Regular and Overtime.  """  
      self.Hours3Code:str = obj["Hours3Code"]
      """  Pay Type ID meant for the Hours3 field.  """  
      self.SentToFile:bool = obj["SentToFile"]
      """  Indicates the record has been exported.  """  
      self.TempDept:str = obj["TempDept"]
      """  Department entered for the work/labor hours.  """  
      self.FromLabor:bool = obj["FromLabor"]
      """  Indicates the record was created from a Labor Entry.  """  
      self.Shift:int = obj["Shift"]
      """  Shift for the entered work/labor hours.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.TotalHours:int = obj["TotalHours"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ExtPRGrpEmpRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.GroupID:str = obj["GroupID"]
      """  Group ID  """  
      self.EmpID:str = obj["EmpID"]
      """  Employee being processed in the group.  """  
      self.PSDate:str = obj["PSDate"]
      """  Pay Period Start Date.  """  
      self.PEDate:str = obj["PEDate"]
      """  Pay Period End Date.  """  
      self.TotalBaseHours:int = obj["TotalBaseHours"]
      """  Total number of base hours.  """  
      self.TotalOTHours:int = obj["TotalOTHours"]
      """  Total number of overtime hours.  """  
      self.TotalDTHours:int = obj["TotalDTHours"]
      """  Total number of premium hours.  """  
      self.PayClassID:str = obj["PayClassID"]
      """  Payroll Class assigned to the Employee.  """  
      self.PayFreq:str = obj["PayFreq"]
      """  Pay frequency assigned to the Employee.  """  
      self.SentToFile:bool = obj["SentToFile"]
      """  Indicates this record has been exported.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.EmpTotalHours:int = obj["EmpTotalHours"]
      """  Total Hours for the Employee.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.EmpIDEmpName:str = obj["EmpIDEmpName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ExtPRProcGrpListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.GroupID:str = obj["GroupID"]
      """  Group ID  """  
      self.Status:str = obj["Status"]
      """  Indicates the Status of the Payroll Group. Currently we use three: New, Exported and Closed.  """  
      self.PEDate:str = obj["PEDate"]
      """  Payroll Pay Period Ending Date.  """  
      self.PayWeekly:bool = obj["PayWeekly"]
      """  Indicates the "Generate Hours" action will process employees who get paid every week.  """  
      self.PayBiWeekly:bool = obj["PayBiWeekly"]
      """  Indicates the "Generate Hours" action will process employees who get paid every two weeks.  """  
      self.PaySemiMonthly:bool = obj["PaySemiMonthly"]
      """  Indicates the "Generate Hours" action will process employees who get paid twice every month.  """  
      self.PayMonthly:bool = obj["PayMonthly"]
      """  Indicates the "Generate Hours" action will process employees who get paid once every month.  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  UserID of the Employee who created this group.  """  
      self.PayClasses:str = obj["PayClasses"]
      """  List of Payroll Classes that will be processed within the Payroll Group.  """  
      self.SentToFile:bool = obj["SentToFile"]
      """  Indicates the group has been exported to a file.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ExtPRProcGrpRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.GroupID:str = obj["GroupID"]
      """  Group ID  """  
      self.Status:str = obj["Status"]
      """  Indicates the Status of the Payroll Group. Currently we use three: New, Exported and Closed.  """  
      self.PEDate:str = obj["PEDate"]
      """  Payroll Pay Period Ending Date.  """  
      self.PayWeekly:bool = obj["PayWeekly"]
      """  Indicates the "Generate Hours" action will process employees who get paid every week.  """  
      self.PayBiWeekly:bool = obj["PayBiWeekly"]
      """  Indicates the "Generate Hours" action will process employees who get paid every two weeks.  """  
      self.PaySemiMonthly:bool = obj["PaySemiMonthly"]
      """  Indicates the "Generate Hours" action will process employees who get paid twice every month.  """  
      self.PayMonthly:bool = obj["PayMonthly"]
      """  Indicates the "Generate Hours" action will process employees who get paid once every month.  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  UserID of the Employee who created this group.  """  
      self.PayClasses:str = obj["PayClasses"]
      """  List of Payroll Classes that will be processed within the Payroll Group.  """  
      self.SentToFile:bool = obj["SentToFile"]
      """  Indicates the group has been exported to a file.  """  
      self.FilePath:str = obj["FilePath"]
      """  Path file location where the file was written.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.PayClassesDesc:str = obj["PayClassesDesc"]
      """  This field will hold the Description of the IDs in column PayClasses.  """  
      self.NonPayClasses:str = obj["NonPayClasses"]
      """  This field will have the list of PayClassIDs which are avaialble to be selected.  """  
      self.NonPayClassesDesc:str = obj["NonPayClassesDesc"]
      """  This field will hold the Description of the PayClassIDs available to be selected.  """  
      self.ServerFilePath:str = obj["ServerFilePath"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class CalculateOTDT_input:
   """ Required : 
   GroupID
   """  
   def __init__(self, obj):
      self.GroupID:str = obj["GroupID"]
      """  GroupID to calculate  """  
      pass

class CalculateOTDT_output:
   def __init__(self, obj):
      pass

class ClosePayrollGroup_input:
   """ Required : 
   groupId
   ds
   """  
   def __init__(self, obj):
      self.groupId:str = obj["groupId"]
      self.ds:list[Erp_Tablesets_ExtPRProcGrpTableset] = obj["ds"]
      pass

class ClosePayrollGroup_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ExtPRProcGrpTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   groupID
   """  
   def __init__(self, obj):
      self.groupID:str = obj["groupID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_ExtPRGrpEmpDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.GroupID:str = obj["GroupID"]
      """  Group ID  """  
      self.EmpID:str = obj["EmpID"]
      """  Employee ID  """  
      self.DtlNum:int = obj["DtlNum"]
      """  DtlNum  """  
      self.PayrollDate:str = obj["PayrollDate"]
      """  Date for the entered work/labor hours.  """  
      self.PayTypeID:str = obj["PayTypeID"]
      """  Pay Type selected for the hours detail record.  """  
      self.BaseHours:int = obj["BaseHours"]
      """  Number of Base Hours.  """  
      self.OTHours:int = obj["OTHours"]
      """  Number of overtime hours.  """  
      self.Hours3:int = obj["Hours3"]
      """  This are usually other hours apart from Regular and Overtime.  """  
      self.Hours3Code:str = obj["Hours3Code"]
      """  Pay Type ID meant for the Hours3 field.  """  
      self.SentToFile:bool = obj["SentToFile"]
      """  Indicates the record has been exported.  """  
      self.TempDept:str = obj["TempDept"]
      """  Department entered for the work/labor hours.  """  
      self.FromLabor:bool = obj["FromLabor"]
      """  Indicates the record was created from a Labor Entry.  """  
      self.Shift:int = obj["Shift"]
      """  Shift for the entered work/labor hours.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.TotalHours:int = obj["TotalHours"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ExtPRGrpEmpRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.GroupID:str = obj["GroupID"]
      """  Group ID  """  
      self.EmpID:str = obj["EmpID"]
      """  Employee being processed in the group.  """  
      self.PSDate:str = obj["PSDate"]
      """  Pay Period Start Date.  """  
      self.PEDate:str = obj["PEDate"]
      """  Pay Period End Date.  """  
      self.TotalBaseHours:int = obj["TotalBaseHours"]
      """  Total number of base hours.  """  
      self.TotalOTHours:int = obj["TotalOTHours"]
      """  Total number of overtime hours.  """  
      self.TotalDTHours:int = obj["TotalDTHours"]
      """  Total number of premium hours.  """  
      self.PayClassID:str = obj["PayClassID"]
      """  Payroll Class assigned to the Employee.  """  
      self.PayFreq:str = obj["PayFreq"]
      """  Pay frequency assigned to the Employee.  """  
      self.SentToFile:bool = obj["SentToFile"]
      """  Indicates this record has been exported.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.EmpTotalHours:int = obj["EmpTotalHours"]
      """  Total Hours for the Employee.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.EmpIDEmpName:str = obj["EmpIDEmpName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ExtPRProcGrpListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.GroupID:str = obj["GroupID"]
      """  Group ID  """  
      self.Status:str = obj["Status"]
      """  Indicates the Status of the Payroll Group. Currently we use three: New, Exported and Closed.  """  
      self.PEDate:str = obj["PEDate"]
      """  Payroll Pay Period Ending Date.  """  
      self.PayWeekly:bool = obj["PayWeekly"]
      """  Indicates the "Generate Hours" action will process employees who get paid every week.  """  
      self.PayBiWeekly:bool = obj["PayBiWeekly"]
      """  Indicates the "Generate Hours" action will process employees who get paid every two weeks.  """  
      self.PaySemiMonthly:bool = obj["PaySemiMonthly"]
      """  Indicates the "Generate Hours" action will process employees who get paid twice every month.  """  
      self.PayMonthly:bool = obj["PayMonthly"]
      """  Indicates the "Generate Hours" action will process employees who get paid once every month.  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  UserID of the Employee who created this group.  """  
      self.PayClasses:str = obj["PayClasses"]
      """  List of Payroll Classes that will be processed within the Payroll Group.  """  
      self.SentToFile:bool = obj["SentToFile"]
      """  Indicates the group has been exported to a file.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ExtPRProcGrpListTableset:
   def __init__(self, obj):
      self.ExtPRProcGrpList:list[Erp_Tablesets_ExtPRProcGrpListRow] = obj["ExtPRProcGrpList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_ExtPRProcGrpRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.GroupID:str = obj["GroupID"]
      """  Group ID  """  
      self.Status:str = obj["Status"]
      """  Indicates the Status of the Payroll Group. Currently we use three: New, Exported and Closed.  """  
      self.PEDate:str = obj["PEDate"]
      """  Payroll Pay Period Ending Date.  """  
      self.PayWeekly:bool = obj["PayWeekly"]
      """  Indicates the "Generate Hours" action will process employees who get paid every week.  """  
      self.PayBiWeekly:bool = obj["PayBiWeekly"]
      """  Indicates the "Generate Hours" action will process employees who get paid every two weeks.  """  
      self.PaySemiMonthly:bool = obj["PaySemiMonthly"]
      """  Indicates the "Generate Hours" action will process employees who get paid twice every month.  """  
      self.PayMonthly:bool = obj["PayMonthly"]
      """  Indicates the "Generate Hours" action will process employees who get paid once every month.  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  UserID of the Employee who created this group.  """  
      self.PayClasses:str = obj["PayClasses"]
      """  List of Payroll Classes that will be processed within the Payroll Group.  """  
      self.SentToFile:bool = obj["SentToFile"]
      """  Indicates the group has been exported to a file.  """  
      self.FilePath:str = obj["FilePath"]
      """  Path file location where the file was written.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.PayClassesDesc:str = obj["PayClassesDesc"]
      """  This field will hold the Description of the IDs in column PayClasses.  """  
      self.NonPayClasses:str = obj["NonPayClasses"]
      """  This field will have the list of PayClassIDs which are avaialble to be selected.  """  
      self.NonPayClassesDesc:str = obj["NonPayClassesDesc"]
      """  This field will hold the Description of the PayClassIDs available to be selected.  """  
      self.ServerFilePath:str = obj["ServerFilePath"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ExtPRProcGrpTableset:
   def __init__(self, obj):
      self.ExtPRProcGrp:list[Erp_Tablesets_ExtPRProcGrpRow] = obj["ExtPRProcGrp"]
      self.ExtPRGrpEmp:list[Erp_Tablesets_ExtPRGrpEmpRow] = obj["ExtPRGrpEmp"]
      self.ExtPRGrpEmpDtl:list[Erp_Tablesets_ExtPRGrpEmpDtlRow] = obj["ExtPRGrpEmpDtl"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtExtPRProcGrpTableset:
   def __init__(self, obj):
      self.ExtPRProcGrp:list[Erp_Tablesets_ExtPRProcGrpRow] = obj["ExtPRProcGrp"]
      self.ExtPRGrpEmp:list[Erp_Tablesets_ExtPRGrpEmpRow] = obj["ExtPRGrpEmp"]
      self.ExtPRGrpEmpDtl:list[Erp_Tablesets_ExtPRGrpEmpDtlRow] = obj["ExtPRGrpEmpDtl"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class FillEmployeeData_input:
   """ Required : 
   EmpID
   ds
   """  
   def __init__(self, obj):
      self.EmpID:str = obj["EmpID"]
      """  Employee ID selected  """  
      self.ds:list[Erp_Tablesets_ExtPRProcGrpTableset] = obj["ds"]
      pass

class FillEmployeeData_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ExtPRProcGrpTableset] = obj["ds"]
      self.msg:str = obj["parameters"]
      pass

      """  output parameters  """  

class GenerateHours_input:
   """ Required : 
   GroupID
   """  
   def __init__(self, obj):
      self.GroupID:str = obj["GroupID"]
      """  GroupID to generate  """  
      pass

class GenerateHours_output:
   def __init__(self, obj):
      pass

class GetByID_input:
   """ Required : 
   groupID
   """  
   def __init__(self, obj):
      self.groupID:str = obj["groupID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ExtPRProcGrpTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ExtPRProcGrpTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ExtPRProcGrpTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ExtPRProcGrpListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewExtPRGrpEmpDtl_input:
   """ Required : 
   ds
   groupID
   empID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ExtPRProcGrpTableset] = obj["ds"]
      self.groupID:str = obj["groupID"]
      self.empID:str = obj["empID"]
      pass

class GetNewExtPRGrpEmpDtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ExtPRProcGrpTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewExtPRGrpEmp_input:
   """ Required : 
   ds
   groupID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ExtPRProcGrpTableset] = obj["ds"]
      self.groupID:str = obj["groupID"]
      pass

class GetNewExtPRGrpEmp_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ExtPRProcGrpTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewExtPRProcGrp_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ExtPRProcGrpTableset] = obj["ds"]
      pass

class GetNewExtPRProcGrp_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ExtPRProcGrpTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseExtPRProcGrp
   whereClauseExtPRGrpEmp
   whereClauseExtPRGrpEmpDtl
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseExtPRProcGrp:str = obj["whereClauseExtPRProcGrp"]
      self.whereClauseExtPRGrpEmp:str = obj["whereClauseExtPRGrpEmp"]
      self.whereClauseExtPRGrpEmpDtl:str = obj["whereClauseExtPRGrpEmpDtl"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ExtPRProcGrpTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetWhereClause_input:
   """ Required : 
   delimiter
   ds
   """  
   def __init__(self, obj):
      self.delimiter:str = obj["delimiter"]
      """  Delimiter used in 'PayClass' field  """  
      self.ds:list[Erp_Tablesets_ExtPRProcGrpTableset] = obj["ds"]
      pass

class GetWhereClause_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.whereClause:str = obj["parameters"]
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
      self.ds:list[Erp_Tablesets_UpdExtExtPRProcGrpTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtExtPRProcGrpTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ExtPRProcGrpTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ExtPRProcGrpTableset] = obj["ds"]
      pass

      """  output parameters  """  

