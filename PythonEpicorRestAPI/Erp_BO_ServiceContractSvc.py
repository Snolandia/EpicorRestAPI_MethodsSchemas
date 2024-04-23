import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.ServiceContractSvc
# Description: Service Contract Business Object
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_ServiceContracts(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ServiceContracts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ServiceContracts
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FSContHdRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/ServiceContracts",headers=creds) as resp:
           return await resp.json()

async def post_ServiceContracts(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ServiceContracts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.FSContHdRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.FSContHdRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/ServiceContracts", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ServiceContracts_Company_ContractNum(Company, ContractNum, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ServiceContract item
   Description: Calls GetByID to retrieve the ServiceContract item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ServiceContract
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ContractNum: Desc: ContractNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.FSContHdRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/ServiceContracts(" + Company + "," + ContractNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ServiceContracts_Company_ContractNum(Company, ContractNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ServiceContract for the service
   Description: Calls UpdateExt to update ServiceContract. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ServiceContract
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ContractNum: Desc: ContractNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.FSContHdRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/ServiceContracts(" + Company + "," + ContractNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ServiceContracts_Company_ContractNum(Company, ContractNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ServiceContract item
   Description: Call UpdateExt to delete ServiceContract item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ServiceContract
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ContractNum: Desc: ContractNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/ServiceContracts(" + Company + "," + ContractNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_ServiceContracts_Company_ContractNum_FSContDts(Company, ContractNum, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get FSContDts items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_FSContDts1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ContractNum: Desc: ContractNum   Required: True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FSContDtRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/ServiceContracts(" + Company + "," + ContractNum + ")/FSContDts",headers=creds) as resp:
           return await resp.json()

async def get_ServiceContracts_Company_ContractNum_FSContDts_Company_ContractNum_ContractLine(Company, ContractNum, ContractLine, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the FSContDt item
   Description: Calls GetByID to retrieve the FSContDt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_FSContDt1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ContractNum: Desc: ContractNum   Required: True
      :param ContractLine: Desc: ContractLine   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.FSContDtRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/ServiceContracts(" + Company + "," + ContractNum + ")/FSContDts(" + Company + "," + ContractNum + "," + ContractLine + ")",headers=creds) as resp:
           return await resp.json()

async def get_ServiceContracts_Company_ContractNum_FSRenewals(Company, ContractNum, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get FSRenewals items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_FSRenewals1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ContractNum: Desc: ContractNum   Required: True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FSRenewalRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/ServiceContracts(" + Company + "," + ContractNum + ")/FSRenewals",headers=creds) as resp:
           return await resp.json()

async def get_ServiceContracts_Company_ContractNum_FSRenewals_Company_ContractNum_RenewalNbr(Company, ContractNum, RenewalNbr, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the FSRenewal item
   Description: Calls GetByID to retrieve the FSRenewal item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_FSRenewal1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ContractNum: Desc: ContractNum   Required: True
      :param RenewalNbr: Desc: RenewalNbr   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.FSRenewalRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/ServiceContracts(" + Company + "," + ContractNum + ")/FSRenewals(" + Company + "," + ContractNum + "," + RenewalNbr + ")",headers=creds) as resp:
           return await resp.json()

async def get_ServiceContracts_Company_ContractNum_FSContLabExpRates(Company, ContractNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get FSContLabExpRates items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_FSContLabExpRates1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ContractNum: Desc: ContractNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FSContLabExpRateRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/ServiceContracts(" + Company + "," + ContractNum + ")/FSContLabExpRates",headers=creds) as resp:
           return await resp.json()

async def get_ServiceContracts_Company_ContractNum_FSContLabExpRates_Company_ContractNum_ExpenseCode(Company, ContractNum, ExpenseCode, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the FSContLabExpRate item
   Description: Calls GetByID to retrieve the FSContLabExpRate item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_FSContLabExpRate1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ContractNum: Desc: ContractNum   Required: True
      :param ExpenseCode: Desc: ExpenseCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.FSContLabExpRateRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/ServiceContracts(" + Company + "," + ContractNum + ")/FSContLabExpRates(" + Company + "," + ContractNum + "," + ExpenseCode + ")",headers=creds) as resp:
           return await resp.json()

async def get_FSContDts(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get FSContDts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_FSContDts
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FSContDtRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/FSContDts",headers=creds) as resp:
           return await resp.json()

async def post_FSContDts(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_FSContDts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.FSContDtRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.FSContDtRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/FSContDts", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_FSContDts_Company_ContractNum_ContractLine(Company, ContractNum, ContractLine, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the FSContDt item
   Description: Calls GetByID to retrieve the FSContDt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_FSContDt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ContractNum: Desc: ContractNum   Required: True
      :param ContractLine: Desc: ContractLine   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.FSContDtRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/FSContDts(" + Company + "," + ContractNum + "," + ContractLine + ")",headers=creds) as resp:
           return await resp.json()

async def patch_FSContDts_Company_ContractNum_ContractLine(Company, ContractNum, ContractLine, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update FSContDt for the service
   Description: Calls UpdateExt to update FSContDt. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_FSContDt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ContractNum: Desc: ContractNum   Required: True
      :param ContractLine: Desc: ContractLine   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.FSContDtRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/FSContDts(" + Company + "," + ContractNum + "," + ContractLine + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_FSContDts_Company_ContractNum_ContractLine(Company, ContractNum, ContractLine, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete FSContDt item
   Description: Call UpdateExt to delete FSContDt item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_FSContDt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ContractNum: Desc: ContractNum   Required: True
      :param ContractLine: Desc: ContractLine   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/FSContDts(" + Company + "," + ContractNum + "," + ContractLine + ")",headers=creds) as resp:
           return await resp.json()

async def get_FSContDts_Company_ContractNum_ContractLine_FSContSNs(Company, ContractNum, ContractLine, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get FSContSNs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_FSContSNs1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ContractNum: Desc: ContractNum   Required: True
      :param ContractLine: Desc: ContractLine   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FSContSNRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/FSContDts(" + Company + "," + ContractNum + "," + ContractLine + ")/FSContSNs",headers=creds) as resp:
           return await resp.json()

async def get_FSContDts_Company_ContractNum_ContractLine_FSContSNs_Company_ContractNum_ContractLine_PartNum_SerialNumber(Company, ContractNum, ContractLine, PartNum, SerialNumber, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the FSContSN item
   Description: Calls GetByID to retrieve the FSContSN item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_FSContSN1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ContractNum: Desc: ContractNum   Required: True
      :param ContractLine: Desc: ContractLine   Required: True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param SerialNumber: Desc: SerialNumber   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.FSContSNRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/FSContDts(" + Company + "," + ContractNum + "," + ContractLine + ")/FSContSNs(" + Company + "," + ContractNum + "," + ContractLine + "," + PartNum + "," + SerialNumber + ")",headers=creds) as resp:
           return await resp.json()

async def get_FSContSNs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get FSContSNs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_FSContSNs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FSContSNRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/FSContSNs",headers=creds) as resp:
           return await resp.json()

async def post_FSContSNs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_FSContSNs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.FSContSNRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.FSContSNRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/FSContSNs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_FSContSNs_Company_ContractNum_ContractLine_PartNum_SerialNumber(Company, ContractNum, ContractLine, PartNum, SerialNumber, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the FSContSN item
   Description: Calls GetByID to retrieve the FSContSN item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_FSContSN
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ContractNum: Desc: ContractNum   Required: True
      :param ContractLine: Desc: ContractLine   Required: True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param SerialNumber: Desc: SerialNumber   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.FSContSNRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/FSContSNs(" + Company + "," + ContractNum + "," + ContractLine + "," + PartNum + "," + SerialNumber + ")",headers=creds) as resp:
           return await resp.json()

async def patch_FSContSNs_Company_ContractNum_ContractLine_PartNum_SerialNumber(Company, ContractNum, ContractLine, PartNum, SerialNumber, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update FSContSN for the service
   Description: Calls UpdateExt to update FSContSN. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_FSContSN
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ContractNum: Desc: ContractNum   Required: True
      :param ContractLine: Desc: ContractLine   Required: True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param SerialNumber: Desc: SerialNumber   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.FSContSNRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/FSContSNs(" + Company + "," + ContractNum + "," + ContractLine + "," + PartNum + "," + SerialNumber + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_FSContSNs_Company_ContractNum_ContractLine_PartNum_SerialNumber(Company, ContractNum, ContractLine, PartNum, SerialNumber, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete FSContSN item
   Description: Call UpdateExt to delete FSContSN item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_FSContSN
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ContractNum: Desc: ContractNum   Required: True
      :param ContractLine: Desc: ContractLine   Required: True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param SerialNumber: Desc: SerialNumber   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/FSContSNs(" + Company + "," + ContractNum + "," + ContractLine + "," + PartNum + "," + SerialNumber + ")",headers=creds) as resp:
           return await resp.json()

async def get_FSRenewals(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get FSRenewals items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_FSRenewals
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FSRenewalRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/FSRenewals",headers=creds) as resp:
           return await resp.json()

async def post_FSRenewals(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_FSRenewals
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.FSRenewalRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.FSRenewalRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/FSRenewals", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_FSRenewals_Company_ContractNum_RenewalNbr(Company, ContractNum, RenewalNbr, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the FSRenewal item
   Description: Calls GetByID to retrieve the FSRenewal item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_FSRenewal
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ContractNum: Desc: ContractNum   Required: True
      :param RenewalNbr: Desc: RenewalNbr   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.FSRenewalRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/FSRenewals(" + Company + "," + ContractNum + "," + RenewalNbr + ")",headers=creds) as resp:
           return await resp.json()

async def patch_FSRenewals_Company_ContractNum_RenewalNbr(Company, ContractNum, RenewalNbr, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update FSRenewal for the service
   Description: Calls UpdateExt to update FSRenewal. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_FSRenewal
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ContractNum: Desc: ContractNum   Required: True
      :param RenewalNbr: Desc: RenewalNbr   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.FSRenewalRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/FSRenewals(" + Company + "," + ContractNum + "," + RenewalNbr + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_FSRenewals_Company_ContractNum_RenewalNbr(Company, ContractNum, RenewalNbr, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete FSRenewal item
   Description: Call UpdateExt to delete FSRenewal item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_FSRenewal
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ContractNum: Desc: ContractNum   Required: True
      :param RenewalNbr: Desc: RenewalNbr   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/FSRenewals(" + Company + "," + ContractNum + "," + RenewalNbr + ")",headers=creds) as resp:
           return await resp.json()

async def get_FSRenewals_Company_ContractNum_RenewalNbr_FSRenewalDts(Company, ContractNum, RenewalNbr, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get FSRenewalDts items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_FSRenewalDts1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ContractNum: Desc: ContractNum   Required: True
      :param RenewalNbr: Desc: RenewalNbr   Required: True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FSRenewalDtRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/FSRenewals(" + Company + "," + ContractNum + "," + RenewalNbr + ")/FSRenewalDts",headers=creds) as resp:
           return await resp.json()

async def get_FSRenewals_Company_ContractNum_RenewalNbr_FSRenewalDts_Company_ContractNum_RenewalNbr_RenewalLine(Company, ContractNum, RenewalNbr, RenewalLine, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the FSRenewalDt item
   Description: Calls GetByID to retrieve the FSRenewalDt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_FSRenewalDt1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ContractNum: Desc: ContractNum   Required: True
      :param RenewalNbr: Desc: RenewalNbr   Required: True
      :param RenewalLine: Desc: RenewalLine   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.FSRenewalDtRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/FSRenewals(" + Company + "," + ContractNum + "," + RenewalNbr + ")/FSRenewalDts(" + Company + "," + ContractNum + "," + RenewalNbr + "," + RenewalLine + ")",headers=creds) as resp:
           return await resp.json()

async def get_FSRenewalDts(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get FSRenewalDts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_FSRenewalDts
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FSRenewalDtRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/FSRenewalDts",headers=creds) as resp:
           return await resp.json()

async def post_FSRenewalDts(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_FSRenewalDts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.FSRenewalDtRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.FSRenewalDtRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/FSRenewalDts", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_FSRenewalDts_Company_ContractNum_RenewalNbr_RenewalLine(Company, ContractNum, RenewalNbr, RenewalLine, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the FSRenewalDt item
   Description: Calls GetByID to retrieve the FSRenewalDt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_FSRenewalDt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ContractNum: Desc: ContractNum   Required: True
      :param RenewalNbr: Desc: RenewalNbr   Required: True
      :param RenewalLine: Desc: RenewalLine   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.FSRenewalDtRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/FSRenewalDts(" + Company + "," + ContractNum + "," + RenewalNbr + "," + RenewalLine + ")",headers=creds) as resp:
           return await resp.json()

async def patch_FSRenewalDts_Company_ContractNum_RenewalNbr_RenewalLine(Company, ContractNum, RenewalNbr, RenewalLine, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update FSRenewalDt for the service
   Description: Calls UpdateExt to update FSRenewalDt. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_FSRenewalDt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ContractNum: Desc: ContractNum   Required: True
      :param RenewalNbr: Desc: RenewalNbr   Required: True
      :param RenewalLine: Desc: RenewalLine   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.FSRenewalDtRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/FSRenewalDts(" + Company + "," + ContractNum + "," + RenewalNbr + "," + RenewalLine + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_FSRenewalDts_Company_ContractNum_RenewalNbr_RenewalLine(Company, ContractNum, RenewalNbr, RenewalLine, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete FSRenewalDt item
   Description: Call UpdateExt to delete FSRenewalDt item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_FSRenewalDt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ContractNum: Desc: ContractNum   Required: True
      :param RenewalNbr: Desc: RenewalNbr   Required: True
      :param RenewalLine: Desc: RenewalLine   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/FSRenewalDts(" + Company + "," + ContractNum + "," + RenewalNbr + "," + RenewalLine + ")",headers=creds) as resp:
           return await resp.json()

async def get_FSRenewalDts_Company_ContractNum_RenewalNbr_RenewalLine_FSRenewalSNs(Company, ContractNum, RenewalNbr, RenewalLine, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get FSRenewalSNs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_FSRenewalSNs1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ContractNum: Desc: ContractNum   Required: True
      :param RenewalNbr: Desc: RenewalNbr   Required: True
      :param RenewalLine: Desc: RenewalLine   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FSRenewalSNRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/FSRenewalDts(" + Company + "," + ContractNum + "," + RenewalNbr + "," + RenewalLine + ")/FSRenewalSNs",headers=creds) as resp:
           return await resp.json()

async def get_FSRenewalDts_Company_ContractNum_RenewalNbr_RenewalLine_FSRenewalSNs_Company_ContractNum_RenewalNbr_RenewalLine_PartNum_SerialNumber(Company, ContractNum, RenewalNbr, RenewalLine, PartNum, SerialNumber, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the FSRenewalSN item
   Description: Calls GetByID to retrieve the FSRenewalSN item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_FSRenewalSN1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ContractNum: Desc: ContractNum   Required: True
      :param RenewalNbr: Desc: RenewalNbr   Required: True
      :param RenewalLine: Desc: RenewalLine   Required: True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param SerialNumber: Desc: SerialNumber   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.FSRenewalSNRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/FSRenewalDts(" + Company + "," + ContractNum + "," + RenewalNbr + "," + RenewalLine + ")/FSRenewalSNs(" + Company + "," + ContractNum + "," + RenewalNbr + "," + RenewalLine + "," + PartNum + "," + SerialNumber + ")",headers=creds) as resp:
           return await resp.json()

async def get_FSRenewalSNs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get FSRenewalSNs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_FSRenewalSNs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FSRenewalSNRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/FSRenewalSNs",headers=creds) as resp:
           return await resp.json()

async def post_FSRenewalSNs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_FSRenewalSNs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.FSRenewalSNRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.FSRenewalSNRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/FSRenewalSNs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_FSRenewalSNs_Company_ContractNum_RenewalNbr_RenewalLine_PartNum_SerialNumber(Company, ContractNum, RenewalNbr, RenewalLine, PartNum, SerialNumber, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the FSRenewalSN item
   Description: Calls GetByID to retrieve the FSRenewalSN item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_FSRenewalSN
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ContractNum: Desc: ContractNum   Required: True
      :param RenewalNbr: Desc: RenewalNbr   Required: True
      :param RenewalLine: Desc: RenewalLine   Required: True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param SerialNumber: Desc: SerialNumber   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.FSRenewalSNRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/FSRenewalSNs(" + Company + "," + ContractNum + "," + RenewalNbr + "," + RenewalLine + "," + PartNum + "," + SerialNumber + ")",headers=creds) as resp:
           return await resp.json()

async def patch_FSRenewalSNs_Company_ContractNum_RenewalNbr_RenewalLine_PartNum_SerialNumber(Company, ContractNum, RenewalNbr, RenewalLine, PartNum, SerialNumber, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update FSRenewalSN for the service
   Description: Calls UpdateExt to update FSRenewalSN. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_FSRenewalSN
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ContractNum: Desc: ContractNum   Required: True
      :param RenewalNbr: Desc: RenewalNbr   Required: True
      :param RenewalLine: Desc: RenewalLine   Required: True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param SerialNumber: Desc: SerialNumber   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.FSRenewalSNRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/FSRenewalSNs(" + Company + "," + ContractNum + "," + RenewalNbr + "," + RenewalLine + "," + PartNum + "," + SerialNumber + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_FSRenewalSNs_Company_ContractNum_RenewalNbr_RenewalLine_PartNum_SerialNumber(Company, ContractNum, RenewalNbr, RenewalLine, PartNum, SerialNumber, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete FSRenewalSN item
   Description: Call UpdateExt to delete FSRenewalSN item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_FSRenewalSN
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ContractNum: Desc: ContractNum   Required: True
      :param RenewalNbr: Desc: RenewalNbr   Required: True
      :param RenewalLine: Desc: RenewalLine   Required: True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param SerialNumber: Desc: SerialNumber   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/FSRenewalSNs(" + Company + "," + ContractNum + "," + RenewalNbr + "," + RenewalLine + "," + PartNum + "," + SerialNumber + ")",headers=creds) as resp:
           return await resp.json()

async def get_FSContLabExpRates(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get FSContLabExpRates items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_FSContLabExpRates
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FSContLabExpRateRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/FSContLabExpRates",headers=creds) as resp:
           return await resp.json()

async def post_FSContLabExpRates(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_FSContLabExpRates
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.FSContLabExpRateRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.FSContLabExpRateRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/FSContLabExpRates", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_FSContLabExpRates_Company_ContractNum_ExpenseCode(Company, ContractNum, ExpenseCode, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the FSContLabExpRate item
   Description: Calls GetByID to retrieve the FSContLabExpRate item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_FSContLabExpRate
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ContractNum: Desc: ContractNum   Required: True
      :param ExpenseCode: Desc: ExpenseCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.FSContLabExpRateRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/FSContLabExpRates(" + Company + "," + ContractNum + "," + ExpenseCode + ")",headers=creds) as resp:
           return await resp.json()

async def patch_FSContLabExpRates_Company_ContractNum_ExpenseCode(Company, ContractNum, ExpenseCode, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update FSContLabExpRate for the service
   Description: Calls UpdateExt to update FSContLabExpRate. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_FSContLabExpRate
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ContractNum: Desc: ContractNum   Required: True
      :param ExpenseCode: Desc: ExpenseCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.FSContLabExpRateRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/FSContLabExpRates(" + Company + "," + ContractNum + "," + ExpenseCode + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_FSContLabExpRates_Company_ContractNum_ExpenseCode(Company, ContractNum, ExpenseCode, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete FSContLabExpRate item
   Description: Call UpdateExt to delete FSContLabExpRate item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_FSContLabExpRate
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ContractNum: Desc: ContractNum   Required: True
      :param ExpenseCode: Desc: ExpenseCode   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/FSContLabExpRates(" + Company + "," + ContractNum + "," + ExpenseCode + ")",headers=creds) as resp:
           return await resp.json()

async def get_FSContOrderDtlLists(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get FSContOrderDtlLists items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_FSContOrderDtlLists
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FSContOrderDtlListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/FSContOrderDtlLists",headers=creds) as resp:
           return await resp.json()

async def post_FSContOrderDtlLists(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_FSContOrderDtlLists
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.FSContOrderDtlListRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.FSContOrderDtlListRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/FSContOrderDtlLists", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_FSContOrderDtlLists_SysRowID(SysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the FSContOrderDtlList item
   Description: Calls GetByID to retrieve the FSContOrderDtlList item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_FSContOrderDtlList
      :param SysRowID: Desc: SysRowID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.FSContOrderDtlListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/FSContOrderDtlLists(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_FSContOrderDtlLists_SysRowID(SysRowID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update FSContOrderDtlList for the service
   Description: Calls UpdateExt to update FSContOrderDtlList. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_FSContOrderDtlList
      :param SysRowID: Desc: SysRowID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.FSContOrderDtlListRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/FSContOrderDtlLists(" + SysRowID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_FSContOrderDtlLists_SysRowID(SysRowID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete FSContOrderDtlList item
   Description: Call UpdateExt to delete FSContOrderDtlList item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_FSContOrderDtlList
      :param SysRowID: Desc: SysRowID   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/FSContOrderDtlLists(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def get_SelectedSerialNumbers(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get SelectedSerialNumbers items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_SelectedSerialNumbers
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SelectedSerialNumbersRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/SelectedSerialNumbers",headers=creds) as resp:
           return await resp.json()

async def post_SelectedSerialNumbers(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_SelectedSerialNumbers
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.SelectedSerialNumbersRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.SelectedSerialNumbersRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/SelectedSerialNumbers", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_SelectedSerialNumbers_Company_PartNum_SerialNumber(Company, PartNum, SerialNumber, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the SelectedSerialNumber item
   Description: Calls GetByID to retrieve the SelectedSerialNumber item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SelectedSerialNumber
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param SerialNumber: Desc: SerialNumber   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.SelectedSerialNumbersRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/SelectedSerialNumbers(" + Company + "," + PartNum + "," + SerialNumber + ")",headers=creds) as resp:
           return await resp.json()

async def patch_SelectedSerialNumbers_Company_PartNum_SerialNumber(Company, PartNum, SerialNumber, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update SelectedSerialNumber for the service
   Description: Calls UpdateExt to update SelectedSerialNumber. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_SelectedSerialNumber
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param SerialNumber: Desc: SerialNumber   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.SelectedSerialNumbersRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/SelectedSerialNumbers(" + Company + "," + PartNum + "," + SerialNumber + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_SelectedSerialNumbers_Company_PartNum_SerialNumber(Company, PartNum, SerialNumber, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete SelectedSerialNumber item
   Description: Call UpdateExt to delete SelectedSerialNumber item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_SelectedSerialNumber
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param SerialNumber: Desc: SerialNumber   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/SelectedSerialNumbers(" + Company + "," + PartNum + "," + SerialNumber + ")",headers=creds) as resp:
           return await resp.json()

async def get_SNFormats(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get SNFormats items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_SNFormats
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SNFormatRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/SNFormats",headers=creds) as resp:
           return await resp.json()

async def post_SNFormats(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_SNFormats
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.SNFormatRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.SNFormatRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/SNFormats", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_SNFormats_Company_PartNum_Plant(Company, PartNum, Plant, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the SNFormat item
   Description: Calls GetByID to retrieve the SNFormat item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SNFormat
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.SNFormatRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/SNFormats(" + Company + "," + PartNum + "," + Plant + ")",headers=creds) as resp:
           return await resp.json()

async def patch_SNFormats_Company_PartNum_Plant(Company, PartNum, Plant, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update SNFormat for the service
   Description: Calls UpdateExt to update SNFormat. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_SNFormat
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.SNFormatRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/SNFormats(" + Company + "," + PartNum + "," + Plant + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_SNFormats_Company_PartNum_Plant(Company, PartNum, Plant, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete SNFormat item
   Description: Call UpdateExt to delete SNFormat item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_SNFormat
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/SNFormats(" + Company + "," + PartNum + "," + Plant + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FSContHdListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseFSContHd, whereClauseFSContDt, whereClauseFSContSN, whereClauseFSRenewal, whereClauseFSRenewalDt, whereClauseFSRenewalSN, whereClauseFSContLabExpRate, whereClauseFSContOrderDtlList, whereClauseSelectedSerialNumbers, whereClauseSNFormat, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
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
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseFSContHd=" + whereClauseFSContHd
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseFSContDt=" + whereClauseFSContDt
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseFSContSN=" + whereClauseFSContSN
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseFSRenewal=" + whereClauseFSRenewal
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseFSRenewalDt=" + whereClauseFSRenewalDt
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseFSRenewalSN=" + whereClauseFSRenewalSN
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseFSContLabExpRate=" + whereClauseFSContLabExpRate
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseFSContOrderDtlList=" + whereClauseFSContOrderDtlList
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseSelectedSerialNumbers=" + whereClauseSelectedSerialNumbers
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseSNFormat=" + whereClauseSNFormat
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(contractNum, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
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
   params += "contractNum=" + contractNum

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_ActivateContract(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ActivateContract
   Description: Method to call when activating the contract.
   OperationID: ActivateContract
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ActivateContract_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ActivateContract_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeFSContDtBillEndDate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeFSContDtBillEndDate
   Description: Method to call when changing the billing end date on the contract detail record.
Updates FSContDt with values based on the new billing start date.
   OperationID: ChangeFSContDtBillEndDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFSContDtBillEndDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFSContDtBillEndDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeFSContDtBillStartDate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeFSContDtBillStartDate
   Description: Method to call when changing the billing start date on the contract detail record.
Updates FSContDt with values based on the new billing start date.
   OperationID: ChangeFSContDtBillStartDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFSContDtBillStartDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFSContDtBillStartDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeFSContDtContractQty(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeFSContDtContractQty
   Description: Method to call when changing the contract quantity on the contract detail record.
Recalculates Ext Prices on FSContDt with values from the new quantity.
   OperationID: ChangeFSContDtContractQty
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFSContDtContractQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFSContDtContractQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeFSContDtOrderLine(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeFSContDtOrderLine
   Description: Method to call when changing the order line on the contract detail record.
Validates the line and updates FSContDt with values from the order line.
   OperationID: ChangeFSContDtOrderLine
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFSContDtOrderLine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFSContDtOrderLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeFSContDtOrderNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeFSContDtOrderNum
   Description: Method to call when changing the order number on the contract detail record.
Validates the number and updates FSContDt with values from the order.
   OperationID: ChangeFSContDtOrderNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFSContDtOrderNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFSContDtOrderNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeFSContDtPartNumWithSubs(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeFSContDtPartNumWithSubs
   Description: Method to call when changing the part number on the contract detail record.
Updates FSContDt with values from the part number. If substitute PartNum is provided,
it will use the substitute part instead of the proposed part.
Prior to calling this method, the CheckPartNumChange method should be run
to validate the part.
   OperationID: ChangeFSContDtPartNumWithSubs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFSContDtPartNumWithSubs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFSContDtPartNumWithSubs_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeFSContDtPartNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeFSContDtPartNum
   Description: Method to call when changing the part number on the contract detail record.
Updates FSContDt with values from the part number.
Prior to calling this method, the CheckPartNumChange method should be run
to validate the part.
   OperationID: ChangeFSContDtPartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFSContDtPartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFSContDtPartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeFSContDtPricePerUnit(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeFSContDtPricePerUnit
   Description: Method to call when changing the price per unit on the contract detail record.
Recalculates Ext Prices on FSContDt with values from the new price per unit.
   OperationID: ChangeFSContDtPricePerUnit
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFSContDtPricePerUnit_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFSContDtPricePerUnit_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeFSContDtProdCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeFSContDtProdCode
   Description: Method to call when changing the product code on the contract detail record.
Validates the code and updates FSContDt with values from the product code.
   OperationID: ChangeFSContDtProdCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFSContDtProdCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFSContDtProdCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeFSContDtProjectID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeFSContDtProjectID
   Description: Method to call when changing the project id on the contract detail record.
Validates the id and updates FSContDt with values from the project.
   OperationID: ChangeFSContDtProjectID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFSContDtProjectID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFSContDtProjectID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeFSContDtXPartNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeFSContDtXPartNum
   Description: Method to call when changing the customer part number (XPartNum) on the
contract detail record.
Updates FSContDt with values from the customer part.
   OperationID: ChangeFSContDtXPartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFSContDtXPartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFSContDtXPartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeFSContHdActiveDate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeFSContHdActiveDate
   Description: Method to call when changing the effective date on the contract header record.
Updates FSContHd with values based on the new effective date.
   OperationID: ChangeFSContHdActiveDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFSContHdActiveDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFSContHdActiveDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeFSContHdBTCusNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeFSContHdBTCusNum
   Description: Method to call when changing the customer id on the contract header record.
Validates the customer id and updates FSContHd with values from the customer.
   OperationID: ChangeFSContHdBTCusNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFSContHdBTCusNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFSContHdBTCusNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeFSContHdContractCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeFSContHdContractCode
   Description: Method to call when changing the contract code on the contract header record.
Validates the code and updates FSContHd with values from the contract.
   OperationID: ChangeFSContHdContractCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFSContHdContractCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFSContHdContractCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeFSContHdCurrencyCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeFSContHdCurrencyCode
   Description: Method to call when changing the currency code on the contract header record.
Validates the code and updates FSContHd with values from the currency.
   OperationID: ChangeFSContHdCurrencyCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFSContHdCurrencyCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFSContHdCurrencyCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeFSContHdCustID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeFSContHdCustID
   Description: Method to call when changing the customer id on the contract header record.
Validates the customer id and updates FSContHd with values from the customer.
   OperationID: ChangeFSContHdCustID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFSContHdCustID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFSContHdCustID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeFSContHdDeferredRev(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeFSContHdDeferredRev
   Description: Method to call when changing the Deferred Revenue flag on the contract header record.
   OperationID: ChangeFSContHdDeferredRev
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFSContHdDeferredRev_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFSContHdDeferredRev_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeFSContHdDuration(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeFSContHdDuration
   Description: Method to call when changing the duration on the contract header record.
Updates FSContHd with values based on the new duration.
   OperationID: ChangeFSContHdDuration
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFSContHdDuration_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFSContHdDuration_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeFSContHdFiscalCalendarID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeFSContHdFiscalCalendarID
   Description: Method to call when changing the Fiscal Calendar on the contract header record.
   OperationID: ChangeFSContHdFiscalCalendarID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFSContHdFiscalCalendarID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFSContHdFiscalCalendarID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeFSContHdModifier(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeFSContHdModifier
   Description: Method to call when changing the Modifier on the contract header record.
Updates FSContHd with values based on the new Modifier.
   OperationID: ChangeFSContHdModifier
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFSContHdModifier_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFSContHdModifier_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeFSContHdPrcConNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeFSContHdPrcConNum
   Description: Method to call when changing the customer contact number on the contract header record.
Validates the number and updates FSContHd with values from the contact.
   OperationID: ChangeFSContHdPrcConNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFSContHdPrcConNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFSContHdPrcConNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeFSContHdPricePer(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeFSContHdPricePer
   Description: Method to call when changing the PricePer on the contract header record.
Updates FSContHd with values based on the new PricePer.
   OperationID: ChangeFSContHdPricePer
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFSContHdPricePer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFSContHdPricePer_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeFSContHdQuotedContract(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeFSContHdQuotedContract
   Description: Method to call when changing the Quoted Contract flag on the contract header record.
   OperationID: ChangeFSContHdQuotedContract
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFSContHdQuotedContract_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFSContHdQuotedContract_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeFSContHdRACode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeFSContHdRACode
   Description: Method to call when changing the RACode on the contract header record.
   OperationID: ChangeFSContHdRACode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFSContHdRACode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFSContHdRACode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeFSContHdRecurringFreq(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeFSContHdRecurringFreq
   Description: Method to call when changing the RecurringFreq on the contract header record.
Updates FSContHd with values based on the new RecurringFreq.
   OperationID: ChangeFSContHdRecurringFreq
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFSContHdRecurringFreq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFSContHdRecurringFreq_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeFSContHdShipToCustID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeFSContHdShipToCustID
   Description: Method to call when changing the ShipTo Customer ID on the contract header record.
Validates the ShipTo Customer ID and updates FSContHd with values from the customer.
   OperationID: ChangeFSContHdShipToCustID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFSContHdShipToCustID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFSContHdShipToCustID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeFSContHdShipToNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeFSContHdShipToNum
   Description: Method to call when changing the ship to on the contract header record.
Validates the number and updates FSContHd with values from the ship to.
   OperationID: ChangeFSContHdShipToNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFSContHdShipToNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFSContHdShipToNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeFSContHdShpConNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeFSContHdShpConNum
   Description: Method to call when changing the ship to contact on the contract header record.
Validates the contact and updates FSContHd with values from the ship to contact.
   OperationID: ChangeFSContHdShpConNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFSContHdShpConNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFSContHdShpConNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeFSContHdSuspended(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeFSContHdSuspended
   Description: Method to call when changing the Suspended flag on the contract header record.
This method determines if the contract has outstanding invoice revenue amortization
schedules that need to be updated to be put on hold or not. If InvcDtlRASch records
exist then a message will be returned to the user to let the user decide whether to
continue the update of invoice revenue schedules or not. The FSContHd.Suspended is
updated right away if no related invoice schedule exists.
   OperationID: ChangeFSContHdSuspended
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFSContHdSuspended_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFSContHdSuspended_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeFSContHdTaskSetID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeFSContHdTaskSetID
   Description: Method to call when changing the Task Set ID on the contract header record.
   OperationID: ChangeFSContHdTaskSetID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFSContHdTaskSetID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFSContHdTaskSetID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeFSContHdTaxCatID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeFSContHdTaxCatID
   Description: Method to call when changing the tax category id on the contract header record.
Validates the id and updates FSContHd with values from the tax category.
   OperationID: ChangeFSContHdTaxCatID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFSContHdTaxCatID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFSContHdTaxCatID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeFSContHdRecurringInv(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeFSContHdRecurringInv
   Description: Method to call when changing the recurring invoice flag on the contract header record.
   OperationID: ChangeFSContHdRecurringInv
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFSContHdRecurringInv_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFSContHdRecurringInv_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeFSContHDUseOTS(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeFSContHDUseOTS
   Description: Method to call when changing the UseOTS field the contract header record.
Refreshes the address list and contact info
   OperationID: ChangeFSContHDUseOTS
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFSContHDUseOTS_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFSContHDUseOTS_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeFSRenewalContractCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeFSRenewalContractCode
   Description: Method to call when changing the contract code on the contract renewal header record.
Validates the code and updates FSRenewal with values from the contract code defaults.
   OperationID: ChangeFSRenewalContractCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFSRenewalContractCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFSRenewalContractCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeFSRenewalDeferredRev(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeFSRenewalDeferredRev
   Description: Method to call when changing the Deferred Revenue flag on the contract renewal header record.
   OperationID: ChangeFSRenewalDeferredRev
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFSRenewalDeferredRev_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFSRenewalDeferredRev_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeFSRenewalDtBillEndDate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeFSRenewalDtBillEndDate
   Description: Method to call when changing the billing end date on the contract renewal detail record.
Updates FSRenewalDt with values based on the new billing start date.
   OperationID: ChangeFSRenewalDtBillEndDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFSRenewalDtBillEndDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFSRenewalDtBillEndDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeFSRenewalDtBillStartDate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeFSRenewalDtBillStartDate
   Description: Method to call when changing the billing start date on the contract renewal detail record.
Updates FSRenewalDt with values based on the new billing start date.
   OperationID: ChangeFSRenewalDtBillStartDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFSRenewalDtBillStartDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFSRenewalDtBillStartDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeFSRenewalDtContractQty(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeFSRenewalDtContractQty
   Description: Method to call when changing the contract quantity on the contract renewal detail record.
Recalculates Ext Prices on FSRenewalDt with values from the new quantity.
   OperationID: ChangeFSRenewalDtContractQty
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFSRenewalDtContractQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFSRenewalDtContractQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeFSRenewalDtIncreasePct(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeFSRenewalDtIncreasePct
   Description: Method to call when changing the increase percent on the contract renewal detail record.
Recalculates Prices on FSRenewalDt with values from the new increase percent.
   OperationID: ChangeFSRenewalDtIncreasePct
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFSRenewalDtIncreasePct_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFSRenewalDtIncreasePct_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeFSRenewalDtOrderLine(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeFSRenewalDtOrderLine
   Description: Method to call when changing the order line on the contract renewal detail record.
Validates the line and updates FSRenewalDt with values from the order line.
   OperationID: ChangeFSRenewalDtOrderLine
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFSRenewalDtOrderLine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFSRenewalDtOrderLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeFSRenewalDtOrderNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeFSRenewalDtOrderNum
   Description: Method to call when changing the order number on the contract renewal detail record.
Validates the number and updates FSRenewalDt with values from the order.
   OperationID: ChangeFSRenewalDtOrderNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFSRenewalDtOrderNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFSRenewalDtOrderNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeFSRenewalDtPartNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeFSRenewalDtPartNum
   Description: Method to call when changing the part number on the contract renewal detail record.
Updates FSRenewalDt with values from the part number.
Prior to calling this method, the CheckPartNumChange method should be run
to validate the part.
   OperationID: ChangeFSRenewalDtPartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFSRenewalDtPartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFSRenewalDtPartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeFSRenewalDtPartNumWithSubs(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeFSRenewalDtPartNumWithSubs
   Description: Method to call when changing the part number on the contract renewal detail record.
Updates FSRenewalDt with values from the part number.
Prior to calling this method, the CheckPartNumChange method should be run
to validate the part.
   OperationID: ChangeFSRenewalDtPartNumWithSubs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFSRenewalDtPartNumWithSubs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFSRenewalDtPartNumWithSubs_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeFSRenewalDtPricePerUnit(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeFSRenewalDtPricePerUnit
   Description: Method to call when changing the price per unit on the contract renewal detail record.
Recalculates Ext Prices on FSRenewalDt with values from the new price per unit.
   OperationID: ChangeFSRenewalDtPricePerUnit
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFSRenewalDtPricePerUnit_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFSRenewalDtPricePerUnit_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeFSRenewalDtProdCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeFSRenewalDtProdCode
   Description: Method to call when changing the product code on the contract renewal detail record.
Validates the code and updates FSRenewalDt with values from the product code.
   OperationID: ChangeFSRenewalDtProdCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFSRenewalDtProdCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFSRenewalDtProdCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeFSRenewalDtProjectID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeFSRenewalDtProjectID
   Description: Method to call when changing the project id on the contract renewal detail record.
Validates the id and updates FSRenewalDt with values from the project.
   OperationID: ChangeFSRenewalDtProjectID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFSRenewalDtProjectID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFSRenewalDtProjectID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeFSRenewalDtXPartNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeFSRenewalDtXPartNum
   Description: Method to call when changing the customer part number (XPartNum) on the
contract renewal detail record.
Updates FSRenewalDt with values from the customer part.
   OperationID: ChangeFSRenewalDtXPartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFSRenewalDtXPartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFSRenewalDtXPartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeFSRenewalDuration(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeFSRenewalDuration
   Description: Method to call when changing the duration on the contract renewal header record.
Updates FSRenewal with values based on the new duration.
   OperationID: ChangeFSRenewalDuration
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFSRenewalDuration_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFSRenewalDuration_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeFSRenewalFiscalCalendarID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeFSRenewalFiscalCalendarID
   Description: Method to call when changing the Fiscal Calendar on the contract renewal header record.
   OperationID: ChangeFSRenewalFiscalCalendarID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFSRenewalFiscalCalendarID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFSRenewalFiscalCalendarID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeFSRenewalModifier(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeFSRenewalModifier
   Description: Method to call when changing the Modifier on the contract renewal header record.
Updates FSRenewal with values based on the new Modifier.
   OperationID: ChangeFSRenewalModifier
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFSRenewalModifier_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFSRenewalModifier_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeFSRenewalPricePer(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeFSRenewalPricePer
   Description: Method to call when changing the PricePer on the contract renewal header record.
Updates FSRenewal with values based on the new PricePer.
   OperationID: ChangeFSRenewalPricePer
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFSRenewalPricePer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFSRenewalPricePer_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeFSRenewalQuotedRenewal(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeFSRenewalQuotedRenewal
   Description: Method to call when changing the Quoted Renewal flag on the contract renewal header record.
   OperationID: ChangeFSRenewalQuotedRenewal
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFSRenewalQuotedRenewal_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFSRenewalQuotedRenewal_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeFSRenewalRACode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeFSRenewalRACode
   Description: Method to call when changing the RACode on the contract renewal header record.
   OperationID: ChangeFSRenewalRACode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFSRenewalRACode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFSRenewalRACode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeFSRenewalRecurringFreq(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeFSRenewalRecurringFreq
   Description: Method to call when changing the RecurringFreq on the contract renewal header record.
Updates FSRenewal with values based on the new RecurringFreq.
   OperationID: ChangeFSRenewalRecurringFreq
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFSRenewalRecurringFreq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFSRenewalRecurringFreq_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeFSRenewalRenewEffDate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeFSRenewalRenewEffDate
   Description: Method to call when changing the renewal effective date on the contract renewal header record.
Updates FSRenewal with values based on the new effective date.
   OperationID: ChangeFSRenewalRenewEffDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFSRenewalRenewEffDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFSRenewalRenewEffDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeFSRenewalTaskSetID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeFSRenewalTaskSetID
   Description: Method to call when changing the Task Set ID on the contract renewal header record.
   OperationID: ChangeFSRenewalTaskSetID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFSRenewalTaskSetID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFSRenewalTaskSetID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeFSRenewalTaxCatID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeFSRenewalTaxCatID
   Description: Method to call when changing the tax category id on the contract renewal header record.
Validates the id and updates FSRenewal with values from the tax category.
   OperationID: ChangeFSRenewalTaxCatID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFSRenewalTaxCatID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFSRenewalTaxCatID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeFSRenewalRecurringInv(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeFSRenewalRecurringInv
   Description: Method to call when changing the recurring invoice flag on the contract renewal header record.
   OperationID: ChangeFSRenewalRecurringInv
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFSRenewalRecurringInv_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFSRenewalRecurringInv_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckPartNumChange(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckPartNumChange
   Description: The method is to be run on leave of the PartNum field before the
ChangeFSContDtPartNum or Update methods are run.
This returns all the questions that need to be asked before a part can be changed.
   OperationID: CheckPartNumChange
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckPartNumChange_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckPartNumChange_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckSerialNumbers(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckSerialNumbers
   Description: This method returns text of a message to be asked if the number of serial numbers
selected does not match the quantity entered for the FSContDt record.
The user has the option of continuing with the mismatch quantities or canceling.
This method should be called before the update method and should be called only when
part is serial number tracked and the quantity is greater than zero.
If the user answers yes, the change can occur; otherwise the change shouldn't occur.
   OperationID: CheckSerialNumbers
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckSerialNumbers_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckSerialNumbers_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CreateContractRMA(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CreateContractRMA
   Description: Call this method to create RMA for a given service contract.
   OperationID: CreateContractRMA
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateContractRMA_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateContractRMA_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ExpireContract(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ExpireContract
   Description: Call this method to expire a service contract.  Allow the user to confirm the
intention to expire the contract before calling this method.  Warn the user
that expiring the contract cannot be undone.
   OperationID: ExpireContract
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExpireContract_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExpireContract_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_FrequencyList(epicorHeaders = None):
   """  
   Summary: Invoke method FrequencyList
   Description: Method to call to get the list for the Frequency options.  The list is
returned in code1`code desc1~code2`code desc2 format.
   OperationID: FrequencyList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/FrequencyList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GenerateRenewal(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GenerateRenewal
   Description: Call this method to generate Contract Renewal (FSRenewal and FsRenewalDt)
from a given Contract or Renewal.
   OperationID: GenerateRenewal
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GenerateRenewal_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateRenewal_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GenerateRenewalLines(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GenerateRenewalLines
   Description: Call this method to generate Contract Renewal Lines (FsRenewalDt)
for a given Contract Renewal Header.
   OperationID: GenerateRenewalLines
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GenerateRenewalLines_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateRenewalLines_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetListCustom(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetListCustom
   Description: Custom GetList method. Retrieves records based on a delimited list
of Contract Numbers.
   OperationID: GetListCustom
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListCustom_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListCustom_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewFSContHdFromOrder(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewFSContHdFromOrder
   Description: Method to call when adding a contract from an order.
   OperationID: GetNewFSContHdFromOrder
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewFSContHdFromOrder_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewFSContHdFromOrder_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRowsContactTracker(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsContactTracker
   Description: Calls the normal GetRows method and then constructs a custom data set combining Hd/Dt fields for the contact tracker.
   OperationID: GetRowsContactTracker
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsContactTracker_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsContactTracker_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRowsCustom(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsCustom
   Description: Custom GetList method. Retrieves records based on a delimited list
of Contract Numbers.
   OperationID: GetRowsCustom
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsCustom_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsCustom_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRowsCustomerTracker(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsCustomerTracker
   Description: Calls the normal GetRows method and then constructs a custom data set combining Hd/Dt fields for the customer tracker.
   OperationID: GetRowsCustomerTracker
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsCustomerTracker_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsCustomerTracker_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRowsCustomerTrackerActive(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsCustomerTrackerActive
   Description: Returns active/not voided contracts for the customer
   OperationID: GetRowsCustomerTrackerActive
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsCustomerTrackerActive_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsCustomerTrackerActive_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRowsCustomerTrackerExpired(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsCustomerTrackerExpired
   Description: Returns expired/not voided contracts for the customer
   OperationID: GetRowsCustomerTrackerExpired
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsCustomerTrackerExpired_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsCustomerTrackerExpired_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetSelectedSerialNumbers(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetSelectedSerialNumbers
   Description: This method will retrieve the serial numbers for a service contract line and
update the SelectedSerialNumbers table with these records.
   OperationID: GetSelectedSerialNumbers
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSelectedSerialNumbers_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSelectedSerialNumbers_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetSelectSerialNumbersParams(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetSelectSerialNumbersParams
   Description: Gets parameters required for launching Select Serial Numbers
   OperationID: GetSelectSerialNumbersParams
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSelectSerialNumbersParams_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSelectSerialNumbersParams_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRenewalSelectedSerialNumbers(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRenewalSelectedSerialNumbers
   Description: This method will retrieve the serial numbers for a service contract Renewal line and
update the SelectedSerialNumbers table with these records.
   OperationID: GetRenewalSelectedSerialNumbers
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRenewalSelectedSerialNumbers_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRenewalSelectedSerialNumbers_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRenewalSelectSerialNumbersParams(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRenewalSelectSerialNumbersParams
   Description: Gets parameters required for launching Select Serial Numbers
   OperationID: GetRenewalSelectSerialNumbersParams
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRenewalSelectSerialNumbersParams_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRenewalSelectSerialNumbersParams_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CountContractsOnQuote(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CountContractsOnQuote
   Description: Verifies if the Contract/Renewal has any Quote. Then check if the Quote is related with other Contracts/Renewals.
   OperationID: CountContractsOnQuote
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CountContractsOnQuote_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CountContractsOnQuote_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_IsPlantSerialTracking(epicorHeaders = None):
   """  
   Summary: Invoke method IsPlantSerialTracking
   Description: Verifies if the current login plant is set for Serial Tracking
   OperationID: IsPlantSerialTracking
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/IsPlantSerialTracking_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_PricePerList(epicorHeaders = None):
   """  
   Summary: Invoke method PricePerList
   Description: Method to call to get the list for the Price Per options.  The list is
returned in code1`code desc1~code2`code desc2 format.
   OperationID: PricePerList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/PricePerList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_SuspendContract(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SuspendContract
   Description: Call this method after the user answered yes to the warning message returned by
SuspendContract method.  This logic updates all related InvcDtlRASch
records for this service contract. Based on the input contract status, the related
invoice revenue schedules will be put on hold/unhold.
   OperationID: SuspendContract
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SuspendContract_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SuspendContract_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateSN(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateSN
   Description: Validates that a single serial number is valid for this transaction
   OperationID: ValidateSN
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateSN_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateSN_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_VoidContract(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method VoidContract
   Description: Method to call when voiding the contract.
   OperationID: VoidContract
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/VoidContract_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/VoidContract_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DisableContractLines(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DisableContractLines
   OperationID: DisableContractLines
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DisableContractLines_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DisableContractLines_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_isContractExpired(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method isContractExpired
   Description: Validates contract Expired date against the current time zone Date for the current company.
   OperationID: isContractExpired
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/isContractExpired_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/isContractExpired_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateOTSTaxID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateOTSTaxID
   Description: One Time Ship To Tax Id validation
   OperationID: ValidateOTSTaxID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateOTSTaxID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateOTSTaxID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewFSContHd(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewFSContHd
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewFSContHd
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewFSContHd_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewFSContHd_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewFSContDt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewFSContDt
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewFSContDt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewFSContDt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewFSContDt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewFSContSN(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewFSContSN
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewFSContSN
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewFSContSN_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewFSContSN_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewFSRenewal(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewFSRenewal
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewFSRenewal
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewFSRenewal_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewFSRenewal_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewFSRenewalDt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewFSRenewalDt
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewFSRenewalDt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewFSRenewalDt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewFSRenewalDt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewFSRenewalSN(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewFSRenewalSN
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewFSRenewalSN
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewFSRenewalSN_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewFSRenewalSN_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewFSContLabExpRate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewFSContLabExpRate
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewFSContLabExpRate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewFSContLabExpRate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewFSContLabExpRate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FSContDtRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_FSContDtRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FSContHdListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_FSContHdListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FSContHdRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_FSContHdRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FSContLabExpRateRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_FSContLabExpRateRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FSContOrderDtlListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_FSContOrderDtlListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FSContSNRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_FSContSNRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FSRenewalDtRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_FSRenewalDtRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FSRenewalRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_FSRenewalRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FSRenewalSNRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_FSRenewalSNRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SNFormatRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_SNFormatRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SelectedSerialNumbersRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_SelectedSerialNumbersRow] = obj["value"]
      pass

class Erp_Tablesets_FSContDtRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier  """  
      self.ContractNum:int = obj["ContractNum"]
      """  Contract Number of the Contract  """  
      self.ContractLine:int = obj["ContractLine"]
      """  This field along with Company and ContractNum make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the FSContDtl record for the Contract and the adding 1 to it.  The user can override this number if they wish.  """  
      self.ContractCode:str = obj["ContractCode"]
      """  A unique code that identifies the Contract  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Optional field that contains the customers revision. Default from the Part.RevisionNum field.  """  
      self.LineDesc:str = obj["LineDesc"]
      """  Line Item description. The Part.Description can be used as a default.  """  
      self.IUM:str = obj["IUM"]
      """  Unit Of Measure (how it is sold/issued). Use the default Part.IUM if its a valid Part.  """  
      self.PricePerUnit:int = obj["PricePerUnit"]
      """  Price per unit for the Contract in base currency.  Defaults from the FScontCd table  """  
      self.DocPricePerUnit:int = obj["DocPricePerUnit"]
      """  Price per unit for the Contract in customers currency.  Defaults from the FScontCd table  """  
      self.ContractQty:int = obj["ContractQty"]
      """  Total Contract Quantity for the line item.  """  
      self.ProdCode:str = obj["ProdCode"]
      """  Product Group Code. Use the Part.ProdCode as a default.  This can be blank or must be valid in the ProdGrup table.  """  
      self.XPartNum:str = obj["XPartNum"]
      """  An optional field that is used if the customer has a different  Part number  than the users internal part number.  The XPartNum and PartNum can provide defaults for each other via the PartXref table.. The XPartNum can be blank, does not have to exist in the PartXref table.  """  
      self.XRevisionNum:str = obj["XRevisionNum"]
      """  Optional field that contains the customers revision. Default from the CustXPrt.RevisionNum field.  """  
      self.InvoiceComment:str = obj["InvoiceComment"]
      """  Used to establish invoice comments about the Contract line item. These will copied into the Invoice detail  file as defaults.  """  
      self.CustNum:int = obj["CustNum"]
      """  Customer number that the sales order is for. Duplicated from OrderHed.CustNum.  Used to allow efficient browsing of the FSContDt records for a specific customer.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Contains the Order Number that ties this detail record back to an OrderHed record.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  This field along with Company and OrderNum make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the OrderDtl record for the Order and the adding 1 to it.  The user can override this number if they wish.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  Project ID of the Project table record that this FSContDt record. Can be blank.  """  
      self.CommentText:str = obj["CommentText"]
      """  Editor widget for Contract comments.  """  
      self.ContractType:str = obj["ContractType"]
      """   A value of "ORD-ENT" indicates that this Service contract is related to a specific Sales Order and its line items and will be created and maintained from there, It will print on the Order acknowledgment and be invoiced with the sales order item as they are shipped.  A Value of "Cnt-Ent" indicates that this Service Contract was created from the service contract entry programs.  It is not directly related to a sales order; it will be printed by itself and invoiced by itself.
(Duplicated from FSContHd for Browse)  """  
      self.ContractComment:str = obj["ContractComment"]
      """  Contains comments about the detail contract line item. These will be printed on the Sales Acknowledgements and service contracts  """  
      self.SoldOrderNum:int = obj["SoldOrderNum"]
      """  Sold to Order Number  """  
      self.SoldOrderLine:int = obj["SoldOrderLine"]
      """  Sold To Order line  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.Rpt1PricePerUnit:int = obj["Rpt1PricePerUnit"]
      """  Reporting currency value of this field  """  
      self.Rpt2PricePerUnit:int = obj["Rpt2PricePerUnit"]
      """  Reporting currency value of this field  """  
      self.Rpt3PricePerUnit:int = obj["Rpt3PricePerUnit"]
      """  Reporting currency value of this field  """  
      self.Inactive:bool = obj["Inactive"]
      """  A value of Yes indicates the line is not part of the service contract agreement and it will not be included in the contract amounts.  """  
      self.DateInactivated:str = obj["DateInactivated"]
      """  This is the date the contract line was set to inactive.  """  
      self.BillStartDate:str = obj["BillStartDate"]
      """  This is the first date the contract line is considered for billing purposes.  """  
      self.BillEndDate:str = obj["BillEndDate"]
      """  This is the last date the contract line is considered for billing.  """  
      self.Invoiced:bool = obj["Invoiced"]
      """  Indicates this line has been invoiced.  """  
      self.DateInvoiced:str = obj["DateInvoiced"]
      """  Date this line was invoiced.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AllowUpdate:bool = obj["AllowUpdate"]
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      self.ExtPrice:int = obj["ExtPrice"]
      self.DocExtPrice:int = obj["DocExtPrice"]
      self.DisplayContractType:str = obj["DisplayContractType"]
      self.ReturnQty:int = obj["ReturnQty"]
      """  Return Quantity used in the create RMA process.  """  
      self.SelectedforRMA:bool = obj["SelectedforRMA"]
      """  Indicates if the contract line is selected to create RMA for.  """  
      self.HdCurrencyCode:str = obj["HdCurrencyCode"]
      self.HdCurrencyCodeDesc:str = obj["HdCurrencyCodeDesc"]
      self.DocCurrSymbol:str = obj["DocCurrSymbol"]
      """  Document currency symbol.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code of the related record  """  
      self.IUMDesc:str = obj["IUMDesc"]
      """  Unit of Measure Description  """  
      self.TrackSerialNumbers:bool = obj["TrackSerialNumbers"]
      self.Rpt1ExtPrice:int = obj["Rpt1ExtPrice"]
      self.Rpt2ExtPrice:int = obj["Rpt2ExtPrice"]
      self.Rpt3ExtPrice:int = obj["Rpt3ExtPrice"]
      self.PriceMulti:int = obj["PriceMulti"]
      """  The calculated PriceMulti is based on the parent FSContHd record.  """  
      self.IntExternalKey:str = obj["IntExternalKey"]
      """  Unique identifier of related integration record.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.ContractCodeContractDescription:str = obj["ContractCodeContractDescription"]
      self.CustNumBTName:str = obj["CustNumBTName"]
      self.CustNumCustID:str = obj["CustNumCustID"]
      self.CustNumName:str = obj["CustNumName"]
      self.OrderLineLineDesc:str = obj["OrderLineLineDesc"]
      self.OrderNumCurrencyCode:str = obj["OrderNumCurrencyCode"]
      self.OrderNumCardMemberName:str = obj["OrderNumCardMemberName"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.ProdCodeDescription:str = obj["ProdCodeDescription"]
      self.ProjectIDDescription:str = obj["ProjectIDDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_FSContHdListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ContractNum:int = obj["ContractNum"]
      """  When creating a new Service Contract the user is prompted for an Contract number. If the field is left blank, the next available Number is assigned by the system. The system generates a number by finding the order # of the last record on file and then a 1 to it.  """  
      self.ContractType:str = obj["ContractType"]
      """  A value of "Ord-Ent" indicates that this Service contract is related to a specific Sales Order and its line items and will be created and maintained from there, It will print on the Order acknowledgment and be invoiced with the sales order item as they are shipped.  A Value of "Cnt-Ent" indicates that this Service Contract was created from the service contract entry programs.  It is not directly related to a sales order; it will be printed by itself and invoiced by itself.  """  
      self.CustNum:int = obj["CustNum"]
      """  Contains the Customer number that the Service Contract is for.  This must be valid in the Customer table.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  The Sales order that this contract is linked to.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  The line number of the sales order that this contract is linked to  """  
      self.EntryDate:str = obj["EntryDate"]
      """  Same as OrderDate when SLSORD.  TODAY when CNTENT  """  
      self.ContractCode:str = obj["ContractCode"]
      """  A unique code that identifies the Contract  """  
      self.ContractComment:str = obj["ContractComment"]
      """  Contains comments about the overall Contract. These will be printed on the Service Contract.  """  
      self.InvoiceComment:str = obj["InvoiceComment"]
      """  Used to establish invoice comments about the overall Contract. These will copied into the Invoice detail file as defaults.  """  
      self.PrcConNum:int = obj["PrcConNum"]
      """  Contains the key  value for the Purchasing Contact. This can be blank or it must be valid in the CUSTCNT  table. Use the CUSTOMER.PRIMPCON as the default.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  Indicates which customer ship to is to be used  for the Service Contract. It  can be blank or it must be valid in the SHIPTO table. Use the CUSTOMER.SHIPTONUM as the default on new orders or when the ORDERHED.CUSTNUM is changed.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """   Exchange rate that will be used for this Contract.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  """  
      self.LockRate:bool = obj["LockRate"]
      """  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  This will also be the default for the invoice.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """   This is used as one of the selection parameters on the Service Contract entry edit reports. The intent is for users to be able to select Contract that they have entered for hard copy edit.
On new orders use the users login ID as the default. They can override this if they wish to enter something more meaningful.  """  
      self.ContVoid:bool = obj["ContVoid"]
      """  This Service Contract has been deactivated when TRUE  """  
      self.ShpConNum:int = obj["ShpConNum"]
      """  Establishes the Shipping Contact to be used.  In this case the contact at the location where the item the service contract is covering are. Contains the key value for the shipping contact in the CUSTCNT table. Can be blank or must be valid in the CUSTCNT table. Use the Customer.PrimScon as a default.  """  
      self.ActiveDate:str = obj["ActiveDate"]
      """   The date of the earliest FscontSp.activateDate for this contract.
Not user maintainable.  It is written when the fscontsp record is created or changed. This will always be the earliest activate date on this contract.  """  
      self.ExpireDate:str = obj["ExpireDate"]
      """   The date of the Latest FscontSp.ExpirationDate for this contract.
Not user maintainable.  It is written when the fscontsp record is created or changed.  this will always be the Latest activate date on this contract.  """  
      self.Duration:int = obj["Duration"]
      """  Duration of Contract  """  
      self.Modifier:str = obj["Modifier"]
      """  Whether the duration is for Days, Months, years.  """  
      self.Material:bool = obj["Material"]
      """  Coverage  for material  """  
      self.Labor:bool = obj["Labor"]
      """  Coverage for Labor  """  
      self.Misc:bool = obj["Misc"]
      """  Coverage for Misc charges. This includes the miscellaneous expenses like travel, etc.  """  
      self.Invoiced:bool = obj["Invoiced"]
      """  The invoice for this Service contract  has been created. The Order line that this contract is linked to has shipped.  """  
      self.PackNum:int = obj["PackNum"]
      """  Packing slip number that this detail record is linked with.  """  
      self.PackLine:int = obj["PackLine"]
      """  An integer that Ties the Contract record to a packing slip detail line  """  
      self.OnSite:bool = obj["OnSite"]
      """  This contract covers on site visits  """  
      self.RecurringInv:bool = obj["RecurringInv"]
      """  Indicates that Service Contract with this Code will generate recurring invoices.  """  
      self.RecurringFreq:str = obj["RecurringFreq"]
      """  The frequency that recurring invoices are generated only 'monthly' for now.  """  
      self.PricePer:str = obj["PricePer"]
      """  Price modifier for unit price field Daily, monthly, Contract(Full length of the contract)  """  
      self.LastInvGen:bool = obj["LastInvGen"]
      """  This flag is set to TRUE after the last recurring invoice is generated for the contract.  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  The invoice number of the last recurring invoice.  """  
      self.TaxCatID:str = obj["TaxCatID"]
      """  Indicates the Tax Category for this record.  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.BTCustNum:int = obj["BTCustNum"]
      """  Bill To Customer Number  """  
      self.UseOTS:bool = obj["UseOTS"]
      """   Indicates if the One Time ShipTo information should be used instead of the standard ShipTo.  One Time ShipTo info is stored in this record in the fields prefixed with "OTS"
Note: This can only be true when if the OTSName is not blank. 
UI disables this when Customer.AllowQTS = False,  """  
      self.OTSName:str = obj["OTSName"]
      """  One Time Shipto Name of the ShipTo.  """  
      self.OTSAddress1:str = obj["OTSAddress1"]
      """  One Time Shipto first line of the ShipTo address.  """  
      self.OTSAddress2:str = obj["OTSAddress2"]
      """  One Time Shipto  second line of the ShipTo address.  """  
      self.OTSAddress3:str = obj["OTSAddress3"]
      """  One Time Shipto  third line of the ShipTo address.  """  
      self.OTSCity:str = obj["OTSCity"]
      """  City portion of the One Time Shipto  address.  """  
      self.OTSState:str = obj["OTSState"]
      """  The state or province portion of the One Time Shipto  address.  """  
      self.OTSZIP:str = obj["OTSZIP"]
      """  The zip or postal code portion of the One Time ShipTo  address.  """  
      self.OTSResaleID:str = obj["OTSResaleID"]
      """  The State Tax Identification Number of the One Time Shipto.  """  
      self.OTSTaxRegionCode:str = obj["OTSTaxRegionCode"]
      """  Contains the TaxRgn.TaxRegionCode value of the One Time ShipTo tax region for purposes of Sales Tax calculations.  """  
      self.OTSContact:str = obj["OTSContact"]
      """  Full name of the contact.  """  
      self.OTSFaxNum:str = obj["OTSFaxNum"]
      """  Fax number for the One Time ShipTo.  """  
      self.OTSPhoneNum:str = obj["OTSPhoneNum"]
      """  Phone number for the One Time ShipTo  """  
      self.OTSCountryNum:int = obj["OTSCountryNum"]
      """  One Time Shipping country Number.  """  
      self.ShipToCustNum:int = obj["ShipToCustNum"]
      """  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  """  
      self.DeferredRev:bool = obj["DeferredRev"]
      """  Indicates if revenue is deferred for contracts assigned to this group.  """  
      self.RACode:str = obj["RACode"]
      """  Revenue Amortization Code.  """  
      self.DefRevStart:str = obj["DefRevStart"]
      """  Starting date the revenue is deferred.  """  
      self.Suspended:bool = obj["Suspended"]
      """  Indicates if the contract has been suspended.  A suspended contract cannot have any calls linked to it.  """  
      self.QuotedContract:bool = obj["QuotedContract"]
      """  Indicates if the contrct will automatically generate a quote  """  
      self.ShipContract:bool = obj["ShipContract"]
      """  Defaulted from the service contract code.  Determines whether or not the contract can be invoiced directly or if it must be shipped.  When yes the contract must be added to a sales order and then shipped prior to invoicing.  """  
      self.TaskSetID:str = obj["TaskSetID"]
      """  Unique identifier of the task set assigned by the user.  """  
      self.ReadyToInvoice:bool = obj["ReadyToInvoice"]
      """  Indicates if the contract is ready to be invoiced.   This is only available when ShipContract = no.  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Quote number to which this line item detail record is associated with. This is part of the foreign key to OrderHed file.  """  
      self.QuoteLine:int = obj["QuoteLine"]
      """  This field along with Company and QuoteNum make up the unique key to the table. The system generates this number during entry of new detail records. The system determines next available number by finding the QuoteDtl record for the Quote and the adding 1 to it.  """  
      self.QuoteAccepted:bool = obj["QuoteAccepted"]
      """  Indicates the Quote has been accepted  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.OTSCountry:str = obj["OTSCountry"]
      self.ContractStartup:bool = obj["ContractStartup"]
      self.SoldToPhoneNum:str = obj["SoldToPhoneNum"]
      self.SoldToFaxNum:str = obj["SoldToFaxNum"]
      self.SoldToContactName:str = obj["SoldToContactName"]
      self.ShipToPhoneNum:str = obj["ShipToPhoneNum"]
      self.ShipToFaxNum:str = obj["ShipToFaxNum"]
      self.ShipToContactName:str = obj["ShipToContactName"]
      self.ContractExpired:bool = obj["ContractExpired"]
      self.ContractTotal:int = obj["ContractTotal"]
      self.DocContractTotal:int = obj["DocContractTotal"]
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      self.EnableBillTo:bool = obj["EnableBillTo"]
      self.EnableShipTo:bool = obj["EnableShipTo"]
      self.EnableCurrency:bool = obj["EnableCurrency"]
      self.AllowUpdate:bool = obj["AllowUpdate"]
      self.DisplayContractType:str = obj["DisplayContractType"]
      self.ShipToAddressList:str = obj["ShipToAddressList"]
      self.SoldToAddressList:str = obj["SoldToAddressList"]
      self.PartOrderDtlList:str = obj["PartOrderDtlList"]
      self.opMessage:str = obj["opMessage"]
      self.Rpt1ContractTotal:int = obj["Rpt1ContractTotal"]
      self.Rpt2ContractTotal:int = obj["Rpt2ContractTotal"]
      self.Rpt3ContractTotal:int = obj["Rpt3ContractTotal"]
      self.CustAllowOTS:bool = obj["CustAllowOTS"]
      """  Customer.AllowOTS value. Allow One Time Shipto.  """  
      self.BTCustName:str = obj["BTCustName"]
      """  Name of the Bill To Customer  """  
      self.AvailBTCustList:str = obj["AvailBTCustList"]
      """  Delimited list of available bill to customers.  """  
      self.BaseCurrencyID:str = obj["BaseCurrencyID"]
      self.RenewedUntil:str = obj["RenewedUntil"]
      """  The expire date of the last effective renewed contract  """  
      self.RenewalTotal:int = obj["RenewalTotal"]
      self.DocRenewalTotal:int = obj["DocRenewalTotal"]
      self.Rpt1RenewalTotal:int = obj["Rpt1RenewalTotal"]
      self.Rpt2RenewalTotal:int = obj["Rpt2RenewalTotal"]
      self.Rpt3RenewalTotal:int = obj["Rpt3RenewalTotal"]
      self.ContractRenewed:bool = obj["ContractRenewed"]
      self.EnableRenewal:bool = obj["EnableRenewal"]
      """  Flag to indicate if the service contract can be renewed.  """  
      self.ContractCodeContractDescription:str = obj["ContractCodeContractDescription"]
      """  Description of the service contract.  """  
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      """  Description of the currency  """  
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      """  A symbol that identifies the currency. Used on Forms and displays  """  
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      """  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  """  
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      """   An extended description that can be used on documents such as
POs and invoices.  """  
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      """   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  """  
      self.CustNumBTName:str = obj["CustNumBTName"]
      """  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  """  
      self.CustNumCustID:str = obj["CustNumCustID"]
      """  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  """  
      self.CustNumName:str = obj["CustNumName"]
      """  The full name of the customer.  """  
      self.CustNumAllowShipTo3:bool = obj["CustNumAllowShipTo3"]
      """  When yes, a ShipTo CustID on certain forms will be enabled. This allows a shipto of a different customer to be referenced as a 3rd party for a document.  """  
      self.InvoiceNumCardMemberName:str = obj["InvoiceNumCardMemberName"]
      """  The member's name on the credit card.  """  
      self.InvoiceNumTermsCode:str = obj["InvoiceNumTermsCode"]
      """  Contains the foreign key to the TERMS master file.  Defaults from OrderHed if OrderNum > 0 else from the Customer master. This IS A MANDATORY ENTRY. User maintainable via a combo-box for terms description.  """  
      self.OrderLineLineDesc:str = obj["OrderLineLineDesc"]
      """  Line Item description. The Part.Description can be used as a default.  """  
      self.OrderNumCurrencyCode:str = obj["OrderNumCurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.OrderNumCardMemberName:str = obj["OrderNumCardMemberName"]
      """  The member's name on the credit card.  """  
      self.OTSTaxRegionCodeDescription:str = obj["OTSTaxRegionCodeDescription"]
      """  Full description for the Tax Region.  """  
      self.PackLineLineDesc:str = obj["PackLineLineDesc"]
      """  Line description.  """  
      self.PackNumName:str = obj["PackNumName"]
      """  Name of the ShipTo. When creating new records the Customer.Name is used as a default.  This can't be blank.  """  
      self.RACodeRADesc:str = obj["RACodeRADesc"]
      """  Free form text describing the revenue amortization code.  """  
      self.ShipToBTName:str = obj["ShipToBTName"]
      """  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  """  
      self.ShipToCustID:str = obj["ShipToCustID"]
      """  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  """  
      self.ShipToName:str = obj["ShipToName"]
      """  The full name of the customer.  """  
      self.TaxCatIDDescription:str = obj["TaxCatIDDescription"]
      """  Full description for the Sales Tax category.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_FSContHdRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ContractNum:int = obj["ContractNum"]
      """  When creating a new Service Contract the user is prompted for an Contract number. If the field is left blank, the next available Number is assigned by the system. The system generates a number by finding the order # of the last record on file and then a 1 to it.  """  
      self.ContractType:str = obj["ContractType"]
      """  A value of "Ord-Ent" indicates that this Service contract is related to a specific Sales Order and its line items and will be created and maintained from there, It will print on the Order acknowledgment and be invoiced with the sales order item as they are shipped.  A Value of "Cnt-Ent" indicates that this Service Contract was created from the service contract entry programs.  It is not directly related to a sales order; it will be printed by itself and invoiced by itself.  """  
      self.CustNum:int = obj["CustNum"]
      """  Contains the Customer number that the Service Contract is for.  This must be valid in the Customer table.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  The Sales order that this contract is linked to.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  The line number of the sales order that this contract is linked to  """  
      self.EntryDate:str = obj["EntryDate"]
      """  Same as OrderDate when SLSORD.  TODAY when CNTENT  """  
      self.ContractCode:str = obj["ContractCode"]
      """  A unique code that identifies the Contract  """  
      self.ContractComment:str = obj["ContractComment"]
      """  Contains comments about the overall Contract. These will be printed on the Service Contract.  """  
      self.InvoiceComment:str = obj["InvoiceComment"]
      """  Used to establish invoice comments about the overall Contract. These will copied into the Invoice detail file as defaults.  """  
      self.PrcConNum:int = obj["PrcConNum"]
      """  Contains the key  value for the Purchasing Contact. This can be blank or it must be valid in the CUSTCNT  table. Use the CUSTOMER.PRIMPCON as the default.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  Indicates which customer ship to is to be used  for the Service Contract. It  can be blank or it must be valid in the SHIPTO table. Use the CUSTOMER.SHIPTONUM as the default on new orders or when the ORDERHED.CUSTNUM is changed.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """   Exchange rate that will be used for this Contract.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  """  
      self.LockRate:bool = obj["LockRate"]
      """  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  This will also be the default for the invoice.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """   This is used as one of the selection parameters on the Service Contract entry edit reports. The intent is for users to be able to select Contract that they have entered for hard copy edit.
On new orders use the users login ID as the default. They can override this if they wish to enter something more meaningful.  """  
      self.ContVoid:bool = obj["ContVoid"]
      """  This Service Contract has been deactivated when TRUE  """  
      self.ShpConNum:int = obj["ShpConNum"]
      """  Establishes the Shipping Contact to be used.  In this case the contact at the location where the item the service contract is covering are. Contains the key value for the shipping contact in the CUSTCNT table. Can be blank or must be valid in the CUSTCNT table. Use the Customer.PrimScon as a default.  """  
      self.ActiveDate:str = obj["ActiveDate"]
      """   The date of the earliest FscontSp.activateDate for this contract.
Not user maintainable.  It is written when the fscontsp record is created or changed. This will always be the earliest activate date on this contract.  """  
      self.ExpireDate:str = obj["ExpireDate"]
      """   The date of the Latest FscontSp.ExpirationDate for this contract.
Not user maintainable.  It is written when the fscontsp record is created or changed.  this will always be the Latest activate date on this contract.  """  
      self.Duration:int = obj["Duration"]
      """  Duration of Contract  """  
      self.Modifier:str = obj["Modifier"]
      """  Whether the duration is for Days, Months, years.  """  
      self.Material:bool = obj["Material"]
      """  Coverage  for material  """  
      self.Labor:bool = obj["Labor"]
      """  Coverage for Labor  """  
      self.Misc:bool = obj["Misc"]
      """  Coverage for Misc charges. This includes the miscellaneous expenses like travel, etc.  """  
      self.Invoiced:bool = obj["Invoiced"]
      """  The invoice for this Service contract  has been created. The Order line that this contract is linked to has shipped.  """  
      self.PackNum:int = obj["PackNum"]
      """  Packing slip number that this detail record is linked with.  """  
      self.PackLine:int = obj["PackLine"]
      """  An integer that Ties the Contract record to a packing slip detail line  """  
      self.OnSite:bool = obj["OnSite"]
      """  This contract covers on site visits  """  
      self.RecurringInv:bool = obj["RecurringInv"]
      """  Indicates that Service Contract with this Code will generate recurring invoices.  """  
      self.RecurringFreq:str = obj["RecurringFreq"]
      """  The frequency that recurring invoices are generated only 'monthly' for now.  """  
      self.PricePer:str = obj["PricePer"]
      """  Price modifier for unit price field Daily, monthly, Contract(Full length of the contract)  """  
      self.LastInvGen:bool = obj["LastInvGen"]
      """  This flag is set to TRUE after the last recurring invoice is generated for the contract.  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  The invoice number of the last recurring invoice.  """  
      self.TaxCatID:str = obj["TaxCatID"]
      """  Indicates the Tax Category for this record.  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.BTCustNum:int = obj["BTCustNum"]
      """  Bill To Customer Number  """  
      self.UseOTS:bool = obj["UseOTS"]
      """   Indicates if the One Time ShipTo information should be used instead of the standard ShipTo.  One Time ShipTo info is stored in this record in the fields prefixed with "OTS"
Note: This can only be true when if the OTSName is not blank. 
UI disables this when Customer.AllowQTS = False,  """  
      self.OTSName:str = obj["OTSName"]
      """  One Time Shipto Name of the ShipTo.  """  
      self.OTSAddress1:str = obj["OTSAddress1"]
      """  One Time Shipto first line of the ShipTo address.  """  
      self.OTSAddress2:str = obj["OTSAddress2"]
      """  One Time Shipto  second line of the ShipTo address.  """  
      self.OTSAddress3:str = obj["OTSAddress3"]
      """  One Time Shipto  third line of the ShipTo address.  """  
      self.OTSCity:str = obj["OTSCity"]
      """  City portion of the One Time Shipto  address.  """  
      self.OTSState:str = obj["OTSState"]
      """  The state or province portion of the One Time Shipto  address.  """  
      self.OTSZIP:str = obj["OTSZIP"]
      """  The zip or postal code portion of the One Time ShipTo  address.  """  
      self.OTSResaleID:str = obj["OTSResaleID"]
      """  The State Tax Identification Number of the One Time Shipto.  """  
      self.OTSTaxRegionCode:str = obj["OTSTaxRegionCode"]
      """  Contains the TaxRgn.TaxRegionCode value of the One Time ShipTo tax region for purposes of Sales Tax calculations.  """  
      self.OTSContact:str = obj["OTSContact"]
      """  Full name of the contact.  """  
      self.OTSFaxNum:str = obj["OTSFaxNum"]
      """  Fax number for the One Time ShipTo.  """  
      self.OTSPhoneNum:str = obj["OTSPhoneNum"]
      """  Phone number for the One Time ShipTo  """  
      self.OTSCountryNum:int = obj["OTSCountryNum"]
      """  One Time Shipping country Number.  """  
      self.ShipToCustNum:int = obj["ShipToCustNum"]
      """  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  """  
      self.DeferredRev:bool = obj["DeferredRev"]
      """  Indicates if revenue is deferred for contracts assigned to this group.  """  
      self.RACode:str = obj["RACode"]
      """  Revenue Amortization Code.  """  
      self.DefRevStart:str = obj["DefRevStart"]
      """  Starting date the revenue is deferred.  """  
      self.Suspended:bool = obj["Suspended"]
      """  Indicates if the contract has been suspended.  A suspended contract cannot have any calls linked to it.  """  
      self.QuotedContract:bool = obj["QuotedContract"]
      """  Indicates if the contrct will automatically generate a quote  """  
      self.ShipContract:bool = obj["ShipContract"]
      """  Defaulted from the service contract code.  Determines whether or not the contract can be invoiced directly or if it must be shipped.  When yes the contract must be added to a sales order and then shipped prior to invoicing.  """  
      self.TaskSetID:str = obj["TaskSetID"]
      """  Unique identifier of the task set assigned by the user.  """  
      self.ReadyToInvoice:bool = obj["ReadyToInvoice"]
      """  Indicates if the contract is ready to be invoiced.   This is only available when ShipContract = no.  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Quote number to which this line item detail record is associated with. This is part of the foreign key to OrderHed file.  """  
      self.QuoteLine:int = obj["QuoteLine"]
      """  This field along with Company and QuoteNum make up the unique key to the table. The system generates this number during entry of new detail records. The system determines next available number by finding the QuoteDtl record for the Quote and the adding 1 to it.  """  
      self.QuoteAccepted:bool = obj["QuoteAccepted"]
      """  Indicates the Quote has been accepted  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.InvcTiming:str = obj["InvcTiming"]
      """  InvcTiming  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  Indicates how often an invoice is generated for the contract.  """  
      self.Renewable:bool = obj["Renewable"]
      """  Indicates if the service contract using is valid for renewal.  """  
      self.IncIntrastat:bool = obj["IncIntrastat"]
      """  Intrastat: Activates HS Commodity code retrieving in contract invoicing  """  
      self.SendToFSA:bool = obj["SendToFSA"]
      """  Determines if the service contract has to be synchronized with Epicor FSA application.  """  
      self.OTSTaxValidationStatus:int = obj["OTSTaxValidationStatus"]
      """  OTSTaxValidationStatus  """  
      self.OTSTaxValidationDate:str = obj["OTSTaxValidationDate"]
      """  OTSTaxValidationDate  """  
      self.AllowUpdate:bool = obj["AllowUpdate"]
      self.AvailBTCustList:str = obj["AvailBTCustList"]
      """  Delimited list of available bill to customers.  """  
      self.BaseCurrencyID:str = obj["BaseCurrencyID"]
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      self.BTCustName:str = obj["BTCustName"]
      """  Name of the Bill To Customer  """  
      self.ContractExpired:bool = obj["ContractExpired"]
      self.ContractRenewed:bool = obj["ContractRenewed"]
      self.ContractStartup:bool = obj["ContractStartup"]
      self.ContractTotal:int = obj["ContractTotal"]
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.CustAllowOTS:bool = obj["CustAllowOTS"]
      """  Customer.AllowOTS value. Allow One Time Shipto.  """  
      self.DisplayContractType:str = obj["DisplayContractType"]
      self.DocContractTotal:int = obj["DocContractTotal"]
      self.DocRenewalTotal:int = obj["DocRenewalTotal"]
      self.EnableBillTo:bool = obj["EnableBillTo"]
      self.EnableCurrency:bool = obj["EnableCurrency"]
      self.EnableQuote:bool = obj["EnableQuote"]
      self.EnableRenewable:bool = obj["EnableRenewable"]
      """  Flag to indicate when to enable the Renewable check box.  The flag is set to no if the current contract has been renewed already (FSRenewal exists).  """  
      self.EnableRenewal:bool = obj["EnableRenewal"]
      """  Flag to indicate if the service contract can be renewed.  (This flag should not be confused with EnableRenewable.)  This EnableRenewal is used to check if the current original contract (FSContHd) or the latest contract renewal (FSRenewal) (whichever is currently actve) meets the expiration date check against the expire horizon and contract renewal period set at FSSyst table.  """  
      self.EnableShipTo:bool = obj["EnableShipTo"]
      self.FiscalCalDescription:str = obj["FiscalCalDescription"]
      self.opMessage:str = obj["opMessage"]
      self.OTSCountry:str = obj["OTSCountry"]
      self.PartOrderDtlList:str = obj["PartOrderDtlList"]
      self.ReadyToQuote:bool = obj["ReadyToQuote"]
      """  Flag to indicate if the Contract is ready to be quoted.  """  
      self.RenewalTotal:int = obj["RenewalTotal"]
      self.RenewedUntil:str = obj["RenewedUntil"]
      """  The expire date of the last effective renewed contract  """  
      self.Rpt1ContractTotal:int = obj["Rpt1ContractTotal"]
      self.Rpt1RenewalTotal:int = obj["Rpt1RenewalTotal"]
      self.Rpt2ContractTotal:int = obj["Rpt2ContractTotal"]
      self.Rpt2RenewalTotal:int = obj["Rpt2RenewalTotal"]
      self.Rpt3ContractTotal:int = obj["Rpt3ContractTotal"]
      self.Rpt3RenewalTotal:int = obj["Rpt3RenewalTotal"]
      self.ShipToAddressList:str = obj["ShipToAddressList"]
      self.ShipToContactName:str = obj["ShipToContactName"]
      self.ShipToFaxNum:str = obj["ShipToFaxNum"]
      self.ShipToPhoneNum:str = obj["ShipToPhoneNum"]
      self.SoldToAddressList:str = obj["SoldToAddressList"]
      self.SoldToContactName:str = obj["SoldToContactName"]
      self.SoldToFaxNum:str = obj["SoldToFaxNum"]
      self.SoldToPhoneNum:str = obj["SoldToPhoneNum"]
      self.UninvoicedLine:bool = obj["UninvoicedLine"]
      """  Flag to indicate if additional uninvoiced contract line has been added after the contract has been invoiced.  """  
      self.UpdateLineDates:bool = obj["UpdateLineDates"]
      self.FSAServiceAgreementNum:int = obj["FSAServiceAgreementNum"]
      """  Used to indicate which FSA Service Agreement a Contract Renewal is related to.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CompanySendToFSA:bool = obj["CompanySendToFSA"]
      self.ContractCodeContractDescription:str = obj["ContractCodeContractDescription"]
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      self.CustNumCustID:str = obj["CustNumCustID"]
      self.CustNumAllowShipTo3:bool = obj["CustNumAllowShipTo3"]
      self.CustNumName:str = obj["CustNumName"]
      self.CustNumBTName:str = obj["CustNumBTName"]
      self.CustNumSendToFSA:bool = obj["CustNumSendToFSA"]
      self.InvoiceNumCardMemberName:str = obj["InvoiceNumCardMemberName"]
      self.InvoiceNumTermsCode:str = obj["InvoiceNumTermsCode"]
      self.OrderLineLineDesc:str = obj["OrderLineLineDesc"]
      self.OrderNumCurrencyCode:str = obj["OrderNumCurrencyCode"]
      self.OrderNumCardMemberName:str = obj["OrderNumCardMemberName"]
      self.OTSCountryEUMember:bool = obj["OTSCountryEUMember"]
      self.OTSCountryISOCode:str = obj["OTSCountryISOCode"]
      self.OTSTaxRegionCodeDescription:str = obj["OTSTaxRegionCodeDescription"]
      self.PackLineLineDesc:str = obj["PackLineLineDesc"]
      self.PackNumName:str = obj["PackNumName"]
      self.RACodeRADesc:str = obj["RACodeRADesc"]
      self.ShipToBTName:str = obj["ShipToBTName"]
      self.ShipToName:str = obj["ShipToName"]
      self.ShipToCustID:str = obj["ShipToCustID"]
      self.ShipToNumInactive:bool = obj["ShipToNumInactive"]
      self.ShipToNumName:str = obj["ShipToNumName"]
      self.TaskSetWorkflowType:str = obj["TaskSetWorkflowType"]
      self.TaskSetTaskSetDescription:str = obj["TaskSetTaskSetDescription"]
      self.TaxCatIDDescription:str = obj["TaxCatIDDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_FSContLabExpRateRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ContractNum:int = obj["ContractNum"]
      """  ContractNum  """  
      self.ExpenseCode:str = obj["ExpenseCode"]
      """  ExpenseCode  """  
      self.RateType:int = obj["RateType"]
      """  RateType  """  
      self.RateMultiplier:int = obj["RateMultiplier"]
      """  RateMultiplier  """  
      self.FixedRate:int = obj["FixedRate"]
      """  FixedRate  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_FSContOrderDtlListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Contains the Order Number that ties this detail record back to an OrderHed record.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  This field along with Company and OrderNum make up the unique key to the OrderHed table.  """  
      self.PartNum:str = obj["PartNum"]
      """  The user's Internal Part number used to identify Order line item part.  """  
      self.LineDesc:str = obj["LineDesc"]
      """  Order Line Item description. The Part.Description can be used as a default.  """  
      self.LineStatus:str = obj["LineStatus"]
      """  Status of Order Line  """  
      self.Selected:bool = obj["Selected"]
      """  boolean flag to indicate user has selected this row  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for OrderDtl  row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_FSContSNRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier  """  
      self.ContractNum:int = obj["ContractNum"]
      """  Contract Number of the Contract  """  
      self.ContractLine:int = obj["ContractLine"]
      """  This field along with Company and ContractNum make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the FSContDtl record for the Contract and the adding 1 to it.  The user can override this number if they wish.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part. Not directly maintainable. Mirror image of FSContDt.PartNum. Having this field, allows a SerialNo record to find the contracts that it is related to.  """  
      self.SerialNumber:str = obj["SerialNumber"]
      """  Serial number of the Part that is assigned to this Field Service contract line.  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AutoAdd:bool = obj["AutoAdd"]
      """  True indicates that the FSContSN record was auto added by CustShip or DropShip processing  """  
      self.ExpireDate:str = obj["ExpireDate"]
      """  Expire Date of the contract, for display in Serial Number tracker  """  
      self.FSContCdDesc:str = obj["FSContCdDesc"]
      """  Description of the contract header contract type, for display in SerialNo tracker  """  
      self.IntExternalKey:str = obj["IntExternalKey"]
      """  Unique identifier of related integration record.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_FSRenewalDtRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ContractNum:int = obj["ContractNum"]
      """  When creating a new Service Contract the user is prompted for an Contract number. If the field is left blank, the next available Number is assigned by the system. The system generates a number by finding the order # of the last record on file and then a 1 to it.  """  
      self.RenewalNbr:int = obj["RenewalNbr"]
      """  Contract renewal number. If the value is zero then the contract is not for a renewal.  """  
      self.RenewalLine:int = obj["RenewalLine"]
      """  This field along with Company and ContractNum make up the unique key to the table.  """  
      self.ContractLine:int = obj["ContractLine"]
      """  This field along with Company and ContractNum make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the FSContDtl record for the Contract and the adding 1 to it.  The user can override this number if they wish.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Optional field that contains the customers revision. Default from the Part.RevisionNum field.  """  
      self.LineDesc:str = obj["LineDesc"]
      """  Line Item description. The Part.Description can be used as a default.  """  
      self.IUM:str = obj["IUM"]
      """  Unit Of Measure (how it is sold/issued). Use the default Part.IUM if its a valid Part.  """  
      self.IncreasePct:int = obj["IncreasePct"]
      """  The percentage increase of the renewal price.  """  
      self.PricePerUnit:int = obj["PricePerUnit"]
      """  Price per unit for the Contract in base currency.  Defaults from the FScontCd table  """  
      self.DocPricePerUnit:int = obj["DocPricePerUnit"]
      """  Price per unit for the Contract in customers currency.  Defaults from the FScontCd table  """  
      self.Rpt1PricePerUnit:int = obj["Rpt1PricePerUnit"]
      """  Reporting currency value of this field  """  
      self.Rpt2PricePerUnit:int = obj["Rpt2PricePerUnit"]
      """  Reporting currency value of this field  """  
      self.Rpt3PricePerUnit:int = obj["Rpt3PricePerUnit"]
      """  Reporting currency value of this field  """  
      self.ContractQty:int = obj["ContractQty"]
      """  Total Contract Quantity for the line item.  """  
      self.XPartNum:str = obj["XPartNum"]
      """  An optional field that is used if the customer has a different  Part number  than the users internal part number.  The XPartNum and PartNum can provide defaults for each other via the PartXref table.. The XPartNum can be blank, does not have to exist in the PartXref table.  """  
      self.XRevisionNum:str = obj["XRevisionNum"]
      """  Optional field that contains the customers revision. Default from the CustXPrt.RevisionNum field.  """  
      self.CustNum:int = obj["CustNum"]
      """  Customer number that the sales order is for. Duplicated from OrderHed.CustNum.  Used to allow efficient browsing of the FSContDt records for a specific customer.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Contains the Order Number that ties this detail record back to an OrderHed record.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  This field along with Company and OrderNum make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the OrderDtl record for the Order and the adding 1 to it.  The user can override this number if they wish.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  Project ID of the Project table record that this FSContDt record. Can be blank.  """  
      self.Inactive:bool = obj["Inactive"]
      """  A value of Yes indicates the line is not part of the service contract agreement and it will not be included in the contract amounts.  """  
      self.DateInactivated:str = obj["DateInactivated"]
      """  This is the date the contract line was set to inactive.  """  
      self.BillStartDate:str = obj["BillStartDate"]
      """  This is the first date the contract line is considered for billing purposes.  """  
      self.BillEndDate:str = obj["BillEndDate"]
      """  This is the last date the contract line is considered for billing.  """  
      self.Invoiced:bool = obj["Invoiced"]
      """  Indicates this line has been invoiced.  """  
      self.DateInvoiced:str = obj["DateInvoiced"]
      """  Date this line was invoiced.  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RefRenewalNbr:int = obj["RefRenewalNbr"]
      """  The RefRenewalNbr stores the reference renewal number of the renewal record was copied.  """  
      self.ProdCode:str = obj["ProdCode"]
      """  It is a unique code used to identify a specific product group.  """  
      self.SoldOrderNum:int = obj["SoldOrderNum"]
      """  Sales Order Num related to this FSContDt record.  """  
      self.SoldOrderLine:int = obj["SoldOrderLine"]
      """  Sales Order Line related to this FSContDt record.  """  
      self.AllowUpdate:bool = obj["AllowUpdate"]
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.DocCurrSymbol:str = obj["DocCurrSymbol"]
      self.DocExtendedPrice:int = obj["DocExtendedPrice"]
      self.DocOrigPricePerUnit:int = obj["DocOrigPricePerUnit"]
      self.ExtendedPrice:int = obj["ExtendedPrice"]
      """  Extended Price of the Contract Renewal Line  """  
      self.IUMDesc:str = obj["IUMDesc"]
      self.OrigContractQty:int = obj["OrigContractQty"]
      """  Original Contract Qty of the Contract Line  """  
      self.OrigIUM:str = obj["OrigIUM"]
      """  Original IUM of the Contract Line  """  
      self.OrigIUMDesc:str = obj["OrigIUMDesc"]
      self.OrigPricePerUnit:int = obj["OrigPricePerUnit"]
      """  Original Price Per Unit of the Contract Line  """  
      self.PriceMulti:int = obj["PriceMulti"]
      """  The calculated PriceMulti is based on the parent FSRenewal record.  """  
      self.ProdCodeDescription:str = obj["ProdCodeDescription"]
      self.Rpt1ExtendedPrice:int = obj["Rpt1ExtendedPrice"]
      self.Rpt1OrigPricePerUnit:int = obj["Rpt1OrigPricePerUnit"]
      self.Rpt2ExtendedPrice:int = obj["Rpt2ExtendedPrice"]
      self.Rpt2OrigPricePerUnit:int = obj["Rpt2OrigPricePerUnit"]
      self.Rpt3ExtendedPrice:int = obj["Rpt3ExtendedPrice"]
      self.Rpt3OrigPricePerUnit:int = obj["Rpt3OrigPricePerUnit"]
      self.TrackSerialNumbers:bool = obj["TrackSerialNumbers"]
      self.IntExternalKey:str = obj["IntExternalKey"]
      """  Unique identifier of related integration record.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CustNumCustID:str = obj["CustNumCustID"]
      self.CustNumName:str = obj["CustNumName"]
      self.CustNumBTName:str = obj["CustNumBTName"]
      self.OrderLineLineDesc:str = obj["OrderLineLineDesc"]
      self.OrderNumCardMemberName:str = obj["OrderNumCardMemberName"]
      self.OrderNumCurrencyCode:str = obj["OrderNumCurrencyCode"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.ProjectIDDescription:str = obj["ProjectIDDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_FSRenewalRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ContractNum:int = obj["ContractNum"]
      """  When creating a new Service Contract the user is prompted for an Contract number. If the field is left blank, the next available Number is assigned by the system. The system generates a number by finding the order # of the last record on file and then a 1 to it.  """  
      self.RenewalNbr:int = obj["RenewalNbr"]
      """  Contract renewal number. If the value is zero then the contract is not for a renewal.  """  
      self.QuotedRenewal:bool = obj["QuotedRenewal"]
      """  Indicates if the renwal will automatically generate a quote.  """  
      self.TaskSetID:str = obj["TaskSetID"]
      """  Unique identifier of the task set assigned by the user.  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Quote number to which this line item detail record is associated with. This is part of the foreign key to OrderHed file.  """  
      self.QuoteLine:int = obj["QuoteLine"]
      """  This field along with Company and QuoteNum make up the unique key to the table. The system generates this number during entry of new detail records. The system determines next available number by finding the QuoteDtl record for the Quote and the adding 1 to it.  """  
      self.QuoteAccepted:bool = obj["QuoteAccepted"]
      """  Indicates the Quote has been accepted.  """  
      self.RenewalCode:str = obj["RenewalCode"]
      """  This is the contract code assigned to the renewal.  """  
      self.ShipRenewal:bool = obj["ShipRenewal"]
      """  Defaulted from the service contract code.  Determines whether or not the renewal can be invoiced directly or if it must be shipped.  When yes the contract must be added to a sales order and then shipped prior to invoicing.  """  
      self.RACode:str = obj["RACode"]
      """  Revenue Amortization Code.  """  
      self.DeferredRev:bool = obj["DeferredRev"]
      """  Indicates if revenue is deferred for contracts assigned to this group.  """  
      self.DefRevStart:str = obj["DefRevStart"]
      """  Starting date the revenue is deferred.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """   Exchange rate that will be used for this Contract.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  """  
      self.LockRate:bool = obj["LockRate"]
      """  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  This will also be the default for the invoice.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """   This is used as one of the selection parameters on the Service Contract entry edit reports. The intent is for users to be able to select Contract that they have entered for hard copy edit.
On new orders use the users login ID as the default. They can override this if they wish to enter something more meaningful.  """  
      self.EntryDate:str = obj["EntryDate"]
      """  Date the renewal was created.  """  
      self.Material:bool = obj["Material"]
      """  Coverage  for material  """  
      self.Labor:bool = obj["Labor"]
      """  Coverage for Labor  """  
      self.Misc:bool = obj["Misc"]
      """  Coverage for Misc charges. This includes the miscellaneous expenses like travel, etc.  """  
      self.OnSite:bool = obj["OnSite"]
      """  This contract covers on site visits  """  
      self.Invoiced:bool = obj["Invoiced"]
      """  The invoice for this Service contract  has been created. The Order line that this contract is linked to has shipped.  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  The invoice number of the last recurring invoice.  """  
      self.PackNum:int = obj["PackNum"]
      """  Packing slip number that this detail record is linked with.  """  
      self.PackLine:int = obj["PackLine"]
      """  An integer that Ties the Contract record to a packing slip detail line  """  
      self.RecurringInv:bool = obj["RecurringInv"]
      """  Indicates that Service Contract with this Code will generate recurring invoices.  """  
      self.RecurringFreq:str = obj["RecurringFreq"]
      """  The frequency that recurring invoices are generated only 'monthly' for now.  """  
      self.PricePer:str = obj["PricePer"]
      """  Price modifier for unit price field Daily, monthly, Contract(Full length of the contract)  """  
      self.LastInvGen:bool = obj["LastInvGen"]
      """  This flag is set to TRUE after the last recurring invoice is generated for the contract.  """  
      self.TaxCatID:str = obj["TaxCatID"]
      """  Indicates the Tax Category for this record.  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.ReadyToInvoice:bool = obj["ReadyToInvoice"]
      """  Indicates if the contract is ready to be invoiced.   This is only available when ShipContract = no.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  The Sales order that this contract is linked to.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  The line number of the sales order that this contract is linked to  """  
      self.Duration:int = obj["Duration"]
      """  Duration of Contract  """  
      self.RenewalComment:str = obj["RenewalComment"]
      """  Used to establish invoice comments about the overall Renewal.  """  
      self.RenewEffDate:str = obj["RenewEffDate"]
      """  Date when the renewal begins.  """  
      self.RenewedUntil:str = obj["RenewedUntil"]
      """  Date the renewal ends.  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.InvcTiming:str = obj["InvcTiming"]
      """  InvcTiming  """  
      self.ContractCode:str = obj["ContractCode"]
      """  It is the same as the contract type but applied to renewals  """  
      self.Modifier:str = obj["Modifier"]
      """  The unit of measure of time that the renewal contract lasts.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  Indicates how often an invoice is generated for the contract  """  
      self.Renewable:bool = obj["Renewable"]
      """  Indicates if the service contract is valid for renewal  """  
      self.RenewalTotal:int = obj["RenewalTotal"]
      """  Total Renewal Amount  """  
      self.DocRenewalTotal:int = obj["DocRenewalTotal"]
      self.Rpt1RenewalTotal:int = obj["Rpt1RenewalTotal"]
      self.Rpt2RenewalTotal:int = obj["Rpt2RenewalTotal"]
      self.Rpt3RenewalTotal:int = obj["Rpt3RenewalTotal"]
      self.RenewalExpired:bool = obj["RenewalExpired"]
      """  Indicates if the Contract Renewal has expired.  """  
      self.RenewalRenewed:bool = obj["RenewalRenewed"]
      """  Indicates if the Contract Renewal has been renewed.  """  
      self.RenewalVoid:bool = obj["RenewalVoid"]
      """  Indicates if the related Contract Header has been voided.  """  
      self.AllowUpdate:bool = obj["AllowUpdate"]
      self.UninvoicedLine:bool = obj["UninvoicedLine"]
      """  Flag to indicate if additional uninvoiced renewal line has been added after the renewal header has been invoiced.  """  
      self.FiscalCalDescription:str = obj["FiscalCalDescription"]
      self.ReadyToQuote:bool = obj["ReadyToQuote"]
      """  Flag to indicate if the Contract Renewal is ready to be quoted.  """  
      self.EnableQuote:bool = obj["EnableQuote"]
      self.EnableRenewable:bool = obj["EnableRenewable"]
      """  Flag to indicate when to enable the Renewable check box.  The flag is set to no if the current contract renewal has been renewed already (another FSRenewal exists).  """  
      self.UpdateLineDates:bool = obj["UpdateLineDates"]
      self.ContractCodeDescription:str = obj["ContractCodeDescription"]
      self.BitFlag:int = obj["BitFlag"]
      self.CodeContractDescription:str = obj["CodeContractDescription"]
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      self.RACodeRADesc:str = obj["RACodeRADesc"]
      self.TaskSetWorkflowType:str = obj["TaskSetWorkflowType"]
      self.TaskSetTaskSetDescription:str = obj["TaskSetTaskSetDescription"]
      self.TaxCatIDDescription:str = obj["TaxCatIDDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_FSRenewalSNRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier  """  
      self.ContractNum:int = obj["ContractNum"]
      """  Contract Number of the Contract  """  
      self.RenewalNbr:int = obj["RenewalNbr"]
      """  Contract renewal number. If the value is zero then the contract is not for a renewal.  """  
      self.RenewalLine:int = obj["RenewalLine"]
      """  This field along with Company and ContractNum make up the unique key to the table.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part. Not directly maintainable. Mirror image of FSContDt.PartNum. Having this field, allows a SerialNo record to find the contracts that it is related to.  """  
      self.SerialNumber:str = obj["SerialNumber"]
      """  Serial number of the Part that is assigned to this Field Service contract line.  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.FSContCdDesc:str = obj["FSContCdDesc"]
      """  Description of the contract header contract type, for display in SerialNo tracker  """  
      self.IntExternalKey:str = obj["IntExternalKey"]
      """  Unique identifier of related integration record.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SNFormatRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier. This field cannot be blank.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part and is used in the primary key.  """  
      self.NumberOfDigits:int = obj["NumberOfDigits"]
      """  Number of digits in the serial number  """  
      self.SNMask:str = obj["SNMask"]
      """  If the SNBaseDataType is Mask this is the Serial Mask ID assigned for format validation/generation.  """  
      self.SNBaseDataType:str = obj["SNBaseDataType"]
      """   Current setting for Data type of the Base Serial Number field to be used as new serial numbers are generated. Valid values; Character, Integer, Mask
Code/desc required:
CHARACTER`Alphanumeric
INTEGER`NumericOnly
MASK`Serial Mask
This field should be flagged as Include = true in Object Designer.  """  
      self.SNFormat1:str = obj["SNFormat1"]
      self.LeadingZeroes:bool = obj["LeadingZeroes"]
      """  Whether or not to have leading zeroes  """  
      self.SNPrefix:str = obj["SNPrefix"]
      """   Current setting for the prefix that will be attached to all new Serial Numbers as they are generated for Character and Integer format types.
This field should be flagged as Include = true in Object Designer.  """  
      self.SNMaskSuffix:str = obj["SNMaskSuffix"]
      """  A standard suffix that will be attached to all serial numbers generated for the PartSite currently used only by SNBaseStructure Mask types  """  
      self.SNMaskPrefix:str = obj["SNMaskPrefix"]
      """  The prefix that was used to construct the serial number currently used only by SNBaseStructure Mask types  """  
      self.SNLastUsedSeq:str = obj["SNLastUsedSeq"]
      """  This is the last used serial sequence. It is used only for the Mask Generate type to determine the next logical serial number to generate for this part/Site. It can be altered by the user and several PartSites can have the same counter values defined, but  """  
      self.HasSerialNumbers:bool = obj["HasSerialNumbers"]
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.PartPricePerCode:str = obj["PartPricePerCode"]
      self.PartTrackLots:bool = obj["PartTrackLots"]
      self.PartTrackSerialNum:bool = obj["PartTrackSerialNum"]
      self.PartTrackDimension:bool = obj["PartTrackDimension"]
      self.PartSalesUM:str = obj["PartSalesUM"]
      self.PartIUM:str = obj["PartIUM"]
      self.PartSellingFactor:int = obj["PartSellingFactor"]
      self.PartPartDescription:str = obj["PartPartDescription"]
      self.SerialMaskMaskType:int = obj["SerialMaskMaskType"]
      self.SerialMaskMask:str = obj["SerialMaskMask"]
      self.SerialMaskExample:str = obj["SerialMaskExample"]
      self.SerialMaskDescription:str = obj["SerialMaskDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SelectedSerialNumbersRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.SerialNumber:str = obj["SerialNumber"]
      """  SerialNumber  """  
      self.Scrapped:bool = obj["Scrapped"]
      """  Scrapped flag  """  
      self.ScrappedReasonCode:str = obj["ScrappedReasonCode"]
      """  Scrapped reason code  """  
      self.Voided:bool = obj["Voided"]
      """  Voided flag  """  
      self.Reference:str = obj["Reference"]
      """  Reference field  """  
      self.ReasonCodeType:str = obj["ReasonCodeType"]
      """  Reason code type = s  """  
      self.ReasonCodeDesc:str = obj["ReasonCodeDesc"]
      """  Reason code description  """  
      self.PartNum:str = obj["PartNum"]
      """  PartNumber  """  
      self.SNPrefix:str = obj["SNPrefix"]
      """  Serial number prefix  """  
      self.SNBaseNumber:str = obj["SNBaseNumber"]
      """  Base number used to create the serial number  """  
      self.SourceRowID:str = obj["SourceRowID"]
      """  RowID of the source record for this serial number  """  
      self.TransType:str = obj["TransType"]
      """  TransType of the record that created this serial number  """  
      self.PassedInspection:bool = obj["PassedInspection"]
      """  True if this serial numbered part passed inspection  """  
      self.Deselected:bool = obj["Deselected"]
      """  Used to flag previously selected serial numbers as deselected  """  
      self.KitWhseList:str = obj["KitWhseList"]
      self.RawSerialNum:str = obj["RawSerialNum"]
      """  This will be the raw serial number as it was scanned or entered into the system. This would only differ from the SerialNumber field if a validate type mask was being used where characters were stripped (using ~ in the mask).  """  
      self.KBLbrAction:int = obj["KBLbrAction"]
      """  Action type field used for Kanban receipts to indicate if the new serial number status is Inventory, Scrapped or NonConf.  This requires Code/desc:  1 ` inventory 2 ` Scrapped 3 ` Nonconformance  """  
      self.KBLbrActionDesc:str = obj["KBLbrActionDesc"]
      """  Description field for KBLbrAction ? holds the translated description for the KBLbrAction code for UI display and combo box.  """  
      self.PreventDeselect:bool = obj["PreventDeselect"]
      """  If true, then users can not deselect this serial number.  This is used by applications that allow maintenance to the Selected Serial Numbers after update.  """  
      self.XRefPartNum:str = obj["XRefPartNum"]
      """  Used only by SN Assignment  """  
      self.XRefPartType:str = obj["XRefPartType"]
      """  Used only by SN Assignment: C = Customer Part / I = Internal Part XRef  """  
      self.PreDeselected:bool = obj["PreDeselected"]
      self.poLinkValues:str = obj["poLinkValues"]
      """  temporary field used to link the packout lines to ship detail lines  """  
      self.SNMask:str = obj["SNMask"]
      """  The mask the was used to generate the serial number  """  
      self.NotSavedToDB:bool = obj["NotSavedToDB"]
      """  Flag to indicate that the SelectedSerialNumbers entry has not yet been saved to the DB for the related transaction. Used to keep track of which deselected serial numbers need to be passed to the transaction update logic.  """  
      self.RowSelected:bool = obj["RowSelected"]
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class ActivateContract_input:
   """ Required : 
   ActivateContractNum
   ds
   """  
   def __init__(self, obj):
      self.ActivateContractNum:int = obj["ActivateContractNum"]
      """  The contract number to activate  """  
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

class ActivateContract_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeFSContDtBillEndDate_input:
   """ Required : 
   ipBillEndDate
   ds
   """  
   def __init__(self, obj):
      self.ipBillEndDate:str = obj["ipBillEndDate"]
      """  The proposed bill end date  """  
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

class ChangeFSContDtBillEndDate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeFSContDtBillStartDate_input:
   """ Required : 
   ipBillStartDate
   ds
   """  
   def __init__(self, obj):
      self.ipBillStartDate:str = obj["ipBillStartDate"]
      """  The proposed bill start date  """  
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

class ChangeFSContDtBillStartDate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeFSContDtContractQty_input:
   """ Required : 
   ProposedContractQty
   ds
   """  
   def __init__(self, obj):
      self.ProposedContractQty:int = obj["ProposedContractQty"]
      """  The proposed contract quantity  """  
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

class ChangeFSContDtContractQty_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeFSContDtOrderLine_input:
   """ Required : 
   ProposedOrderLine
   ds
   """  
   def __init__(self, obj):
      self.ProposedOrderLine:int = obj["ProposedOrderLine"]
      """  The proposed order line number  """  
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

class ChangeFSContDtOrderLine_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeFSContDtOrderNum_input:
   """ Required : 
   ProposedOrderNum
   ds
   """  
   def __init__(self, obj):
      self.ProposedOrderNum:int = obj["ProposedOrderNum"]
      """  The proposed order number  """  
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

class ChangeFSContDtOrderNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeFSContDtPartNumWithSubs_input:
   """ Required : 
   ProposedPartNum
   substitutePartNum
   ds
   """  
   def __init__(self, obj):
      self.ProposedPartNum:str = obj["ProposedPartNum"]
      self.substitutePartNum:str = obj["substitutePartNum"]
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

class ChangeFSContDtPartNumWithSubs_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeFSContDtPartNum_input:
   """ Required : 
   ProposedPartNum
   ds
   """  
   def __init__(self, obj):
      self.ProposedPartNum:str = obj["ProposedPartNum"]
      """  The proposed part number  """  
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

class ChangeFSContDtPartNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeFSContDtPricePerUnit_input:
   """ Required : 
   ProposedPricePerUnit
   ds
   """  
   def __init__(self, obj):
      self.ProposedPricePerUnit:int = obj["ProposedPricePerUnit"]
      """  The proposed price per unit  """  
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

class ChangeFSContDtPricePerUnit_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeFSContDtProdCode_input:
   """ Required : 
   ProposedProdCode
   ds
   """  
   def __init__(self, obj):
      self.ProposedProdCode:str = obj["ProposedProdCode"]
      """  The proposed product code  """  
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

class ChangeFSContDtProdCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeFSContDtProjectID_input:
   """ Required : 
   ProposedProjectID
   ds
   """  
   def __init__(self, obj):
      self.ProposedProjectID:str = obj["ProposedProjectID"]
      """  The proposed project id  """  
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

class ChangeFSContDtProjectID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeFSContDtXPartNum_input:
   """ Required : 
   ProposedXPartNum
   ds
   """  
   def __init__(self, obj):
      self.ProposedXPartNum:str = obj["ProposedXPartNum"]
      """  The proposed xref part number  """  
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

class ChangeFSContDtXPartNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeFSContHDUseOTS_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

class ChangeFSContHDUseOTS_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeFSContHdActiveDate_input:
   """ Required : 
   ProposedActiveDate
   ds
   """  
   def __init__(self, obj):
      self.ProposedActiveDate:str = obj["ProposedActiveDate"]
      """  The proposed active date  """  
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

class ChangeFSContHdActiveDate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeFSContHdBTCusNum_input:
   """ Required : 
   ProposedCustNum
   ds
   """  
   def __init__(self, obj):
      self.ProposedCustNum:int = obj["ProposedCustNum"]
      """  The proposed Bill To customer Num  """  
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

class ChangeFSContHdBTCusNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeFSContHdContractCode_input:
   """ Required : 
   ProposedContractCode
   ds
   """  
   def __init__(self, obj):
      self.ProposedContractCode:str = obj["ProposedContractCode"]
      """  The proposed contract code  """  
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

class ChangeFSContHdContractCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeFSContHdCurrencyCode_input:
   """ Required : 
   ProposedCurrencyCode
   ds
   """  
   def __init__(self, obj):
      self.ProposedCurrencyCode:str = obj["ProposedCurrencyCode"]
      """  The proposed currency code  """  
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

class ChangeFSContHdCurrencyCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeFSContHdCustID_input:
   """ Required : 
   ProposedCustID
   ds
   """  
   def __init__(self, obj):
      self.ProposedCustID:str = obj["ProposedCustID"]
      """  The proposed customer id  """  
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

class ChangeFSContHdCustID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeFSContHdDeferredRev_input:
   """ Required : 
   ipDeferredRev
   ds
   """  
   def __init__(self, obj):
      self.ipDeferredRev:bool = obj["ipDeferredRev"]
      """  The proposed Deferred Revenue value  """  
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

class ChangeFSContHdDeferredRev_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeFSContHdDuration_input:
   """ Required : 
   ProposedDuration
   ds
   """  
   def __init__(self, obj):
      self.ProposedDuration:int = obj["ProposedDuration"]
      """  The proposed duration  """  
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

class ChangeFSContHdDuration_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeFSContHdFiscalCalendarID_input:
   """ Required : 
   ipFiscalCalendarID
   ds
   """  
   def __init__(self, obj):
      self.ipFiscalCalendarID:str = obj["ipFiscalCalendarID"]
      """  The proposed Fiscal Calendar ID value  """  
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

class ChangeFSContHdFiscalCalendarID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeFSContHdModifier_input:
   """ Required : 
   proposedModifier
   ds
   """  
   def __init__(self, obj):
      self.proposedModifier:str = obj["proposedModifier"]
      """  The proposed Modifier  """  
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

class ChangeFSContHdModifier_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeFSContHdPrcConNum_input:
   """ Required : 
   ProposedConNum
   ds
   """  
   def __init__(self, obj):
      self.ProposedConNum:int = obj["ProposedConNum"]
      """  The proposed contact number  """  
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

class ChangeFSContHdPrcConNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeFSContHdPricePer_input:
   """ Required : 
   ipPricePer
   ds
   """  
   def __init__(self, obj):
      self.ipPricePer:str = obj["ipPricePer"]
      """  The proposed PricePer  """  
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

class ChangeFSContHdPricePer_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeFSContHdQuotedContract_input:
   """ Required : 
   ipQuotedContract
   ds
   """  
   def __init__(self, obj):
      self.ipQuotedContract:bool = obj["ipQuotedContract"]
      """  The proposed Quoted Contract value  """  
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

class ChangeFSContHdQuotedContract_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeFSContHdRACode_input:
   """ Required : 
   ipRACode
   ds
   """  
   def __init__(self, obj):
      self.ipRACode:str = obj["ipRACode"]
      """  The proposed Revenue Amortization Code value  """  
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

class ChangeFSContHdRACode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeFSContHdRecurringFreq_input:
   """ Required : 
   ipRecurringFreq
   ds
   """  
   def __init__(self, obj):
      self.ipRecurringFreq:str = obj["ipRecurringFreq"]
      """  The proposed RecurringFreq  """  
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

class ChangeFSContHdRecurringFreq_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeFSContHdRecurringInv_input:
   """ Required : 
   ipRecurringInv
   ds
   """  
   def __init__(self, obj):
      self.ipRecurringInv:bool = obj["ipRecurringInv"]
      """  The proposed recurring invoice value  """  
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

class ChangeFSContHdRecurringInv_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeFSContHdShipToCustID_input:
   """ Required : 
   ipShipToCustID
   ds
   """  
   def __init__(self, obj):
      self.ipShipToCustID:str = obj["ipShipToCustID"]
      """  The proposed ShipTo Customer ID  """  
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

class ChangeFSContHdShipToCustID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeFSContHdShipToNum_input:
   """ Required : 
   ProposedShipToNum
   ds
   """  
   def __init__(self, obj):
      self.ProposedShipToNum:str = obj["ProposedShipToNum"]
      """  The proposed ship to number  """  
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

class ChangeFSContHdShipToNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeFSContHdShpConNum_input:
   """ Required : 
   ProposedShpConNum
   ds
   """  
   def __init__(self, obj):
      self.ProposedShpConNum:int = obj["ProposedShpConNum"]
      """  The proposed ship to number  """  
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

class ChangeFSContHdShpConNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeFSContHdSuspended_input:
   """ Required : 
   ipSuspended
   ds
   """  
   def __init__(self, obj):
      self.ipSuspended:bool = obj["ipSuspended"]
      """  The proposed Suspended value  """  
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

class ChangeFSContHdSuspended_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opMessage:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeFSContHdTaskSetID_input:
   """ Required : 
   ipTaskSetID
   ds
   """  
   def __init__(self, obj):
      self.ipTaskSetID:str = obj["ipTaskSetID"]
      """  The proposed Task Set ID value  """  
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

class ChangeFSContHdTaskSetID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeFSContHdTaxCatID_input:
   """ Required : 
   ProposedTaxCatID
   ds
   """  
   def __init__(self, obj):
      self.ProposedTaxCatID:str = obj["ProposedTaxCatID"]
      """  The proposed tax category id  """  
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

class ChangeFSContHdTaxCatID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeFSRenewalContractCode_input:
   """ Required : 
   ipContractCode
   ds
   """  
   def __init__(self, obj):
      self.ipContractCode:str = obj["ipContractCode"]
      """  The proposed contract code  """  
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

class ChangeFSRenewalContractCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeFSRenewalDeferredRev_input:
   """ Required : 
   ipDeferredRev
   ds
   """  
   def __init__(self, obj):
      self.ipDeferredRev:bool = obj["ipDeferredRev"]
      """  The proposed Deferred Revenue value  """  
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

class ChangeFSRenewalDeferredRev_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeFSRenewalDtBillEndDate_input:
   """ Required : 
   ipBillEndDate
   ds
   """  
   def __init__(self, obj):
      self.ipBillEndDate:str = obj["ipBillEndDate"]
      """  The proposed bill end date  """  
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

class ChangeFSRenewalDtBillEndDate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeFSRenewalDtBillStartDate_input:
   """ Required : 
   ipBillStartDate
   ds
   """  
   def __init__(self, obj):
      self.ipBillStartDate:str = obj["ipBillStartDate"]
      """  The proposed bill start date  """  
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

class ChangeFSRenewalDtBillStartDate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeFSRenewalDtContractQty_input:
   """ Required : 
   ipContractQty
   ds
   """  
   def __init__(self, obj):
      self.ipContractQty:int = obj["ipContractQty"]
      """  The proposed contract quantity  """  
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

class ChangeFSRenewalDtContractQty_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeFSRenewalDtIncreasePct_input:
   """ Required : 
   ipIncreasePct
   ds
   """  
   def __init__(self, obj):
      self.ipIncreasePct:int = obj["ipIncreasePct"]
      """  The proposed increase percent  """  
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

class ChangeFSRenewalDtIncreasePct_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeFSRenewalDtOrderLine_input:
   """ Required : 
   ipOrderLine
   ds
   """  
   def __init__(self, obj):
      self.ipOrderLine:int = obj["ipOrderLine"]
      """  The proposed order line number  """  
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

class ChangeFSRenewalDtOrderLine_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeFSRenewalDtOrderNum_input:
   """ Required : 
   ipOrderNum
   ds
   """  
   def __init__(self, obj):
      self.ipOrderNum:int = obj["ipOrderNum"]
      """  The proposed order number  """  
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

class ChangeFSRenewalDtOrderNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeFSRenewalDtPartNumWithSubs_input:
   """ Required : 
   ProposedPartNum
   substitutePartNum
   ds
   """  
   def __init__(self, obj):
      self.ProposedPartNum:str = obj["ProposedPartNum"]
      """  The proposed part number  """  
      self.substitutePartNum:str = obj["substitutePartNum"]
      """  The substitute part if any  """  
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

class ChangeFSRenewalDtPartNumWithSubs_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeFSRenewalDtPartNum_input:
   """ Required : 
   ipPartNum
   ds
   """  
   def __init__(self, obj):
      self.ipPartNum:str = obj["ipPartNum"]
      """  The proposed part number  """  
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

class ChangeFSRenewalDtPartNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeFSRenewalDtPricePerUnit_input:
   """ Required : 
   ipPricePerUnit
   ipBaseOrDoc
   ds
   """  
   def __init__(self, obj):
      self.ipPricePerUnit:int = obj["ipPricePerUnit"]
      """  The proposed price per unit  """  
      self.ipBaseOrDoc:str = obj["ipBaseOrDoc"]
      """  Indicates if calculating for Base ('B') or Doc ('D')  """  
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

class ChangeFSRenewalDtPricePerUnit_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeFSRenewalDtProdCode_input:
   """ Required : 
   ipProdCode
   ds
   """  
   def __init__(self, obj):
      self.ipProdCode:str = obj["ipProdCode"]
      """  The proposed product code  """  
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

class ChangeFSRenewalDtProdCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeFSRenewalDtProjectID_input:
   """ Required : 
   ipProjectID
   ds
   """  
   def __init__(self, obj):
      self.ipProjectID:str = obj["ipProjectID"]
      """  The proposed project id  """  
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

class ChangeFSRenewalDtProjectID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeFSRenewalDtXPartNum_input:
   """ Required : 
   ipXPartNum
   ds
   """  
   def __init__(self, obj):
      self.ipXPartNum:str = obj["ipXPartNum"]
      """  The proposed xref part number  """  
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

class ChangeFSRenewalDtXPartNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeFSRenewalDuration_input:
   """ Required : 
   ipDuration
   ds
   """  
   def __init__(self, obj):
      self.ipDuration:int = obj["ipDuration"]
      """  The proposed duration  """  
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

class ChangeFSRenewalDuration_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeFSRenewalFiscalCalendarID_input:
   """ Required : 
   ipFiscalCalendarID
   ds
   """  
   def __init__(self, obj):
      self.ipFiscalCalendarID:str = obj["ipFiscalCalendarID"]
      """  The proposed Fiscal Calendar ID value  """  
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

class ChangeFSRenewalFiscalCalendarID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeFSRenewalModifier_input:
   """ Required : 
   ipModifier
   ds
   """  
   def __init__(self, obj):
      self.ipModifier:str = obj["ipModifier"]
      """  The proposed Modifier  """  
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

class ChangeFSRenewalModifier_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeFSRenewalPricePer_input:
   """ Required : 
   ipPricePer
   ds
   """  
   def __init__(self, obj):
      self.ipPricePer:str = obj["ipPricePer"]
      """  The proposed PricePer  """  
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

class ChangeFSRenewalPricePer_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeFSRenewalQuotedRenewal_input:
   """ Required : 
   ipQuotedRenewal
   ds
   """  
   def __init__(self, obj):
      self.ipQuotedRenewal:bool = obj["ipQuotedRenewal"]
      """  The proposed Quoted Renewal value  """  
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

class ChangeFSRenewalQuotedRenewal_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeFSRenewalRACode_input:
   """ Required : 
   ipRACode
   ds
   """  
   def __init__(self, obj):
      self.ipRACode:str = obj["ipRACode"]
      """  The proposed Revenue Amortization Code value  """  
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

class ChangeFSRenewalRACode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeFSRenewalRecurringFreq_input:
   """ Required : 
   ipRecurringFreq
   ds
   """  
   def __init__(self, obj):
      self.ipRecurringFreq:str = obj["ipRecurringFreq"]
      """  The proposed RecurringFreq  """  
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

class ChangeFSRenewalRecurringFreq_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeFSRenewalRecurringInv_input:
   """ Required : 
   ipRecurringInv
   ds
   """  
   def __init__(self, obj):
      self.ipRecurringInv:bool = obj["ipRecurringInv"]
      """  The proposed recurring invoice value  """  
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

class ChangeFSRenewalRecurringInv_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeFSRenewalRenewEffDate_input:
   """ Required : 
   ipRenewEffDate
   ds
   """  
   def __init__(self, obj):
      self.ipRenewEffDate:str = obj["ipRenewEffDate"]
      """  The proposed renewal effective date  """  
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

class ChangeFSRenewalRenewEffDate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeFSRenewalTaskSetID_input:
   """ Required : 
   ipTaskSetID
   ds
   """  
   def __init__(self, obj):
      self.ipTaskSetID:str = obj["ipTaskSetID"]
      """  The proposed Task Set ID value  """  
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

class ChangeFSRenewalTaskSetID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeFSRenewalTaxCatID_input:
   """ Required : 
   ipTaxCatID
   ds
   """  
   def __init__(self, obj):
      self.ipTaxCatID:str = obj["ipTaxCatID"]
      """  The proposed tax category id  """  
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

class ChangeFSRenewalTaxCatID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckPartNumChange_input:
   """ Required : 
   cPartNum
   """  
   def __init__(self, obj):
      self.cPartNum:str = obj["cPartNum"]
      """  The new PartNum if a substitute part is found, partNum will be the substitute part
            No means the part cannot be changed  """  
      pass

class CheckPartNumChange_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.cPartNum:str = obj["parameters"]
      self.cSubPartMessage:str = obj["parameters"]
      self.lSubAvail:bool = obj["lSubAvail"]
      self.cMsgType:str = obj["parameters"]
      pass

      """  output parameters  """  

class CheckSerialNumbers_input:
   """ Required : 
   ds
   contractQty
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      self.contractQty:int = obj["contractQty"]
      """  Quantity of Serial Numbers required for the Contract Line  """  
      pass

class CheckSerialNumbers_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      self.cMessageText:str = obj["parameters"]
      pass

      """  output parameters  """  

class CountContractsOnQuote_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

class CountContractsOnQuote_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CreateContractRMA_input:
   """ Required : 
   ipContractNum
   ipReasonCode
   ds
   """  
   def __init__(self, obj):
      self.ipContractNum:int = obj["ipContractNum"]
      """  The contract number to create the RMA for.  """  
      self.ipReasonCode:str = obj["ipReasonCode"]
      """  The Reason Code for the RMA.  """  
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

class CreateContractRMA_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   contractNum
   """  
   def __init__(self, obj):
      self.contractNum:int = obj["contractNum"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class DisableContractLines_input:
   """ Required : 
   expiredDate
   """  
   def __init__(self, obj):
      self.expiredDate:str = obj["expiredDate"]
      pass

class DisableContractLines_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class Erp_Tablesets_FSContCustTrkRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  from FSContHd.Comany  """  
      self.CustNum:int = obj["CustNum"]
      """  from FSContHd.CustNum  """  
      self.ContractNum:int = obj["ContractNum"]
      """  from FSContHd.ContractNum  """  
      self.ShpConNum:int = obj["ShpConNum"]
      """  from FSContHd.ShpConNum  """  
      self.ContractCodeDescription:str = obj["ContractCodeDescription"]
      """  from FSContHd.ContractCodeDescription  """  
      self.Duration:int = obj["Duration"]
      """  from FSContHd.Duration and FSContHd.Modifier  """  
      self.OnSite:bool = obj["OnSite"]
      """  from FSContHd.OnSite  """  
      self.Material:bool = obj["Material"]
      """  from FSContHd.Material  """  
      self.Labor:bool = obj["Labor"]
      """  from FSContHd.Labor  """  
      self.Misc:bool = obj["Misc"]
      """  from FSContHd.Misc  """  
      self.ActiveDate:str = obj["ActiveDate"]
      """  from FSContHd.ActiveDate  """  
      self.ExpireDate:str = obj["ExpireDate"]
      """  from FSContHd.ExpireDate  """  
      self.Invoiced:bool = obj["Invoiced"]
      """  from FSContHd.Invoiced  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  from FSContCd.InvoiceNum  """  
      self.ContractCode:str = obj["ContractCode"]
      """  from FSContHd.ContractCode  """  
      self.PackLine:int = obj["PackLine"]
      """  from FSContHd.PackLine  """  
      self.PackNum:int = obj["PackNum"]
      """  from FSContHd.PackNum  """  
      self.ContractLine:int = obj["ContractLine"]
      """  from FSContDt.ContractLine  """  
      self.PartNum:str = obj["PartNum"]
      """  from FSContDt.PartNum  """  
      self.LineDesc:str = obj["LineDesc"]
      """  from FSContDt.LineDesc  """  
      self.ContractQty:int = obj["ContractQty"]
      """  from FSContDt.ContractQty  """  
      self.OrderNum:int = obj["OrderNum"]
      """  from FSContDt.OrderNum  """  
      self.OrderLine:int = obj["OrderLine"]
      """  from FSContDt.OrderLine  """  
      self.ContractExpired:bool = obj["ContractExpired"]
      """  from FSContHd.ContractExpired  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  from FSContDt.RevisionNum  """  
      self.XPartNum:str = obj["XPartNum"]
      """  from FSContDt.XPartNum  """  
      self.XRevisionNum:str = obj["XRevisionNum"]
      """  from FSContDt.XRevisionNum  """  
      self.Modifier:str = obj["Modifier"]
      self.DispDuration:str = obj["DispDuration"]
      """  Duration + Modifier  """  
      self.CustomerName:str = obj["CustomerName"]
      """  The full name for customer.  """  
      self.ShipToName:str = obj["ShipToName"]
      """  The name for the ship to location.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      self.PrcConNum:int = obj["PrcConNum"]
      self.CustID:str = obj["CustID"]
      """  The customer ID.  """  
      self.IUM:str = obj["IUM"]
      """  from FSContDt.IUM  """  
      self.OTSTaxRegionDesc:str = obj["OTSTaxRegionDesc"]
      self.ShipToCustNum:int = obj["ShipToCustNum"]
      self.ContVoid:bool = obj["ContVoid"]
      """  from FSContHd.ContVoid  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_FSContCustTrkTableset:
   def __init__(self, obj):
      self.FSContCustTrk:list[Erp_Tablesets_FSContCustTrkRow] = obj["FSContCustTrk"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_FSContDtRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier  """  
      self.ContractNum:int = obj["ContractNum"]
      """  Contract Number of the Contract  """  
      self.ContractLine:int = obj["ContractLine"]
      """  This field along with Company and ContractNum make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the FSContDtl record for the Contract and the adding 1 to it.  The user can override this number if they wish.  """  
      self.ContractCode:str = obj["ContractCode"]
      """  A unique code that identifies the Contract  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Optional field that contains the customers revision. Default from the Part.RevisionNum field.  """  
      self.LineDesc:str = obj["LineDesc"]
      """  Line Item description. The Part.Description can be used as a default.  """  
      self.IUM:str = obj["IUM"]
      """  Unit Of Measure (how it is sold/issued). Use the default Part.IUM if its a valid Part.  """  
      self.PricePerUnit:int = obj["PricePerUnit"]
      """  Price per unit for the Contract in base currency.  Defaults from the FScontCd table  """  
      self.DocPricePerUnit:int = obj["DocPricePerUnit"]
      """  Price per unit for the Contract in customers currency.  Defaults from the FScontCd table  """  
      self.ContractQty:int = obj["ContractQty"]
      """  Total Contract Quantity for the line item.  """  
      self.ProdCode:str = obj["ProdCode"]
      """  Product Group Code. Use the Part.ProdCode as a default.  This can be blank or must be valid in the ProdGrup table.  """  
      self.XPartNum:str = obj["XPartNum"]
      """  An optional field that is used if the customer has a different  Part number  than the users internal part number.  The XPartNum and PartNum can provide defaults for each other via the PartXref table.. The XPartNum can be blank, does not have to exist in the PartXref table.  """  
      self.XRevisionNum:str = obj["XRevisionNum"]
      """  Optional field that contains the customers revision. Default from the CustXPrt.RevisionNum field.  """  
      self.InvoiceComment:str = obj["InvoiceComment"]
      """  Used to establish invoice comments about the Contract line item. These will copied into the Invoice detail  file as defaults.  """  
      self.CustNum:int = obj["CustNum"]
      """  Customer number that the sales order is for. Duplicated from OrderHed.CustNum.  Used to allow efficient browsing of the FSContDt records for a specific customer.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Contains the Order Number that ties this detail record back to an OrderHed record.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  This field along with Company and OrderNum make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the OrderDtl record for the Order and the adding 1 to it.  The user can override this number if they wish.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  Project ID of the Project table record that this FSContDt record. Can be blank.  """  
      self.CommentText:str = obj["CommentText"]
      """  Editor widget for Contract comments.  """  
      self.ContractType:str = obj["ContractType"]
      """   A value of "ORD-ENT" indicates that this Service contract is related to a specific Sales Order and its line items and will be created and maintained from there, It will print on the Order acknowledgment and be invoiced with the sales order item as they are shipped.  A Value of "Cnt-Ent" indicates that this Service Contract was created from the service contract entry programs.  It is not directly related to a sales order; it will be printed by itself and invoiced by itself.
(Duplicated from FSContHd for Browse)  """  
      self.ContractComment:str = obj["ContractComment"]
      """  Contains comments about the detail contract line item. These will be printed on the Sales Acknowledgements and service contracts  """  
      self.SoldOrderNum:int = obj["SoldOrderNum"]
      """  Sold to Order Number  """  
      self.SoldOrderLine:int = obj["SoldOrderLine"]
      """  Sold To Order line  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.Rpt1PricePerUnit:int = obj["Rpt1PricePerUnit"]
      """  Reporting currency value of this field  """  
      self.Rpt2PricePerUnit:int = obj["Rpt2PricePerUnit"]
      """  Reporting currency value of this field  """  
      self.Rpt3PricePerUnit:int = obj["Rpt3PricePerUnit"]
      """  Reporting currency value of this field  """  
      self.Inactive:bool = obj["Inactive"]
      """  A value of Yes indicates the line is not part of the service contract agreement and it will not be included in the contract amounts.  """  
      self.DateInactivated:str = obj["DateInactivated"]
      """  This is the date the contract line was set to inactive.  """  
      self.BillStartDate:str = obj["BillStartDate"]
      """  This is the first date the contract line is considered for billing purposes.  """  
      self.BillEndDate:str = obj["BillEndDate"]
      """  This is the last date the contract line is considered for billing.  """  
      self.Invoiced:bool = obj["Invoiced"]
      """  Indicates this line has been invoiced.  """  
      self.DateInvoiced:str = obj["DateInvoiced"]
      """  Date this line was invoiced.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AllowUpdate:bool = obj["AllowUpdate"]
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      self.ExtPrice:int = obj["ExtPrice"]
      self.DocExtPrice:int = obj["DocExtPrice"]
      self.DisplayContractType:str = obj["DisplayContractType"]
      self.ReturnQty:int = obj["ReturnQty"]
      """  Return Quantity used in the create RMA process.  """  
      self.SelectedforRMA:bool = obj["SelectedforRMA"]
      """  Indicates if the contract line is selected to create RMA for.  """  
      self.HdCurrencyCode:str = obj["HdCurrencyCode"]
      self.HdCurrencyCodeDesc:str = obj["HdCurrencyCodeDesc"]
      self.DocCurrSymbol:str = obj["DocCurrSymbol"]
      """  Document currency symbol.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code of the related record  """  
      self.IUMDesc:str = obj["IUMDesc"]
      """  Unit of Measure Description  """  
      self.TrackSerialNumbers:bool = obj["TrackSerialNumbers"]
      self.Rpt1ExtPrice:int = obj["Rpt1ExtPrice"]
      self.Rpt2ExtPrice:int = obj["Rpt2ExtPrice"]
      self.Rpt3ExtPrice:int = obj["Rpt3ExtPrice"]
      self.PriceMulti:int = obj["PriceMulti"]
      """  The calculated PriceMulti is based on the parent FSContHd record.  """  
      self.IntExternalKey:str = obj["IntExternalKey"]
      """  Unique identifier of related integration record.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.ContractCodeContractDescription:str = obj["ContractCodeContractDescription"]
      self.CustNumBTName:str = obj["CustNumBTName"]
      self.CustNumCustID:str = obj["CustNumCustID"]
      self.CustNumName:str = obj["CustNumName"]
      self.OrderLineLineDesc:str = obj["OrderLineLineDesc"]
      self.OrderNumCurrencyCode:str = obj["OrderNumCurrencyCode"]
      self.OrderNumCardMemberName:str = obj["OrderNumCardMemberName"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.ProdCodeDescription:str = obj["ProdCodeDescription"]
      self.ProjectIDDescription:str = obj["ProjectIDDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_FSContHdListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ContractNum:int = obj["ContractNum"]
      """  When creating a new Service Contract the user is prompted for an Contract number. If the field is left blank, the next available Number is assigned by the system. The system generates a number by finding the order # of the last record on file and then a 1 to it.  """  
      self.ContractType:str = obj["ContractType"]
      """  A value of "Ord-Ent" indicates that this Service contract is related to a specific Sales Order and its line items and will be created and maintained from there, It will print on the Order acknowledgment and be invoiced with the sales order item as they are shipped.  A Value of "Cnt-Ent" indicates that this Service Contract was created from the service contract entry programs.  It is not directly related to a sales order; it will be printed by itself and invoiced by itself.  """  
      self.CustNum:int = obj["CustNum"]
      """  Contains the Customer number that the Service Contract is for.  This must be valid in the Customer table.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  The Sales order that this contract is linked to.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  The line number of the sales order that this contract is linked to  """  
      self.EntryDate:str = obj["EntryDate"]
      """  Same as OrderDate when SLSORD.  TODAY when CNTENT  """  
      self.ContractCode:str = obj["ContractCode"]
      """  A unique code that identifies the Contract  """  
      self.ContractComment:str = obj["ContractComment"]
      """  Contains comments about the overall Contract. These will be printed on the Service Contract.  """  
      self.InvoiceComment:str = obj["InvoiceComment"]
      """  Used to establish invoice comments about the overall Contract. These will copied into the Invoice detail file as defaults.  """  
      self.PrcConNum:int = obj["PrcConNum"]
      """  Contains the key  value for the Purchasing Contact. This can be blank or it must be valid in the CUSTCNT  table. Use the CUSTOMER.PRIMPCON as the default.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  Indicates which customer ship to is to be used  for the Service Contract. It  can be blank or it must be valid in the SHIPTO table. Use the CUSTOMER.SHIPTONUM as the default on new orders or when the ORDERHED.CUSTNUM is changed.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """   Exchange rate that will be used for this Contract.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  """  
      self.LockRate:bool = obj["LockRate"]
      """  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  This will also be the default for the invoice.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """   This is used as one of the selection parameters on the Service Contract entry edit reports. The intent is for users to be able to select Contract that they have entered for hard copy edit.
On new orders use the users login ID as the default. They can override this if they wish to enter something more meaningful.  """  
      self.ContVoid:bool = obj["ContVoid"]
      """  This Service Contract has been deactivated when TRUE  """  
      self.ShpConNum:int = obj["ShpConNum"]
      """  Establishes the Shipping Contact to be used.  In this case the contact at the location where the item the service contract is covering are. Contains the key value for the shipping contact in the CUSTCNT table. Can be blank or must be valid in the CUSTCNT table. Use the Customer.PrimScon as a default.  """  
      self.ActiveDate:str = obj["ActiveDate"]
      """   The date of the earliest FscontSp.activateDate for this contract.
Not user maintainable.  It is written when the fscontsp record is created or changed. This will always be the earliest activate date on this contract.  """  
      self.ExpireDate:str = obj["ExpireDate"]
      """   The date of the Latest FscontSp.ExpirationDate for this contract.
Not user maintainable.  It is written when the fscontsp record is created or changed.  this will always be the Latest activate date on this contract.  """  
      self.Duration:int = obj["Duration"]
      """  Duration of Contract  """  
      self.Modifier:str = obj["Modifier"]
      """  Whether the duration is for Days, Months, years.  """  
      self.Material:bool = obj["Material"]
      """  Coverage  for material  """  
      self.Labor:bool = obj["Labor"]
      """  Coverage for Labor  """  
      self.Misc:bool = obj["Misc"]
      """  Coverage for Misc charges. This includes the miscellaneous expenses like travel, etc.  """  
      self.Invoiced:bool = obj["Invoiced"]
      """  The invoice for this Service contract  has been created. The Order line that this contract is linked to has shipped.  """  
      self.PackNum:int = obj["PackNum"]
      """  Packing slip number that this detail record is linked with.  """  
      self.PackLine:int = obj["PackLine"]
      """  An integer that Ties the Contract record to a packing slip detail line  """  
      self.OnSite:bool = obj["OnSite"]
      """  This contract covers on site visits  """  
      self.RecurringInv:bool = obj["RecurringInv"]
      """  Indicates that Service Contract with this Code will generate recurring invoices.  """  
      self.RecurringFreq:str = obj["RecurringFreq"]
      """  The frequency that recurring invoices are generated only 'monthly' for now.  """  
      self.PricePer:str = obj["PricePer"]
      """  Price modifier for unit price field Daily, monthly, Contract(Full length of the contract)  """  
      self.LastInvGen:bool = obj["LastInvGen"]
      """  This flag is set to TRUE after the last recurring invoice is generated for the contract.  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  The invoice number of the last recurring invoice.  """  
      self.TaxCatID:str = obj["TaxCatID"]
      """  Indicates the Tax Category for this record.  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.BTCustNum:int = obj["BTCustNum"]
      """  Bill To Customer Number  """  
      self.UseOTS:bool = obj["UseOTS"]
      """   Indicates if the One Time ShipTo information should be used instead of the standard ShipTo.  One Time ShipTo info is stored in this record in the fields prefixed with "OTS"
Note: This can only be true when if the OTSName is not blank. 
UI disables this when Customer.AllowQTS = False,  """  
      self.OTSName:str = obj["OTSName"]
      """  One Time Shipto Name of the ShipTo.  """  
      self.OTSAddress1:str = obj["OTSAddress1"]
      """  One Time Shipto first line of the ShipTo address.  """  
      self.OTSAddress2:str = obj["OTSAddress2"]
      """  One Time Shipto  second line of the ShipTo address.  """  
      self.OTSAddress3:str = obj["OTSAddress3"]
      """  One Time Shipto  third line of the ShipTo address.  """  
      self.OTSCity:str = obj["OTSCity"]
      """  City portion of the One Time Shipto  address.  """  
      self.OTSState:str = obj["OTSState"]
      """  The state or province portion of the One Time Shipto  address.  """  
      self.OTSZIP:str = obj["OTSZIP"]
      """  The zip or postal code portion of the One Time ShipTo  address.  """  
      self.OTSResaleID:str = obj["OTSResaleID"]
      """  The State Tax Identification Number of the One Time Shipto.  """  
      self.OTSTaxRegionCode:str = obj["OTSTaxRegionCode"]
      """  Contains the TaxRgn.TaxRegionCode value of the One Time ShipTo tax region for purposes of Sales Tax calculations.  """  
      self.OTSContact:str = obj["OTSContact"]
      """  Full name of the contact.  """  
      self.OTSFaxNum:str = obj["OTSFaxNum"]
      """  Fax number for the One Time ShipTo.  """  
      self.OTSPhoneNum:str = obj["OTSPhoneNum"]
      """  Phone number for the One Time ShipTo  """  
      self.OTSCountryNum:int = obj["OTSCountryNum"]
      """  One Time Shipping country Number.  """  
      self.ShipToCustNum:int = obj["ShipToCustNum"]
      """  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  """  
      self.DeferredRev:bool = obj["DeferredRev"]
      """  Indicates if revenue is deferred for contracts assigned to this group.  """  
      self.RACode:str = obj["RACode"]
      """  Revenue Amortization Code.  """  
      self.DefRevStart:str = obj["DefRevStart"]
      """  Starting date the revenue is deferred.  """  
      self.Suspended:bool = obj["Suspended"]
      """  Indicates if the contract has been suspended.  A suspended contract cannot have any calls linked to it.  """  
      self.QuotedContract:bool = obj["QuotedContract"]
      """  Indicates if the contrct will automatically generate a quote  """  
      self.ShipContract:bool = obj["ShipContract"]
      """  Defaulted from the service contract code.  Determines whether or not the contract can be invoiced directly or if it must be shipped.  When yes the contract must be added to a sales order and then shipped prior to invoicing.  """  
      self.TaskSetID:str = obj["TaskSetID"]
      """  Unique identifier of the task set assigned by the user.  """  
      self.ReadyToInvoice:bool = obj["ReadyToInvoice"]
      """  Indicates if the contract is ready to be invoiced.   This is only available when ShipContract = no.  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Quote number to which this line item detail record is associated with. This is part of the foreign key to OrderHed file.  """  
      self.QuoteLine:int = obj["QuoteLine"]
      """  This field along with Company and QuoteNum make up the unique key to the table. The system generates this number during entry of new detail records. The system determines next available number by finding the QuoteDtl record for the Quote and the adding 1 to it.  """  
      self.QuoteAccepted:bool = obj["QuoteAccepted"]
      """  Indicates the Quote has been accepted  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.OTSCountry:str = obj["OTSCountry"]
      self.ContractStartup:bool = obj["ContractStartup"]
      self.SoldToPhoneNum:str = obj["SoldToPhoneNum"]
      self.SoldToFaxNum:str = obj["SoldToFaxNum"]
      self.SoldToContactName:str = obj["SoldToContactName"]
      self.ShipToPhoneNum:str = obj["ShipToPhoneNum"]
      self.ShipToFaxNum:str = obj["ShipToFaxNum"]
      self.ShipToContactName:str = obj["ShipToContactName"]
      self.ContractExpired:bool = obj["ContractExpired"]
      self.ContractTotal:int = obj["ContractTotal"]
      self.DocContractTotal:int = obj["DocContractTotal"]
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      self.EnableBillTo:bool = obj["EnableBillTo"]
      self.EnableShipTo:bool = obj["EnableShipTo"]
      self.EnableCurrency:bool = obj["EnableCurrency"]
      self.AllowUpdate:bool = obj["AllowUpdate"]
      self.DisplayContractType:str = obj["DisplayContractType"]
      self.ShipToAddressList:str = obj["ShipToAddressList"]
      self.SoldToAddressList:str = obj["SoldToAddressList"]
      self.PartOrderDtlList:str = obj["PartOrderDtlList"]
      self.opMessage:str = obj["opMessage"]
      self.Rpt1ContractTotal:int = obj["Rpt1ContractTotal"]
      self.Rpt2ContractTotal:int = obj["Rpt2ContractTotal"]
      self.Rpt3ContractTotal:int = obj["Rpt3ContractTotal"]
      self.CustAllowOTS:bool = obj["CustAllowOTS"]
      """  Customer.AllowOTS value. Allow One Time Shipto.  """  
      self.BTCustName:str = obj["BTCustName"]
      """  Name of the Bill To Customer  """  
      self.AvailBTCustList:str = obj["AvailBTCustList"]
      """  Delimited list of available bill to customers.  """  
      self.BaseCurrencyID:str = obj["BaseCurrencyID"]
      self.RenewedUntil:str = obj["RenewedUntil"]
      """  The expire date of the last effective renewed contract  """  
      self.RenewalTotal:int = obj["RenewalTotal"]
      self.DocRenewalTotal:int = obj["DocRenewalTotal"]
      self.Rpt1RenewalTotal:int = obj["Rpt1RenewalTotal"]
      self.Rpt2RenewalTotal:int = obj["Rpt2RenewalTotal"]
      self.Rpt3RenewalTotal:int = obj["Rpt3RenewalTotal"]
      self.ContractRenewed:bool = obj["ContractRenewed"]
      self.EnableRenewal:bool = obj["EnableRenewal"]
      """  Flag to indicate if the service contract can be renewed.  """  
      self.ContractCodeContractDescription:str = obj["ContractCodeContractDescription"]
      """  Description of the service contract.  """  
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      """  Description of the currency  """  
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      """  A symbol that identifies the currency. Used on Forms and displays  """  
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      """  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  """  
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      """   An extended description that can be used on documents such as
POs and invoices.  """  
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      """   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  """  
      self.CustNumBTName:str = obj["CustNumBTName"]
      """  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  """  
      self.CustNumCustID:str = obj["CustNumCustID"]
      """  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  """  
      self.CustNumName:str = obj["CustNumName"]
      """  The full name of the customer.  """  
      self.CustNumAllowShipTo3:bool = obj["CustNumAllowShipTo3"]
      """  When yes, a ShipTo CustID on certain forms will be enabled. This allows a shipto of a different customer to be referenced as a 3rd party for a document.  """  
      self.InvoiceNumCardMemberName:str = obj["InvoiceNumCardMemberName"]
      """  The member's name on the credit card.  """  
      self.InvoiceNumTermsCode:str = obj["InvoiceNumTermsCode"]
      """  Contains the foreign key to the TERMS master file.  Defaults from OrderHed if OrderNum > 0 else from the Customer master. This IS A MANDATORY ENTRY. User maintainable via a combo-box for terms description.  """  
      self.OrderLineLineDesc:str = obj["OrderLineLineDesc"]
      """  Line Item description. The Part.Description can be used as a default.  """  
      self.OrderNumCurrencyCode:str = obj["OrderNumCurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.OrderNumCardMemberName:str = obj["OrderNumCardMemberName"]
      """  The member's name on the credit card.  """  
      self.OTSTaxRegionCodeDescription:str = obj["OTSTaxRegionCodeDescription"]
      """  Full description for the Tax Region.  """  
      self.PackLineLineDesc:str = obj["PackLineLineDesc"]
      """  Line description.  """  
      self.PackNumName:str = obj["PackNumName"]
      """  Name of the ShipTo. When creating new records the Customer.Name is used as a default.  This can't be blank.  """  
      self.RACodeRADesc:str = obj["RACodeRADesc"]
      """  Free form text describing the revenue amortization code.  """  
      self.ShipToBTName:str = obj["ShipToBTName"]
      """  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  """  
      self.ShipToCustID:str = obj["ShipToCustID"]
      """  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  """  
      self.ShipToName:str = obj["ShipToName"]
      """  The full name of the customer.  """  
      self.TaxCatIDDescription:str = obj["TaxCatIDDescription"]
      """  Full description for the Sales Tax category.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_FSContHdListTableset:
   def __init__(self, obj):
      self.FSContHdList:list[Erp_Tablesets_FSContHdListRow] = obj["FSContHdList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_FSContHdRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ContractNum:int = obj["ContractNum"]
      """  When creating a new Service Contract the user is prompted for an Contract number. If the field is left blank, the next available Number is assigned by the system. The system generates a number by finding the order # of the last record on file and then a 1 to it.  """  
      self.ContractType:str = obj["ContractType"]
      """  A value of "Ord-Ent" indicates that this Service contract is related to a specific Sales Order and its line items and will be created and maintained from there, It will print on the Order acknowledgment and be invoiced with the sales order item as they are shipped.  A Value of "Cnt-Ent" indicates that this Service Contract was created from the service contract entry programs.  It is not directly related to a sales order; it will be printed by itself and invoiced by itself.  """  
      self.CustNum:int = obj["CustNum"]
      """  Contains the Customer number that the Service Contract is for.  This must be valid in the Customer table.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  The Sales order that this contract is linked to.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  The line number of the sales order that this contract is linked to  """  
      self.EntryDate:str = obj["EntryDate"]
      """  Same as OrderDate when SLSORD.  TODAY when CNTENT  """  
      self.ContractCode:str = obj["ContractCode"]
      """  A unique code that identifies the Contract  """  
      self.ContractComment:str = obj["ContractComment"]
      """  Contains comments about the overall Contract. These will be printed on the Service Contract.  """  
      self.InvoiceComment:str = obj["InvoiceComment"]
      """  Used to establish invoice comments about the overall Contract. These will copied into the Invoice detail file as defaults.  """  
      self.PrcConNum:int = obj["PrcConNum"]
      """  Contains the key  value for the Purchasing Contact. This can be blank or it must be valid in the CUSTCNT  table. Use the CUSTOMER.PRIMPCON as the default.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  Indicates which customer ship to is to be used  for the Service Contract. It  can be blank or it must be valid in the SHIPTO table. Use the CUSTOMER.SHIPTONUM as the default on new orders or when the ORDERHED.CUSTNUM is changed.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """   Exchange rate that will be used for this Contract.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  """  
      self.LockRate:bool = obj["LockRate"]
      """  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  This will also be the default for the invoice.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """   This is used as one of the selection parameters on the Service Contract entry edit reports. The intent is for users to be able to select Contract that they have entered for hard copy edit.
On new orders use the users login ID as the default. They can override this if they wish to enter something more meaningful.  """  
      self.ContVoid:bool = obj["ContVoid"]
      """  This Service Contract has been deactivated when TRUE  """  
      self.ShpConNum:int = obj["ShpConNum"]
      """  Establishes the Shipping Contact to be used.  In this case the contact at the location where the item the service contract is covering are. Contains the key value for the shipping contact in the CUSTCNT table. Can be blank or must be valid in the CUSTCNT table. Use the Customer.PrimScon as a default.  """  
      self.ActiveDate:str = obj["ActiveDate"]
      """   The date of the earliest FscontSp.activateDate for this contract.
Not user maintainable.  It is written when the fscontsp record is created or changed. This will always be the earliest activate date on this contract.  """  
      self.ExpireDate:str = obj["ExpireDate"]
      """   The date of the Latest FscontSp.ExpirationDate for this contract.
Not user maintainable.  It is written when the fscontsp record is created or changed.  this will always be the Latest activate date on this contract.  """  
      self.Duration:int = obj["Duration"]
      """  Duration of Contract  """  
      self.Modifier:str = obj["Modifier"]
      """  Whether the duration is for Days, Months, years.  """  
      self.Material:bool = obj["Material"]
      """  Coverage  for material  """  
      self.Labor:bool = obj["Labor"]
      """  Coverage for Labor  """  
      self.Misc:bool = obj["Misc"]
      """  Coverage for Misc charges. This includes the miscellaneous expenses like travel, etc.  """  
      self.Invoiced:bool = obj["Invoiced"]
      """  The invoice for this Service contract  has been created. The Order line that this contract is linked to has shipped.  """  
      self.PackNum:int = obj["PackNum"]
      """  Packing slip number that this detail record is linked with.  """  
      self.PackLine:int = obj["PackLine"]
      """  An integer that Ties the Contract record to a packing slip detail line  """  
      self.OnSite:bool = obj["OnSite"]
      """  This contract covers on site visits  """  
      self.RecurringInv:bool = obj["RecurringInv"]
      """  Indicates that Service Contract with this Code will generate recurring invoices.  """  
      self.RecurringFreq:str = obj["RecurringFreq"]
      """  The frequency that recurring invoices are generated only 'monthly' for now.  """  
      self.PricePer:str = obj["PricePer"]
      """  Price modifier for unit price field Daily, monthly, Contract(Full length of the contract)  """  
      self.LastInvGen:bool = obj["LastInvGen"]
      """  This flag is set to TRUE after the last recurring invoice is generated for the contract.  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  The invoice number of the last recurring invoice.  """  
      self.TaxCatID:str = obj["TaxCatID"]
      """  Indicates the Tax Category for this record.  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.BTCustNum:int = obj["BTCustNum"]
      """  Bill To Customer Number  """  
      self.UseOTS:bool = obj["UseOTS"]
      """   Indicates if the One Time ShipTo information should be used instead of the standard ShipTo.  One Time ShipTo info is stored in this record in the fields prefixed with "OTS"
Note: This can only be true when if the OTSName is not blank. 
UI disables this when Customer.AllowQTS = False,  """  
      self.OTSName:str = obj["OTSName"]
      """  One Time Shipto Name of the ShipTo.  """  
      self.OTSAddress1:str = obj["OTSAddress1"]
      """  One Time Shipto first line of the ShipTo address.  """  
      self.OTSAddress2:str = obj["OTSAddress2"]
      """  One Time Shipto  second line of the ShipTo address.  """  
      self.OTSAddress3:str = obj["OTSAddress3"]
      """  One Time Shipto  third line of the ShipTo address.  """  
      self.OTSCity:str = obj["OTSCity"]
      """  City portion of the One Time Shipto  address.  """  
      self.OTSState:str = obj["OTSState"]
      """  The state or province portion of the One Time Shipto  address.  """  
      self.OTSZIP:str = obj["OTSZIP"]
      """  The zip or postal code portion of the One Time ShipTo  address.  """  
      self.OTSResaleID:str = obj["OTSResaleID"]
      """  The State Tax Identification Number of the One Time Shipto.  """  
      self.OTSTaxRegionCode:str = obj["OTSTaxRegionCode"]
      """  Contains the TaxRgn.TaxRegionCode value of the One Time ShipTo tax region for purposes of Sales Tax calculations.  """  
      self.OTSContact:str = obj["OTSContact"]
      """  Full name of the contact.  """  
      self.OTSFaxNum:str = obj["OTSFaxNum"]
      """  Fax number for the One Time ShipTo.  """  
      self.OTSPhoneNum:str = obj["OTSPhoneNum"]
      """  Phone number for the One Time ShipTo  """  
      self.OTSCountryNum:int = obj["OTSCountryNum"]
      """  One Time Shipping country Number.  """  
      self.ShipToCustNum:int = obj["ShipToCustNum"]
      """  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  """  
      self.DeferredRev:bool = obj["DeferredRev"]
      """  Indicates if revenue is deferred for contracts assigned to this group.  """  
      self.RACode:str = obj["RACode"]
      """  Revenue Amortization Code.  """  
      self.DefRevStart:str = obj["DefRevStart"]
      """  Starting date the revenue is deferred.  """  
      self.Suspended:bool = obj["Suspended"]
      """  Indicates if the contract has been suspended.  A suspended contract cannot have any calls linked to it.  """  
      self.QuotedContract:bool = obj["QuotedContract"]
      """  Indicates if the contrct will automatically generate a quote  """  
      self.ShipContract:bool = obj["ShipContract"]
      """  Defaulted from the service contract code.  Determines whether or not the contract can be invoiced directly or if it must be shipped.  When yes the contract must be added to a sales order and then shipped prior to invoicing.  """  
      self.TaskSetID:str = obj["TaskSetID"]
      """  Unique identifier of the task set assigned by the user.  """  
      self.ReadyToInvoice:bool = obj["ReadyToInvoice"]
      """  Indicates if the contract is ready to be invoiced.   This is only available when ShipContract = no.  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Quote number to which this line item detail record is associated with. This is part of the foreign key to OrderHed file.  """  
      self.QuoteLine:int = obj["QuoteLine"]
      """  This field along with Company and QuoteNum make up the unique key to the table. The system generates this number during entry of new detail records. The system determines next available number by finding the QuoteDtl record for the Quote and the adding 1 to it.  """  
      self.QuoteAccepted:bool = obj["QuoteAccepted"]
      """  Indicates the Quote has been accepted  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.InvcTiming:str = obj["InvcTiming"]
      """  InvcTiming  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  Indicates how often an invoice is generated for the contract.  """  
      self.Renewable:bool = obj["Renewable"]
      """  Indicates if the service contract using is valid for renewal.  """  
      self.IncIntrastat:bool = obj["IncIntrastat"]
      """  Intrastat: Activates HS Commodity code retrieving in contract invoicing  """  
      self.SendToFSA:bool = obj["SendToFSA"]
      """  Determines if the service contract has to be synchronized with Epicor FSA application.  """  
      self.OTSTaxValidationStatus:int = obj["OTSTaxValidationStatus"]
      """  OTSTaxValidationStatus  """  
      self.OTSTaxValidationDate:str = obj["OTSTaxValidationDate"]
      """  OTSTaxValidationDate  """  
      self.AllowUpdate:bool = obj["AllowUpdate"]
      self.AvailBTCustList:str = obj["AvailBTCustList"]
      """  Delimited list of available bill to customers.  """  
      self.BaseCurrencyID:str = obj["BaseCurrencyID"]
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      self.BTCustName:str = obj["BTCustName"]
      """  Name of the Bill To Customer  """  
      self.ContractExpired:bool = obj["ContractExpired"]
      self.ContractRenewed:bool = obj["ContractRenewed"]
      self.ContractStartup:bool = obj["ContractStartup"]
      self.ContractTotal:int = obj["ContractTotal"]
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.CustAllowOTS:bool = obj["CustAllowOTS"]
      """  Customer.AllowOTS value. Allow One Time Shipto.  """  
      self.DisplayContractType:str = obj["DisplayContractType"]
      self.DocContractTotal:int = obj["DocContractTotal"]
      self.DocRenewalTotal:int = obj["DocRenewalTotal"]
      self.EnableBillTo:bool = obj["EnableBillTo"]
      self.EnableCurrency:bool = obj["EnableCurrency"]
      self.EnableQuote:bool = obj["EnableQuote"]
      self.EnableRenewable:bool = obj["EnableRenewable"]
      """  Flag to indicate when to enable the Renewable check box.  The flag is set to no if the current contract has been renewed already (FSRenewal exists).  """  
      self.EnableRenewal:bool = obj["EnableRenewal"]
      """  Flag to indicate if the service contract can be renewed.  (This flag should not be confused with EnableRenewable.)  This EnableRenewal is used to check if the current original contract (FSContHd) or the latest contract renewal (FSRenewal) (whichever is currently actve) meets the expiration date check against the expire horizon and contract renewal period set at FSSyst table.  """  
      self.EnableShipTo:bool = obj["EnableShipTo"]
      self.FiscalCalDescription:str = obj["FiscalCalDescription"]
      self.opMessage:str = obj["opMessage"]
      self.OTSCountry:str = obj["OTSCountry"]
      self.PartOrderDtlList:str = obj["PartOrderDtlList"]
      self.ReadyToQuote:bool = obj["ReadyToQuote"]
      """  Flag to indicate if the Contract is ready to be quoted.  """  
      self.RenewalTotal:int = obj["RenewalTotal"]
      self.RenewedUntil:str = obj["RenewedUntil"]
      """  The expire date of the last effective renewed contract  """  
      self.Rpt1ContractTotal:int = obj["Rpt1ContractTotal"]
      self.Rpt1RenewalTotal:int = obj["Rpt1RenewalTotal"]
      self.Rpt2ContractTotal:int = obj["Rpt2ContractTotal"]
      self.Rpt2RenewalTotal:int = obj["Rpt2RenewalTotal"]
      self.Rpt3ContractTotal:int = obj["Rpt3ContractTotal"]
      self.Rpt3RenewalTotal:int = obj["Rpt3RenewalTotal"]
      self.ShipToAddressList:str = obj["ShipToAddressList"]
      self.ShipToContactName:str = obj["ShipToContactName"]
      self.ShipToFaxNum:str = obj["ShipToFaxNum"]
      self.ShipToPhoneNum:str = obj["ShipToPhoneNum"]
      self.SoldToAddressList:str = obj["SoldToAddressList"]
      self.SoldToContactName:str = obj["SoldToContactName"]
      self.SoldToFaxNum:str = obj["SoldToFaxNum"]
      self.SoldToPhoneNum:str = obj["SoldToPhoneNum"]
      self.UninvoicedLine:bool = obj["UninvoicedLine"]
      """  Flag to indicate if additional uninvoiced contract line has been added after the contract has been invoiced.  """  
      self.UpdateLineDates:bool = obj["UpdateLineDates"]
      self.FSAServiceAgreementNum:int = obj["FSAServiceAgreementNum"]
      """  Used to indicate which FSA Service Agreement a Contract Renewal is related to.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CompanySendToFSA:bool = obj["CompanySendToFSA"]
      self.ContractCodeContractDescription:str = obj["ContractCodeContractDescription"]
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      self.CustNumCustID:str = obj["CustNumCustID"]
      self.CustNumAllowShipTo3:bool = obj["CustNumAllowShipTo3"]
      self.CustNumName:str = obj["CustNumName"]
      self.CustNumBTName:str = obj["CustNumBTName"]
      self.CustNumSendToFSA:bool = obj["CustNumSendToFSA"]
      self.InvoiceNumCardMemberName:str = obj["InvoiceNumCardMemberName"]
      self.InvoiceNumTermsCode:str = obj["InvoiceNumTermsCode"]
      self.OrderLineLineDesc:str = obj["OrderLineLineDesc"]
      self.OrderNumCurrencyCode:str = obj["OrderNumCurrencyCode"]
      self.OrderNumCardMemberName:str = obj["OrderNumCardMemberName"]
      self.OTSCountryEUMember:bool = obj["OTSCountryEUMember"]
      self.OTSCountryISOCode:str = obj["OTSCountryISOCode"]
      self.OTSTaxRegionCodeDescription:str = obj["OTSTaxRegionCodeDescription"]
      self.PackLineLineDesc:str = obj["PackLineLineDesc"]
      self.PackNumName:str = obj["PackNumName"]
      self.RACodeRADesc:str = obj["RACodeRADesc"]
      self.ShipToBTName:str = obj["ShipToBTName"]
      self.ShipToName:str = obj["ShipToName"]
      self.ShipToCustID:str = obj["ShipToCustID"]
      self.ShipToNumInactive:bool = obj["ShipToNumInactive"]
      self.ShipToNumName:str = obj["ShipToNumName"]
      self.TaskSetWorkflowType:str = obj["TaskSetWorkflowType"]
      self.TaskSetTaskSetDescription:str = obj["TaskSetTaskSetDescription"]
      self.TaxCatIDDescription:str = obj["TaxCatIDDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_FSContLabExpRateRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ContractNum:int = obj["ContractNum"]
      """  ContractNum  """  
      self.ExpenseCode:str = obj["ExpenseCode"]
      """  ExpenseCode  """  
      self.RateType:int = obj["RateType"]
      """  RateType  """  
      self.RateMultiplier:int = obj["RateMultiplier"]
      """  RateMultiplier  """  
      self.FixedRate:int = obj["FixedRate"]
      """  FixedRate  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_FSContOrderDtlListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Contains the Order Number that ties this detail record back to an OrderHed record.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  This field along with Company and OrderNum make up the unique key to the OrderHed table.  """  
      self.PartNum:str = obj["PartNum"]
      """  The user's Internal Part number used to identify Order line item part.  """  
      self.LineDesc:str = obj["LineDesc"]
      """  Order Line Item description. The Part.Description can be used as a default.  """  
      self.LineStatus:str = obj["LineStatus"]
      """  Status of Order Line  """  
      self.Selected:bool = obj["Selected"]
      """  boolean flag to indicate user has selected this row  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for OrderDtl  row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_FSContSNRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier  """  
      self.ContractNum:int = obj["ContractNum"]
      """  Contract Number of the Contract  """  
      self.ContractLine:int = obj["ContractLine"]
      """  This field along with Company and ContractNum make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the FSContDtl record for the Contract and the adding 1 to it.  The user can override this number if they wish.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part. Not directly maintainable. Mirror image of FSContDt.PartNum. Having this field, allows a SerialNo record to find the contracts that it is related to.  """  
      self.SerialNumber:str = obj["SerialNumber"]
      """  Serial number of the Part that is assigned to this Field Service contract line.  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AutoAdd:bool = obj["AutoAdd"]
      """  True indicates that the FSContSN record was auto added by CustShip or DropShip processing  """  
      self.ExpireDate:str = obj["ExpireDate"]
      """  Expire Date of the contract, for display in Serial Number tracker  """  
      self.FSContCdDesc:str = obj["FSContCdDesc"]
      """  Description of the contract header contract type, for display in SerialNo tracker  """  
      self.IntExternalKey:str = obj["IntExternalKey"]
      """  Unique identifier of related integration record.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_FSRenewalDtRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ContractNum:int = obj["ContractNum"]
      """  When creating a new Service Contract the user is prompted for an Contract number. If the field is left blank, the next available Number is assigned by the system. The system generates a number by finding the order # of the last record on file and then a 1 to it.  """  
      self.RenewalNbr:int = obj["RenewalNbr"]
      """  Contract renewal number. If the value is zero then the contract is not for a renewal.  """  
      self.RenewalLine:int = obj["RenewalLine"]
      """  This field along with Company and ContractNum make up the unique key to the table.  """  
      self.ContractLine:int = obj["ContractLine"]
      """  This field along with Company and ContractNum make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the FSContDtl record for the Contract and the adding 1 to it.  The user can override this number if they wish.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Optional field that contains the customers revision. Default from the Part.RevisionNum field.  """  
      self.LineDesc:str = obj["LineDesc"]
      """  Line Item description. The Part.Description can be used as a default.  """  
      self.IUM:str = obj["IUM"]
      """  Unit Of Measure (how it is sold/issued). Use the default Part.IUM if its a valid Part.  """  
      self.IncreasePct:int = obj["IncreasePct"]
      """  The percentage increase of the renewal price.  """  
      self.PricePerUnit:int = obj["PricePerUnit"]
      """  Price per unit for the Contract in base currency.  Defaults from the FScontCd table  """  
      self.DocPricePerUnit:int = obj["DocPricePerUnit"]
      """  Price per unit for the Contract in customers currency.  Defaults from the FScontCd table  """  
      self.Rpt1PricePerUnit:int = obj["Rpt1PricePerUnit"]
      """  Reporting currency value of this field  """  
      self.Rpt2PricePerUnit:int = obj["Rpt2PricePerUnit"]
      """  Reporting currency value of this field  """  
      self.Rpt3PricePerUnit:int = obj["Rpt3PricePerUnit"]
      """  Reporting currency value of this field  """  
      self.ContractQty:int = obj["ContractQty"]
      """  Total Contract Quantity for the line item.  """  
      self.XPartNum:str = obj["XPartNum"]
      """  An optional field that is used if the customer has a different  Part number  than the users internal part number.  The XPartNum and PartNum can provide defaults for each other via the PartXref table.. The XPartNum can be blank, does not have to exist in the PartXref table.  """  
      self.XRevisionNum:str = obj["XRevisionNum"]
      """  Optional field that contains the customers revision. Default from the CustXPrt.RevisionNum field.  """  
      self.CustNum:int = obj["CustNum"]
      """  Customer number that the sales order is for. Duplicated from OrderHed.CustNum.  Used to allow efficient browsing of the FSContDt records for a specific customer.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Contains the Order Number that ties this detail record back to an OrderHed record.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  This field along with Company and OrderNum make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the OrderDtl record for the Order and the adding 1 to it.  The user can override this number if they wish.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  Project ID of the Project table record that this FSContDt record. Can be blank.  """  
      self.Inactive:bool = obj["Inactive"]
      """  A value of Yes indicates the line is not part of the service contract agreement and it will not be included in the contract amounts.  """  
      self.DateInactivated:str = obj["DateInactivated"]
      """  This is the date the contract line was set to inactive.  """  
      self.BillStartDate:str = obj["BillStartDate"]
      """  This is the first date the contract line is considered for billing purposes.  """  
      self.BillEndDate:str = obj["BillEndDate"]
      """  This is the last date the contract line is considered for billing.  """  
      self.Invoiced:bool = obj["Invoiced"]
      """  Indicates this line has been invoiced.  """  
      self.DateInvoiced:str = obj["DateInvoiced"]
      """  Date this line was invoiced.  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RefRenewalNbr:int = obj["RefRenewalNbr"]
      """  The RefRenewalNbr stores the reference renewal number of the renewal record was copied.  """  
      self.ProdCode:str = obj["ProdCode"]
      """  It is a unique code used to identify a specific product group.  """  
      self.SoldOrderNum:int = obj["SoldOrderNum"]
      """  Sales Order Num related to this FSContDt record.  """  
      self.SoldOrderLine:int = obj["SoldOrderLine"]
      """  Sales Order Line related to this FSContDt record.  """  
      self.AllowUpdate:bool = obj["AllowUpdate"]
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.DocCurrSymbol:str = obj["DocCurrSymbol"]
      self.DocExtendedPrice:int = obj["DocExtendedPrice"]
      self.DocOrigPricePerUnit:int = obj["DocOrigPricePerUnit"]
      self.ExtendedPrice:int = obj["ExtendedPrice"]
      """  Extended Price of the Contract Renewal Line  """  
      self.IUMDesc:str = obj["IUMDesc"]
      self.OrigContractQty:int = obj["OrigContractQty"]
      """  Original Contract Qty of the Contract Line  """  
      self.OrigIUM:str = obj["OrigIUM"]
      """  Original IUM of the Contract Line  """  
      self.OrigIUMDesc:str = obj["OrigIUMDesc"]
      self.OrigPricePerUnit:int = obj["OrigPricePerUnit"]
      """  Original Price Per Unit of the Contract Line  """  
      self.PriceMulti:int = obj["PriceMulti"]
      """  The calculated PriceMulti is based on the parent FSRenewal record.  """  
      self.ProdCodeDescription:str = obj["ProdCodeDescription"]
      self.Rpt1ExtendedPrice:int = obj["Rpt1ExtendedPrice"]
      self.Rpt1OrigPricePerUnit:int = obj["Rpt1OrigPricePerUnit"]
      self.Rpt2ExtendedPrice:int = obj["Rpt2ExtendedPrice"]
      self.Rpt2OrigPricePerUnit:int = obj["Rpt2OrigPricePerUnit"]
      self.Rpt3ExtendedPrice:int = obj["Rpt3ExtendedPrice"]
      self.Rpt3OrigPricePerUnit:int = obj["Rpt3OrigPricePerUnit"]
      self.TrackSerialNumbers:bool = obj["TrackSerialNumbers"]
      self.IntExternalKey:str = obj["IntExternalKey"]
      """  Unique identifier of related integration record.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CustNumCustID:str = obj["CustNumCustID"]
      self.CustNumName:str = obj["CustNumName"]
      self.CustNumBTName:str = obj["CustNumBTName"]
      self.OrderLineLineDesc:str = obj["OrderLineLineDesc"]
      self.OrderNumCardMemberName:str = obj["OrderNumCardMemberName"]
      self.OrderNumCurrencyCode:str = obj["OrderNumCurrencyCode"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.ProjectIDDescription:str = obj["ProjectIDDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_FSRenewalRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ContractNum:int = obj["ContractNum"]
      """  When creating a new Service Contract the user is prompted for an Contract number. If the field is left blank, the next available Number is assigned by the system. The system generates a number by finding the order # of the last record on file and then a 1 to it.  """  
      self.RenewalNbr:int = obj["RenewalNbr"]
      """  Contract renewal number. If the value is zero then the contract is not for a renewal.  """  
      self.QuotedRenewal:bool = obj["QuotedRenewal"]
      """  Indicates if the renwal will automatically generate a quote.  """  
      self.TaskSetID:str = obj["TaskSetID"]
      """  Unique identifier of the task set assigned by the user.  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Quote number to which this line item detail record is associated with. This is part of the foreign key to OrderHed file.  """  
      self.QuoteLine:int = obj["QuoteLine"]
      """  This field along with Company and QuoteNum make up the unique key to the table. The system generates this number during entry of new detail records. The system determines next available number by finding the QuoteDtl record for the Quote and the adding 1 to it.  """  
      self.QuoteAccepted:bool = obj["QuoteAccepted"]
      """  Indicates the Quote has been accepted.  """  
      self.RenewalCode:str = obj["RenewalCode"]
      """  This is the contract code assigned to the renewal.  """  
      self.ShipRenewal:bool = obj["ShipRenewal"]
      """  Defaulted from the service contract code.  Determines whether or not the renewal can be invoiced directly or if it must be shipped.  When yes the contract must be added to a sales order and then shipped prior to invoicing.  """  
      self.RACode:str = obj["RACode"]
      """  Revenue Amortization Code.  """  
      self.DeferredRev:bool = obj["DeferredRev"]
      """  Indicates if revenue is deferred for contracts assigned to this group.  """  
      self.DefRevStart:str = obj["DefRevStart"]
      """  Starting date the revenue is deferred.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """   Exchange rate that will be used for this Contract.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  """  
      self.LockRate:bool = obj["LockRate"]
      """  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  This will also be the default for the invoice.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """   This is used as one of the selection parameters on the Service Contract entry edit reports. The intent is for users to be able to select Contract that they have entered for hard copy edit.
On new orders use the users login ID as the default. They can override this if they wish to enter something more meaningful.  """  
      self.EntryDate:str = obj["EntryDate"]
      """  Date the renewal was created.  """  
      self.Material:bool = obj["Material"]
      """  Coverage  for material  """  
      self.Labor:bool = obj["Labor"]
      """  Coverage for Labor  """  
      self.Misc:bool = obj["Misc"]
      """  Coverage for Misc charges. This includes the miscellaneous expenses like travel, etc.  """  
      self.OnSite:bool = obj["OnSite"]
      """  This contract covers on site visits  """  
      self.Invoiced:bool = obj["Invoiced"]
      """  The invoice for this Service contract  has been created. The Order line that this contract is linked to has shipped.  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  The invoice number of the last recurring invoice.  """  
      self.PackNum:int = obj["PackNum"]
      """  Packing slip number that this detail record is linked with.  """  
      self.PackLine:int = obj["PackLine"]
      """  An integer that Ties the Contract record to a packing slip detail line  """  
      self.RecurringInv:bool = obj["RecurringInv"]
      """  Indicates that Service Contract with this Code will generate recurring invoices.  """  
      self.RecurringFreq:str = obj["RecurringFreq"]
      """  The frequency that recurring invoices are generated only 'monthly' for now.  """  
      self.PricePer:str = obj["PricePer"]
      """  Price modifier for unit price field Daily, monthly, Contract(Full length of the contract)  """  
      self.LastInvGen:bool = obj["LastInvGen"]
      """  This flag is set to TRUE after the last recurring invoice is generated for the contract.  """  
      self.TaxCatID:str = obj["TaxCatID"]
      """  Indicates the Tax Category for this record.  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.ReadyToInvoice:bool = obj["ReadyToInvoice"]
      """  Indicates if the contract is ready to be invoiced.   This is only available when ShipContract = no.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  The Sales order that this contract is linked to.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  The line number of the sales order that this contract is linked to  """  
      self.Duration:int = obj["Duration"]
      """  Duration of Contract  """  
      self.RenewalComment:str = obj["RenewalComment"]
      """  Used to establish invoice comments about the overall Renewal.  """  
      self.RenewEffDate:str = obj["RenewEffDate"]
      """  Date when the renewal begins.  """  
      self.RenewedUntil:str = obj["RenewedUntil"]
      """  Date the renewal ends.  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.InvcTiming:str = obj["InvcTiming"]
      """  InvcTiming  """  
      self.ContractCode:str = obj["ContractCode"]
      """  It is the same as the contract type but applied to renewals  """  
      self.Modifier:str = obj["Modifier"]
      """  The unit of measure of time that the renewal contract lasts.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  Indicates how often an invoice is generated for the contract  """  
      self.Renewable:bool = obj["Renewable"]
      """  Indicates if the service contract is valid for renewal  """  
      self.RenewalTotal:int = obj["RenewalTotal"]
      """  Total Renewal Amount  """  
      self.DocRenewalTotal:int = obj["DocRenewalTotal"]
      self.Rpt1RenewalTotal:int = obj["Rpt1RenewalTotal"]
      self.Rpt2RenewalTotal:int = obj["Rpt2RenewalTotal"]
      self.Rpt3RenewalTotal:int = obj["Rpt3RenewalTotal"]
      self.RenewalExpired:bool = obj["RenewalExpired"]
      """  Indicates if the Contract Renewal has expired.  """  
      self.RenewalRenewed:bool = obj["RenewalRenewed"]
      """  Indicates if the Contract Renewal has been renewed.  """  
      self.RenewalVoid:bool = obj["RenewalVoid"]
      """  Indicates if the related Contract Header has been voided.  """  
      self.AllowUpdate:bool = obj["AllowUpdate"]
      self.UninvoicedLine:bool = obj["UninvoicedLine"]
      """  Flag to indicate if additional uninvoiced renewal line has been added after the renewal header has been invoiced.  """  
      self.FiscalCalDescription:str = obj["FiscalCalDescription"]
      self.ReadyToQuote:bool = obj["ReadyToQuote"]
      """  Flag to indicate if the Contract Renewal is ready to be quoted.  """  
      self.EnableQuote:bool = obj["EnableQuote"]
      self.EnableRenewable:bool = obj["EnableRenewable"]
      """  Flag to indicate when to enable the Renewable check box.  The flag is set to no if the current contract renewal has been renewed already (another FSRenewal exists).  """  
      self.UpdateLineDates:bool = obj["UpdateLineDates"]
      self.ContractCodeDescription:str = obj["ContractCodeDescription"]
      self.BitFlag:int = obj["BitFlag"]
      self.CodeContractDescription:str = obj["CodeContractDescription"]
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      self.RACodeRADesc:str = obj["RACodeRADesc"]
      self.TaskSetWorkflowType:str = obj["TaskSetWorkflowType"]
      self.TaskSetTaskSetDescription:str = obj["TaskSetTaskSetDescription"]
      self.TaxCatIDDescription:str = obj["TaxCatIDDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_FSRenewalSNRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier  """  
      self.ContractNum:int = obj["ContractNum"]
      """  Contract Number of the Contract  """  
      self.RenewalNbr:int = obj["RenewalNbr"]
      """  Contract renewal number. If the value is zero then the contract is not for a renewal.  """  
      self.RenewalLine:int = obj["RenewalLine"]
      """  This field along with Company and ContractNum make up the unique key to the table.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part. Not directly maintainable. Mirror image of FSContDt.PartNum. Having this field, allows a SerialNo record to find the contracts that it is related to.  """  
      self.SerialNumber:str = obj["SerialNumber"]
      """  Serial number of the Part that is assigned to this Field Service contract line.  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.FSContCdDesc:str = obj["FSContCdDesc"]
      """  Description of the contract header contract type, for display in SerialNo tracker  """  
      self.IntExternalKey:str = obj["IntExternalKey"]
      """  Unique identifier of related integration record.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SNFormatRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier. This field cannot be blank.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part and is used in the primary key.  """  
      self.NumberOfDigits:int = obj["NumberOfDigits"]
      """  Number of digits in the serial number  """  
      self.SNMask:str = obj["SNMask"]
      """  If the SNBaseDataType is Mask this is the Serial Mask ID assigned for format validation/generation.  """  
      self.SNBaseDataType:str = obj["SNBaseDataType"]
      """   Current setting for Data type of the Base Serial Number field to be used as new serial numbers are generated. Valid values; Character, Integer, Mask
Code/desc required:
CHARACTER`Alphanumeric
INTEGER`NumericOnly
MASK`Serial Mask
This field should be flagged as Include = true in Object Designer.  """  
      self.SNFormat:str = obj["SNFormat"]
      """   Current setting for Format of the Base serial number that will be used as new serial numbers are generated. Expressed in progress syntax. Ex: X(30), 99999999 for Character or Integer, or as a Serial Mask defined in SerialMask table.
This field should be flagged as ReadOnly and Include = true in Object Designer.  """  
      self.LeadingZeroes:bool = obj["LeadingZeroes"]
      """  Whether or not to have leading zeroes  """  
      self.SNPrefix:str = obj["SNPrefix"]
      """   Current setting for the prefix that will be attached to all new Serial Numbers as they are generated for Character and Integer format types.
This field should be flagged as Include = true in Object Designer.  """  
      self.SNMaskSuffix:str = obj["SNMaskSuffix"]
      """  A standard suffix that will be attached to all serial numbers generated for the PartSite currently used only by SNBaseStructure Mask types  """  
      self.SNMaskPrefix:str = obj["SNMaskPrefix"]
      """  The prefix that was used to construct the serial number currently used only by SNBaseStructure Mask types  """  
      self.SNLastUsedSeq:str = obj["SNLastUsedSeq"]
      """  This is the last used serial sequence. It is used only for the Mask Generate type to determine the next logical serial number to generate for this part/Site. It can be altered by the user and several PartSites can have the same counter values defined, but  """  
      self.HasSerialNumbers:bool = obj["HasSerialNumbers"]
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.PartPricePerCode:str = obj["PartPricePerCode"]
      self.PartTrackLots:bool = obj["PartTrackLots"]
      self.PartTrackSerialNum:bool = obj["PartTrackSerialNum"]
      self.PartTrackDimension:bool = obj["PartTrackDimension"]
      self.PartSalesUM:str = obj["PartSalesUM"]
      self.PartIUM:str = obj["PartIUM"]
      self.PartSellingFactor:int = obj["PartSellingFactor"]
      self.PartPartDescription:str = obj["PartPartDescription"]
      self.SerialMaskMaskType:int = obj["SerialMaskMaskType"]
      self.SerialMaskMask:str = obj["SerialMaskMask"]
      self.SerialMaskExample:str = obj["SerialMaskExample"]
      self.SerialMaskDescription:str = obj["SerialMaskDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SelectSerialNumbersParamsRow:
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      """  The part number to which the serial numbers have been assigned.  """  
      self.quantity:int = obj["quantity"]
      """  The quantity of serial numbers that need to be selected.  """  
      self.whereClause:str = obj["whereClause"]
      """  whereClause for filtering available serial numbers  """  
      self.transType:str = obj["transType"]
      """  transType of this transaction  """  
      self.sourceRowID:str = obj["sourceRowID"]
      """  Include when filtering a set of SN's for BL processing is necessary.  It may be null if not needed.  """  
      self.enableCreate:bool = obj["enableCreate"]
      """  Determines if serial numbers can be created.  """  
      self.enableSelect:bool = obj["enableSelect"]
      """  Determines if serial numbers can be selected.  """  
      self.enableRetrieve:bool = obj["enableRetrieve"]
      """  Determines if serial numbers can be retrieved.  """  
      self.allowVoided:bool = obj["allowVoided"]
      """  Specifies whether Voided serial numbers can be manually selected.  """  
      self.plant:str = obj["plant"]
      """  The Plant associated with this transaction  """  
      self.xrefPartNum:str = obj["xrefPartNum"]
      self.xrefPartType:str = obj["xrefPartType"]
      self.xrefCustNum:int = obj["xrefCustNum"]
      self.poLinkValues:str = obj["poLinkValues"]
      """  temporary field used to link the packout lines to ship detail lines  """  
      self.attributeSetID:int = obj["attributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.attributeSetShortDescription:str = obj["attributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.revisionNum:str = obj["revisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SelectSerialNumbersParamsTableset:
   def __init__(self, obj):
      self.SelectSerialNumbersParams:list[Erp_Tablesets_SelectSerialNumbersParamsRow] = obj["SelectSerialNumbersParams"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_SelectedSerialNumbersRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.SerialNumber:str = obj["SerialNumber"]
      """  SerialNumber  """  
      self.Scrapped:bool = obj["Scrapped"]
      """  Scrapped flag  """  
      self.ScrappedReasonCode:str = obj["ScrappedReasonCode"]
      """  Scrapped reason code  """  
      self.Voided:bool = obj["Voided"]
      """  Voided flag  """  
      self.Reference:str = obj["Reference"]
      """  Reference field  """  
      self.ReasonCodeType:str = obj["ReasonCodeType"]
      """  Reason code type = s  """  
      self.ReasonCodeDesc:str = obj["ReasonCodeDesc"]
      """  Reason code description  """  
      self.PartNum:str = obj["PartNum"]
      """  PartNumber  """  
      self.SNPrefix:str = obj["SNPrefix"]
      """  Serial number prefix  """  
      self.SNBaseNumber:str = obj["SNBaseNumber"]
      """  Base number used to create the serial number  """  
      self.SourceRowID:str = obj["SourceRowID"]
      """  RowID of the source record for this serial number  """  
      self.TransType:str = obj["TransType"]
      """  TransType of the record that created this serial number  """  
      self.PassedInspection:bool = obj["PassedInspection"]
      """  True if this serial numbered part passed inspection  """  
      self.Deselected:bool = obj["Deselected"]
      """  Used to flag previously selected serial numbers as deselected  """  
      self.KitWhseList:str = obj["KitWhseList"]
      self.RawSerialNum:str = obj["RawSerialNum"]
      """  This will be the raw serial number as it was scanned or entered into the system. This would only differ from the SerialNumber field if a validate type mask was being used where characters were stripped (using ~ in the mask).  """  
      self.KBLbrAction:int = obj["KBLbrAction"]
      """  Action type field used for Kanban receipts to indicate if the new serial number status is Inventory, Scrapped or NonConf.  This requires Code/desc:  1 ` inventory 2 ` Scrapped 3 ` Nonconformance  """  
      self.KBLbrActionDesc:str = obj["KBLbrActionDesc"]
      """  Description field for KBLbrAction ? holds the translated description for the KBLbrAction code for UI display and combo box.  """  
      self.PreventDeselect:bool = obj["PreventDeselect"]
      """  If true, then users can not deselect this serial number.  This is used by applications that allow maintenance to the Selected Serial Numbers after update.  """  
      self.XRefPartNum:str = obj["XRefPartNum"]
      """  Used only by SN Assignment  """  
      self.XRefPartType:str = obj["XRefPartType"]
      """  Used only by SN Assignment: C = Customer Part / I = Internal Part XRef  """  
      self.PreDeselected:bool = obj["PreDeselected"]
      self.poLinkValues:str = obj["poLinkValues"]
      """  temporary field used to link the packout lines to ship detail lines  """  
      self.SNMask:str = obj["SNMask"]
      """  The mask the was used to generate the serial number  """  
      self.NotSavedToDB:bool = obj["NotSavedToDB"]
      """  Flag to indicate that the SelectedSerialNumbers entry has not yet been saved to the DB for the related transaction. Used to keep track of which deselected serial numbers need to be passed to the transaction update logic.  """  
      self.RowSelected:bool = obj["RowSelected"]
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ServiceContractTableset:
   def __init__(self, obj):
      self.FSContHd:list[Erp_Tablesets_FSContHdRow] = obj["FSContHd"]
      self.FSContDt:list[Erp_Tablesets_FSContDtRow] = obj["FSContDt"]
      self.FSContSN:list[Erp_Tablesets_FSContSNRow] = obj["FSContSN"]
      self.FSRenewal:list[Erp_Tablesets_FSRenewalRow] = obj["FSRenewal"]
      self.FSRenewalDt:list[Erp_Tablesets_FSRenewalDtRow] = obj["FSRenewalDt"]
      self.FSRenewalSN:list[Erp_Tablesets_FSRenewalSNRow] = obj["FSRenewalSN"]
      self.FSContLabExpRate:list[Erp_Tablesets_FSContLabExpRateRow] = obj["FSContLabExpRate"]
      self.FSContOrderDtlList:list[Erp_Tablesets_FSContOrderDtlListRow] = obj["FSContOrderDtlList"]
      self.SelectedSerialNumbers:list[Erp_Tablesets_SelectedSerialNumbersRow] = obj["SelectedSerialNumbers"]
      self.SNFormat:list[Erp_Tablesets_SNFormatRow] = obj["SNFormat"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtServiceContractTableset:
   def __init__(self, obj):
      self.FSContHd:list[Erp_Tablesets_FSContHdRow] = obj["FSContHd"]
      self.FSContDt:list[Erp_Tablesets_FSContDtRow] = obj["FSContDt"]
      self.FSContSN:list[Erp_Tablesets_FSContSNRow] = obj["FSContSN"]
      self.FSRenewal:list[Erp_Tablesets_FSRenewalRow] = obj["FSRenewal"]
      self.FSRenewalDt:list[Erp_Tablesets_FSRenewalDtRow] = obj["FSRenewalDt"]
      self.FSRenewalSN:list[Erp_Tablesets_FSRenewalSNRow] = obj["FSRenewalSN"]
      self.FSContLabExpRate:list[Erp_Tablesets_FSContLabExpRateRow] = obj["FSContLabExpRate"]
      self.FSContOrderDtlList:list[Erp_Tablesets_FSContOrderDtlListRow] = obj["FSContOrderDtlList"]
      self.SelectedSerialNumbers:list[Erp_Tablesets_SelectedSerialNumbersRow] = obj["SelectedSerialNumbers"]
      self.SNFormat:list[Erp_Tablesets_SNFormatRow] = obj["SNFormat"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class ExpireContract_input:
   """ Required : 
   ipContractNum
   ds
   """  
   def __init__(self, obj):
      self.ipContractNum:int = obj["ipContractNum"]
      """  The contract number to expire  """  
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

class ExpireContract_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

      """  output parameters  """  

class FrequencyList_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.FrequencyList:str = obj["parameters"]
      pass

      """  output parameters  """  

class GenerateRenewalLines_input:
   """ Required : 
   ipContractNum
   ipRenewalNbr
   ds
   """  
   def __init__(self, obj):
      self.ipContractNum:int = obj["ipContractNum"]
      """  The target contract number.  """  
      self.ipRenewalNbr:int = obj["ipRenewalNbr"]
      """  The target renewal number.  """  
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

class GenerateRenewalLines_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GenerateRenewal_input:
   """ Required : 
   ipContractNum
   ds
   """  
   def __init__(self, obj):
      self.ipContractNum:int = obj["ipContractNum"]
      """  The source contract number.  """  
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

class GenerateRenewal_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetByID_input:
   """ Required : 
   contractNum
   """  
   def __init__(self, obj):
      self.contractNum:int = obj["contractNum"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ServiceContractTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ServiceContractTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ServiceContractTableset] = obj["returnObj"]
      pass

class GetListCustom_input:
   """ Required : 
   ContractNumList
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.ContractNumList:str = obj["ContractNumList"]
      """  The contract number list  """  
      self.pageSize:int = obj["pageSize"]
      """  The pageSize number list  """  
      self.absolutePage:int = obj["absolutePage"]
      """  The absolutePage number list  """  
      pass

class GetListCustom_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_FSContHdListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

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
      self.returnObj:list[Erp_Tablesets_FSContHdListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewFSContDt_input:
   """ Required : 
   ds
   contractNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      self.contractNum:int = obj["contractNum"]
      pass

class GetNewFSContDt_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewFSContHdFromOrder_input:
   """ Required : 
   OrderNum
   ds
   """  
   def __init__(self, obj):
      self.OrderNum:int = obj["OrderNum"]
      """  The order number  """  
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

class GetNewFSContHdFromOrder_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewFSContHd_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

class GetNewFSContHd_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewFSContLabExpRate_input:
   """ Required : 
   ds
   contractNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      self.contractNum:int = obj["contractNum"]
      pass

class GetNewFSContLabExpRate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewFSContSN_input:
   """ Required : 
   ds
   contractNum
   contractLine
   partNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      self.contractNum:int = obj["contractNum"]
      self.contractLine:int = obj["contractLine"]
      self.partNum:str = obj["partNum"]
      pass

class GetNewFSContSN_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewFSRenewalDt_input:
   """ Required : 
   ds
   contractNum
   renewalNbr
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      self.contractNum:int = obj["contractNum"]
      self.renewalNbr:int = obj["renewalNbr"]
      pass

class GetNewFSRenewalDt_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewFSRenewalSN_input:
   """ Required : 
   ds
   contractNum
   renewalNbr
   renewalLine
   partNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      self.contractNum:int = obj["contractNum"]
      self.renewalNbr:int = obj["renewalNbr"]
      self.renewalLine:int = obj["renewalLine"]
      self.partNum:str = obj["partNum"]
      pass

class GetNewFSRenewalSN_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewFSRenewal_input:
   """ Required : 
   ds
   contractNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      self.contractNum:int = obj["contractNum"]
      pass

class GetNewFSRenewal_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRenewalSelectSerialNumbersParams_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

class GetRenewalSelectSerialNumbersParams_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_SelectSerialNumbersParamsTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRenewalSelectedSerialNumbers_input:
   """ Required : 
   iContractNum
   iRenewalNbr
   iRenewalLine
   iPartNum
   ds
   """  
   def __init__(self, obj):
      self.iContractNum:int = obj["iContractNum"]
      """  The Contract Number  """  
      self.iRenewalNbr:int = obj["iRenewalNbr"]
      """  The Contract Renewal number  """  
      self.iRenewalLine:int = obj["iRenewalLine"]
      """  The Contract Renewal Line number  """  
      self.iPartNum:str = obj["iPartNum"]
      """  The Part Num  """  
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

class GetRenewalSelectedSerialNumbers_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRowsContactTracker_input:
   """ Required : 
   whereClauseFSContHd
   whereClauseFSContDt
   whereClauseFSContSN
   whereClauseSelectedSerialNumbers
   whereClauseSerialNumberSearch
   whereClauseSNFormat
   contactName
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseFSContHd:str = obj["whereClauseFSContHd"]
      """  Whereclause for FSContHd table.  """  
      self.whereClauseFSContDt:str = obj["whereClauseFSContDt"]
      """  Whereclause for FSContDt table.  """  
      self.whereClauseFSContSN:str = obj["whereClauseFSContSN"]
      """  Whereclause for FSContSN table.  """  
      self.whereClauseSelectedSerialNumbers:str = obj["whereClauseSelectedSerialNumbers"]
      """  Whereclause for SelectedSerialNumbers.  """  
      self.whereClauseSerialNumberSearch:str = obj["whereClauseSerialNumberSearch"]
      """  Whereclause for SerialNumberSearch  """  
      self.whereClauseSNFormat:str = obj["whereClauseSNFormat"]
      """  Whereclause for SNFormat table.  """  
      self.contactName:str = obj["contactName"]
      """  Contact to return data for.  """  
      self.pageSize:int = obj["pageSize"]
      """  Page size.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Absolute page.  """  
      pass

class GetRowsContactTracker_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_FSContCustTrkTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRowsCustom_input:
   """ Required : 
   ContractNumList
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.ContractNumList:str = obj["ContractNumList"]
      """  The contract number list  """  
      self.pageSize:int = obj["pageSize"]
      """  The pageSize number list  """  
      self.absolutePage:int = obj["absolutePage"]
      """  The absolutePage number list  """  
      pass

class GetRowsCustom_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ServiceContractTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRowsCustomerTrackerActive_input:
   """ Required : 
   whereClauseFSContHd
   whereClauseFSContDt
   whereClauseFSContSN
   whereClauseSelectedSerialNumbers
   whereClauseSerialNumberSearch
   whereClauseSNFormat
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseFSContHd:str = obj["whereClauseFSContHd"]
      """  Whereclause for FSContHd table.  """  
      self.whereClauseFSContDt:str = obj["whereClauseFSContDt"]
      """  Whereclause for FSContDt table.  """  
      self.whereClauseFSContSN:str = obj["whereClauseFSContSN"]
      """  Whereclause for FSContSN table.  """  
      self.whereClauseSelectedSerialNumbers:str = obj["whereClauseSelectedSerialNumbers"]
      """  Whereclause for SelectedSerialNumbers.  """  
      self.whereClauseSerialNumberSearch:str = obj["whereClauseSerialNumberSearch"]
      """  Whereclause for SerialNumberSearch  """  
      self.whereClauseSNFormat:str = obj["whereClauseSNFormat"]
      """  Whereclause for SNFormat table.  """  
      self.pageSize:int = obj["pageSize"]
      """  Page size.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Absolute page.  """  
      pass

class GetRowsCustomerTrackerActive_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_FSContCustTrkTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRowsCustomerTrackerExpired_input:
   """ Required : 
   whereClauseFSContHd
   whereClauseFSContDt
   whereClauseFSContSN
   whereClauseSelectedSerialNumbers
   whereClauseSerialNumberSearch
   whereClauseSNFormat
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseFSContHd:str = obj["whereClauseFSContHd"]
      """  Whereclause for FSContHd table.  """  
      self.whereClauseFSContDt:str = obj["whereClauseFSContDt"]
      """  Whereclause for FSContDt table.  """  
      self.whereClauseFSContSN:str = obj["whereClauseFSContSN"]
      """  Whereclause for FSContSN table.  """  
      self.whereClauseSelectedSerialNumbers:str = obj["whereClauseSelectedSerialNumbers"]
      """  Whereclause for SelectedSerialNumbers.  """  
      self.whereClauseSerialNumberSearch:str = obj["whereClauseSerialNumberSearch"]
      """  Whereclause for SerialNumberSearch  """  
      self.whereClauseSNFormat:str = obj["whereClauseSNFormat"]
      """  Whereclause for SNFormat table.  """  
      self.pageSize:int = obj["pageSize"]
      """  Page size.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Absolute page.  """  
      pass

class GetRowsCustomerTrackerExpired_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_FSContCustTrkTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRowsCustomerTracker_input:
   """ Required : 
   whereClauseFSContHd
   whereClauseFSContDt
   whereClauseFSContSN
   whereClauseSelectedSerialNumbers
   whereClauseSerialNumberSearch
   whereClauseSNFormat
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseFSContHd:str = obj["whereClauseFSContHd"]
      """  Whereclause for FSContHd table.  """  
      self.whereClauseFSContDt:str = obj["whereClauseFSContDt"]
      """  Whereclause for FSContDt table.  """  
      self.whereClauseFSContSN:str = obj["whereClauseFSContSN"]
      """  Whereclause for FSContSN table.  """  
      self.whereClauseSelectedSerialNumbers:str = obj["whereClauseSelectedSerialNumbers"]
      """  Whereclause for SelectedSerialNumbers.  """  
      self.whereClauseSerialNumberSearch:str = obj["whereClauseSerialNumberSearch"]
      """  Whereclause for SerialNumberSearch  """  
      self.whereClauseSNFormat:str = obj["whereClauseSNFormat"]
      """  Whereclause for SNFormat table.  """  
      self.pageSize:int = obj["pageSize"]
      """  Page size.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Absolute page.  """  
      pass

class GetRowsCustomerTracker_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_FSContCustTrkTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseFSContHd
   whereClauseFSContDt
   whereClauseFSContSN
   whereClauseFSRenewal
   whereClauseFSRenewalDt
   whereClauseFSRenewalSN
   whereClauseFSContLabExpRate
   whereClauseFSContOrderDtlList
   whereClauseSelectedSerialNumbers
   whereClauseSNFormat
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseFSContHd:str = obj["whereClauseFSContHd"]
      self.whereClauseFSContDt:str = obj["whereClauseFSContDt"]
      self.whereClauseFSContSN:str = obj["whereClauseFSContSN"]
      self.whereClauseFSRenewal:str = obj["whereClauseFSRenewal"]
      self.whereClauseFSRenewalDt:str = obj["whereClauseFSRenewalDt"]
      self.whereClauseFSRenewalSN:str = obj["whereClauseFSRenewalSN"]
      self.whereClauseFSContLabExpRate:str = obj["whereClauseFSContLabExpRate"]
      self.whereClauseFSContOrderDtlList:str = obj["whereClauseFSContOrderDtlList"]
      self.whereClauseSelectedSerialNumbers:str = obj["whereClauseSelectedSerialNumbers"]
      self.whereClauseSNFormat:str = obj["whereClauseSNFormat"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ServiceContractTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetSelectSerialNumbersParams_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

class GetSelectSerialNumbersParams_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_SelectSerialNumbersParamsTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetSelectedSerialNumbers_input:
   """ Required : 
   iContractNum
   iContractLine
   iPartNum
   ds
   """  
   def __init__(self, obj):
      self.iContractNum:int = obj["iContractNum"]
      """  The Contract Number  """  
      self.iContractLine:int = obj["iContractLine"]
      """  The Contract Detail line number  """  
      self.iPartNum:str = obj["iPartNum"]
      """  The Part Num  """  
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

class GetSelectedSerialNumbers_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
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

class IsPlantSerialTracking_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.isSerialTracking:bool = obj["isSerialTracking"]
      pass

      """  output parameters  """  

class PricePerList_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.PricePerList:str = obj["parameters"]
      pass

      """  output parameters  """  

class SuspendContract_input:
   """ Required : 
   ipSuspend
   ipReasonCode
   ds
   """  
   def __init__(self, obj):
      self.ipSuspend:bool = obj["ipSuspend"]
      """  The requested Suspend or Unsuspend status change.  """  
      self.ipReasonCode:str = obj["ipReasonCode"]
      """  The Reason Code for the hold request.  """  
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

class SuspendContract_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtServiceContractTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtServiceContractTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateOTSTaxID_input:
   """ Required : 
   ds
   manualValidation
   hmrcFraudPrevHeader
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      self.manualValidation:bool = obj["manualValidation"]
      self.hmrcFraudPrevHeader:str = obj["hmrcFraudPrevHeader"]
      pass

class ValidateOTSTaxID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      self.opMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class ValidateSN_input:
   """ Required : 
   ds
   serialNumber
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      self.serialNumber:str = obj["serialNumber"]
      """  Serial number to validate.  """  
      pass

class ValidateSN_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      self.isVoided:bool = obj["isVoided"]
      pass

      """  output parameters  """  

class VoidContract_input:
   """ Required : 
   VoidContractNum
   ds
   """  
   def __init__(self, obj):
      self.VoidContractNum:int = obj["VoidContractNum"]
      """  The contract number to void  """  
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

class VoidContract_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

      """  output parameters  """  

class isContractExpired_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

class isContractExpired_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      """  Returns true if expired, false if not expired.  """  
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ServiceContractTableset] = obj["ds"]
      pass

      """  output parameters  """  

